#!/usr/bin/env python3
"""Migrate Avail Forum governance material into a self-contained GitHub archive.

The script fetches public Discourse category/topic data, stores source snapshots,
downloads forum-hosted assets referenced by migrated posts, and writes readable
Markdown wrappers around the preserved Discourse HTML.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qs, quote_plus, unquote, urljoin, urlparse

import requests


FORUM_BASE = "https://forum.availproject.org"
GOVERNANCE_CATEGORY_IDS = [32, 33, 34, 35]
CATEGORY_NAMES = {
    32: "Governance V1",
    33: "Avail Improvement Proposal (AIP)",
    34: "Avail Transparency Report",
    35: "Technical Committee",
}
CATEGORY_DESTINATIONS = {
    33: "AIPs",
    34: "transparency-reports",
    35: "committees",
}
GENERATED_AT = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_DIR = ROOT
ARCHIVE_DIR = GOVERNANCE_DIR / "archive"
RAW_JSON_DIR = ARCHIVE_DIR / "raw-json"
RAW_HTML_DIR = ARCHIVE_DIR / "raw-html"
ASSET_DIR = ARCHIVE_DIR / "assets"

ATTR_RE = re.compile(
    r"(?P<prefix>\b(?:src|href)=)(?P<quote>[\"'])(?P<url>.*?)(?P=quote)",
    re.IGNORECASE,
)
SRCSET_RE = re.compile(
    r"(?P<prefix>\bsrcset=)(?P<quote>[\"'])(?P<srcset>.*?)(?P=quote)",
    re.IGNORECASE,
)
AIP_RE = re.compile(r"^\s*AIP\s+(\d+)\s*:\s*(.+)$", re.IGNORECASE)
TRANSPARENCY_RE = re.compile(
    r"^\s*(?:Avail\s+)?Transparency\s+[Rr]eport\s+(\d+)\s*:\s*(.+)$"
)
OFFICIAL_TITLE_RE = re.compile(
    r"^\s*(AIP\s+\d+|(?:Avail\s+)?Transparency\s+[Rr]eport\s+\d+|"
    r"Avail\s+(?:Fee Pricing|Technical)\s+Committee|Technical Committee|About the .*category)",
    re.IGNORECASE,
)


@dataclass
class TopicRecord:
    topic_id: int
    title: str
    slug: str
    category_id: int
    source_url: str
    destination_dir: str
    destination_path: Path
    topic_json_path: Path
    topic_html_path: Path
    posts_included: int = 0
    highest_post_number: Optional[int] = None
    assets: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


class Fetcher:
    def __init__(self, delay_seconds: float) -> None:
        self.delay_seconds = delay_seconds
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Avail governance migration script "
                    "(self-contained GitHub archive)"
                )
            }
        )

    def get_text(self, url: str) -> str:
        time.sleep(self.delay_seconds)
        response = self.session.get(url, timeout=60)
        response.raise_for_status()
        return response.text

    def get_bytes(self, url: str) -> bytes:
        time.sleep(self.delay_seconds)
        response = self.session.get(url, timeout=60)
        response.raise_for_status()
        return response.content


def ensure_dirs() -> None:
    for path in [
        GOVERNANCE_DIR / "AIPs",
        GOVERNANCE_DIR / "transparency-reports",
        GOVERNANCE_DIR / "committees",
        RAW_JSON_DIR,
        RAW_HTML_DIR,
        ASSET_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def relpath(from_file: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_file.parent).replace(os.sep, "/")


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "topic"


def topic_source_url(slug: str, topic_id: int) -> str:
    return f"{FORUM_BASE}/t/{slug}/{topic_id}"


def classify_topic(title: str, category_id: int) -> str:
    if AIP_RE.match(title) or category_id == 33:
        return "AIPs"
    if TRANSPARENCY_RE.match(title) or category_id == 34:
        return "transparency-reports"
    if (
        "committee" in title.lower()
        or "fee pricing" in title.lower()
        or category_id == 35
    ):
        return "committees"
    return "."


def filename_for_topic(title: str, slug: str, destination_dir: str) -> str:
    aip_match = AIP_RE.match(title)
    if aip_match:
        rest = slug
        rest = re.sub(r"^aip-\d+-?", "", rest)
        return f"aip-{int(aip_match.group(1)):03d}-{rest or slugify(aip_match.group(2))}.md"

    transparency_match = TRANSPARENCY_RE.match(title)
    if transparency_match:
        rest = slug
        rest = re.sub(r"^(avail-)?transparency-report-\d+-?", "", rest)
        return (
            f"transparency-report-{int(transparency_match.group(1)):03d}-"
            f"{rest or slugify(transparency_match.group(2))}.md"
        )

    prefix = ""
    if title.lower().startswith("about the ") and destination_dir in {
        "AIPs",
        "transparency-reports",
        "committees",
    }:
        return f"{slugify(slug or title)}.md"

    return f"{prefix}{slugify(slug or title)}.md"


def is_official_search_hit(topic: dict) -> bool:
    title = topic.get("title") or ""
    category_id = int(topic.get("category_id") or 0)
    if category_id in GOVERNANCE_CATEGORY_IDS:
        return True
    return bool(OFFICIAL_TITLE_RE.match(title))


def parse_json(text: str, source: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Could not parse JSON from {source}: {exc}") from exc


def category_url(category_id: int, page: int) -> str:
    return f"{FORUM_BASE}/c/{category_id}.json?page={page}"


def collect_topic_summaries(fetcher: Fetcher) -> Tuple[Dict[int, dict], List[str]]:
    topic_summaries: Dict[int, dict] = {}
    audit_notes: List[str] = []

    categories_text = fetcher.get_text(f"{FORUM_BASE}/categories.json")
    write_text(RAW_JSON_DIR / "categories.json", categories_text)

    for category_id in GOVERNANCE_CATEGORY_IDS:
        page = 0
        while True:
            url = category_url(category_id, page)
            text = fetcher.get_text(url)
            write_text(RAW_JSON_DIR / f"category-{category_id}-page-{page}.json", text)
            data = parse_json(text, url)
            topics = data.get("topic_list", {}).get("topics", [])
            for topic in topics:
                if not topic.get("visible", True):
                    continue
                topic_id = int(topic["id"])
                topic_summaries.setdefault(topic_id, topic)

            more_topics_url = data.get("topic_list", {}).get("more_topics_url")
            if not more_topics_url:
                break
            page += 1

    audit_notes.append(
        "Inventory source: Governance V1 category pages and direct subcategory pages "
        "for AIPs, transparency reports, and the technical committee."
    )

    return topic_summaries, audit_notes


def build_topic_records(topic_summaries: Dict[int, dict]) -> Dict[int, TopicRecord]:
    records: Dict[int, TopicRecord] = {}
    used_paths: Dict[Path, int] = {}

    for topic_id, summary in sorted(topic_summaries.items()):
        title = summary.get("title") or f"Topic {topic_id}"
        slug = summary.get("slug") or slugify(title)
        category_id = int(summary.get("category_id") or 0)
        destination_dir = classify_topic(title, category_id)
        filename = filename_for_topic(title, slug, destination_dir)
        destination_path = GOVERNANCE_DIR / destination_dir / filename
        if destination_path in used_paths:
            stem = destination_path.stem
            destination_path = destination_path.with_name(f"{stem}-{topic_id}.md")
        used_paths[destination_path] = topic_id

        records[topic_id] = TopicRecord(
            topic_id=topic_id,
            title=title,
            slug=slug,
            category_id=category_id,
            source_url=topic_source_url(slug, topic_id),
            destination_dir=destination_dir,
            destination_path=destination_path,
            topic_json_path=RAW_JSON_DIR / f"topic-{topic_id}.json",
            topic_html_path=RAW_HTML_DIR / f"topic-{topic_id}.html",
        )

    return records


def full_url(url: str) -> str:
    return urljoin(FORUM_BASE, html.unescape(url))


def is_forum_asset(url: str) -> bool:
    parsed = urlparse(full_url(url))
    host = parsed.netloc.lower()
    path = parsed.path
    if host == "forum.availproject.org" and path.startswith("/uploads/"):
        return True
    if "discourse-cdn.com" in host and "/uploads/availproject/" in path:
        return True
    if host == "emoji.discourse-cdn.com":
        return True
    return False


def is_forum_topic_url(url: str) -> bool:
    parsed = urlparse(full_url(url))
    return parsed.netloc.lower() == "forum.availproject.org" and parsed.path.startswith(
        "/t/"
    )


def parse_topic_link(url: str) -> Tuple[Optional[int], Optional[int]]:
    parsed = urlparse(full_url(url))
    parts = [part for part in parsed.path.split("/") if part]
    topic_id: Optional[int] = None
    post_number: Optional[int] = None
    if len(parts) >= 3 and parts[0] == "t":
        for part in parts[1:]:
            if part.isdigit():
                if topic_id is None:
                    topic_id = int(part)
                else:
                    post_number = int(part)
                    break
    if parsed.fragment and parsed.fragment.startswith("post_"):
        maybe_number = parsed.fragment.removeprefix("post_")
        if maybe_number.isdigit():
            post_number = int(maybe_number)
    query_post = parse_qs(parsed.query).get("post")
    if query_post and query_post[0].isdigit():
        post_number = int(query_post[0])
    return topic_id, post_number


def safe_asset_filename(url: str) -> str:
    parsed = urlparse(full_url(url))
    basename = unquote(Path(parsed.path).name) or "asset"
    basename = slugify(Path(basename).stem) + Path(basename).suffix.lower()
    if "." not in basename:
        basename += ".bin"
    digest = hashlib.sha256(full_url(url).encode("utf-8")).hexdigest()[:12]
    return f"{digest}-{basename}"


def download_asset(
    fetcher: Fetcher,
    url: str,
    record: TopicRecord,
    asset_cache: Dict[str, Path],
) -> Optional[Path]:
    normalized = full_url(url)
    if normalized in asset_cache:
        return asset_cache[normalized]

    path = ASSET_DIR / str(record.topic_id) / safe_asset_filename(normalized)
    try:
        if not path.exists():
            write_bytes(path, fetcher.get_bytes(normalized))
        asset_cache[normalized] = path
        archive_rel = path.relative_to(GOVERNANCE_DIR).as_posix()
        if archive_rel not in record.assets:
            record.assets.append(archive_rel)
        return path
    except Exception as exc:
        record.notes.append(f"Asset download failed for `{normalized}`: {exc}")
        return None


def rewrite_url(
    fetcher: Fetcher,
    url: str,
    record: TopicRecord,
    topic_destinations: Dict[int, Path],
    asset_cache: Dict[str, Path],
) -> str:
    unescaped = html.unescape(url)
    if is_forum_asset(unescaped):
        asset_path = download_asset(fetcher, unescaped, record, asset_cache)
        if asset_path is not None:
            return relpath(record.destination_path, asset_path)
        return full_url(unescaped)

    if is_forum_topic_url(unescaped):
        topic_id, post_number = parse_topic_link(unescaped)
        if topic_id in topic_destinations:
            target = relpath(record.destination_path, topic_destinations[topic_id])
            if post_number:
                target += f"#post-{post_number}"
            return target
        return full_url(unescaped)

    parsed = urlparse(unescaped)
    if not parsed.scheme and unescaped.startswith("/"):
        return full_url(unescaped)
    return unescaped


def rewrite_html(
    fetcher: Fetcher,
    content: str,
    record: TopicRecord,
    topic_destinations: Dict[int, Path],
    asset_cache: Dict[str, Path],
) -> str:
    def replace(match: re.Match) -> str:
        original_url = match.group("url")
        rewritten = rewrite_url(
            fetcher, original_url, record, topic_destinations, asset_cache
        )
        return (
            f"{match.group('prefix')}{match.group('quote')}"
            f"{html.escape(rewritten, quote=True)}{match.group('quote')}"
        )

    rewritten_content = ATTR_RE.sub(replace, content or "")

    def replace_srcset(match: re.Match) -> str:
        srcset = html.unescape(match.group("srcset"))
        rewritten_parts = []
        for part in srcset.split(","):
            stripped = part.strip()
            if not stripped:
                continue
            pieces = stripped.split()
            src_url = pieces[0]
            descriptor = " ".join(pieces[1:])
            rewritten_src = rewrite_url(
                fetcher,
                src_url,
                record,
                topic_destinations,
                asset_cache,
            )
            rewritten_parts.append(
                " ".join(piece for piece in [rewritten_src, descriptor] if piece)
            )
        return (
            f"{match.group('prefix')}{match.group('quote')}"
            f"{html.escape(', '.join(rewritten_parts), quote=True)}"
            f"{match.group('quote')}"
        )

    return SRCSET_RE.sub(replace_srcset, rewritten_content)


def author_for(post: dict) -> str:
    name = post.get("name") or post.get("display_username") or post.get("username")
    username = post.get("username")
    if name and username and str(name).strip() and str(name).strip() != username:
        return f"{name} (@{username})"
    if username:
        return f"@{username}"
    return "Unknown"


def markdown_metadata_row(label: str, value: object) -> str:
    if value is None or value == "":
        value = "Unknown"
    value = str(value).replace("\n", " ")
    return f"| {label} | {value} |"


def post_markdown(post: dict, body_html: str, title: str) -> str:
    post_number = post.get("post_number")
    author = author_for(post)
    posted_at = post.get("created_at") or "Unknown"
    updated_at = post.get("updated_at")
    like_count = 0
    for action in post.get("actions_summary", []):
        if action.get("id") == 2:
            like_count = action.get("count") or 0
            break

    lines = [
        f'<a id="post-{post_number}"></a>',
        "",
        f"### {title}",
        "",
        "| Field | Value |",
        "| --- | --- |",
        markdown_metadata_row("Author", author),
        markdown_metadata_row("Posted", posted_at),
        markdown_metadata_row("Updated", updated_at),
        markdown_metadata_row("Forum post number", post_number),
        markdown_metadata_row("Forum post ID", post.get("id")),
        markdown_metadata_row("Likes", like_count),
        "",
        '<div class="discourse-post-content">',
        "",
        body_html.strip(),
        "",
        "</div>",
    ]
    return "\n".join(lines)


def topic_markdown(
    topic_data: dict,
    record: TopicRecord,
    fetcher: Fetcher,
    topic_destinations: Dict[int, Path],
    asset_cache: Dict[str, Path],
) -> str:
    posts = topic_data.get("post_stream", {}).get("posts", [])
    record.posts_included = len(posts)
    record.highest_post_number = topic_data.get("highest_post_number")
    if len(posts) != int(topic_data.get("posts_count") or len(posts)):
        record.notes.append(
            f"Topic JSON included {len(posts)} posts while posts_count is "
            f"{topic_data.get('posts_count')}"
        )

    if not posts:
        record.notes.append("Topic JSON contained no posts.")

    first_post = posts[0] if posts else {}
    source_category = CATEGORY_NAMES.get(record.category_id, f"Category {record.category_id}")
    raw_json_rel = relpath(record.destination_path, record.topic_json_path)
    raw_html_rel = relpath(record.destination_path, record.topic_html_path)

    lines = [
        f"# {record.title}",
        "",
        "> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.",
        "",
        "| Field | Value |",
        "| --- | --- |",
        markdown_metadata_row("Historical forum URL", record.source_url),
        markdown_metadata_row("Forum topic ID", record.topic_id),
        markdown_metadata_row("Original category", source_category),
        markdown_metadata_row("Original author", author_for(first_post) if first_post else ""),
        markdown_metadata_row("Created", topic_data.get("created_at")),
        markdown_metadata_row("Last posted", topic_data.get("last_posted_at")),
        markdown_metadata_row("Forum posts included", len(posts)),
        markdown_metadata_row("Highest forum post number", topic_data.get("highest_post_number")),
        markdown_metadata_row("Raw JSON snapshot", f"[{record.topic_json_path.name}]({raw_json_rel})"),
        markdown_metadata_row("Raw HTML snapshot", f"[{record.topic_html_path.name}]({raw_html_rel})"),
        "",
        "## Original Post",
        "",
    ]

    if posts:
        original_body = rewrite_html(
            fetcher,
            posts[0].get("cooked") or "",
            record,
            topic_destinations,
            asset_cache,
        )
        lines.append(post_markdown(posts[0], original_body, "Post 1"))
    else:
        lines.append("_No original post body was present in the topic JSON._")

    replies = posts[1:]
    lines.extend(["", "## Forum Discussion", ""])
    if replies:
        lines.append(
            "The following replies were migrated from the original forum topic in chronological order."
        )
        for post in replies:
            body = rewrite_html(
                fetcher,
                post.get("cooked") or "",
                record,
                topic_destinations,
                asset_cache,
            )
            lines.extend(
                [
                    "",
                    post_markdown(
                        post,
                        body,
                        f"Post {post.get('post_number')}",
                    ),
                ]
            )
    else:
        lines.append("_No replies were present in the migrated forum topic._")

    return "\n".join(lines)


def fetch_topic(fetcher: Fetcher, record: TopicRecord) -> dict:
    json_url = f"{FORUM_BASE}/t/{record.topic_id}.json"
    json_text = fetcher.get_text(json_url)
    write_text(record.topic_json_path, json_text)
    topic_data = parse_json(json_text, json_url)

    html_url = topic_source_url(record.slug, record.topic_id)
    try:
        html_text = fetcher.get_text(html_url)
        write_text(record.topic_html_path, html_text)
    except Exception as exc:
        record.notes.append(f"Raw HTML snapshot failed for `{html_url}`: {exc}")
        write_text(record.topic_html_path, "")

    return topic_data


def sort_key(record: TopicRecord) -> Tuple[int, int, str]:
    aip_match = AIP_RE.match(record.title)
    transparency_match = TRANSPARENCY_RE.match(record.title)
    if record.destination_dir == "AIPs":
        return (0, int(aip_match.group(1)) if aip_match else 999, record.title)
    if record.destination_dir == "transparency-reports":
        return (
            1,
            int(transparency_match.group(1)) if transparency_match else 999,
            record.title,
        )
    if record.destination_dir == "committees":
        return (2, record.topic_id, record.title)
    return (3, record.topic_id, record.title)


def markdown_link(from_file: Path, to_file: Path, label: str) -> str:
    return f"[{label}]({relpath(from_file, to_file)})"


def generate_readme(records: Iterable[TopicRecord]) -> str:
    records = sorted(records, key=sort_key)
    counts = {
        "AIPs": sum(1 for record in records if record.destination_dir == "AIPs"),
        "transparency-reports": sum(
            1 for record in records if record.destination_dir == "transparency-reports"
        ),
        "committees": sum(
            1 for record in records if record.destination_dir == "committees"
        ),
        ".": sum(1 for record in records if record.destination_dir == "."),
    }
    readme_path = GOVERNANCE_DIR / "README.md"

    lines = [
        "# Avail Governance",
        "",
        "This repository contains governance and reference material migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026.",
        "",
        "The forum URL retained in each file is a historical source identifier. The migrated content, source JSON, source HTML, and downloaded forum-hosted assets are preserved in this repository so the material remains available after the forum closes.",
        "",
        "This is not a full replacement for forum discussion. Ongoing community conversations continue outside this repository through Avail's community channels.",
        "",
        "## Contents",
        "",
        f"- AIPs: {counts['AIPs']} files",
        f"- Transparency reports: {counts['transparency-reports']} files",
        f"- Committee material: {counts['committees']} files",
        f"- General governance reference: {counts['.']} files",
        "- Source archive: `archive/`",
        "- Migration manifest: `MIGRATION_MANIFEST.md`",
        "- Source audit: `SOURCE_AUDIT.md`",
        "",
    ]

    for heading, destination in [
        ("AIPs", "AIPs"),
        ("Transparency Reports", "transparency-reports"),
        ("Committees", "committees"),
        ("General Governance Reference", "."),
    ]:
        subset = [record for record in records if record.destination_dir == destination]
        if not subset:
            continue
        lines.extend([f"## {heading}", "", "| Topic | File |", "| --- | --- |"])
        for record in subset:
            lines.append(
                f"| {record.title} | {markdown_link(readme_path, record.destination_path, record.destination_path.name)} |"
            )
        lines.append("")

    return "\n".join(lines)


def generate_manifest(records: Iterable[TopicRecord]) -> str:
    manifest_path = GOVERNANCE_DIR / "MIGRATION_MANIFEST.md"
    lines = [
        "# Avail Forum Governance Migration Manifest",
        "",
        f"Generated at: `{GENERATED_AT}`",
        "",
        "This manifest maps each migrated forum topic to its GitHub destination and archived source snapshots.",
        "",
        "| Topic ID | Title | Original Category | Destination | Posts | Assets | Raw JSON | Raw HTML | Notes |",
        "| --- | --- | --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for record in sorted(records, key=sort_key):
        category = CATEGORY_NAMES.get(record.category_id, f"Category {record.category_id}")
        destination = markdown_link(
            manifest_path,
            record.destination_path,
            record.destination_path.relative_to(ROOT).as_posix(),
        )
        raw_json = markdown_link(manifest_path, record.topic_json_path, record.topic_json_path.name)
        raw_html = markdown_link(manifest_path, record.topic_html_path, record.topic_html_path.name)
        notes = "<br>".join(record.notes) if record.notes else ""
        title = record.title.replace("|", "\\|")
        lines.append(
            f"| {record.topic_id} | {title} | {category} | {destination} | "
            f"{record.posts_included} | {len(record.assets)} | {raw_json} | {raw_html} | {notes} |"
        )

    return "\n".join(lines)


def numbers_for(records: Iterable[TopicRecord], pattern: re.Pattern) -> List[int]:
    numbers = []
    for record in records:
        match = pattern.match(record.title)
        if match:
            numbers.append(int(match.group(1)))
    return sorted(set(numbers))


def missing_numbers(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    return [number for number in range(min(numbers), max(numbers) + 1) if number not in numbers]


def generate_source_audit(records: Iterable[TopicRecord], audit_notes: List[str]) -> str:
    records = sorted(records, key=sort_key)
    aips = [record for record in records if record.destination_dir == "AIPs"]
    transparency = [
        record for record in records if record.destination_dir == "transparency-reports"
    ]
    committees = [record for record in records if record.destination_dir == "committees"]
    general = [record for record in records if record.destination_dir == "."]
    aip_numbers = numbers_for(aips, AIP_RE)
    transparency_numbers = numbers_for(transparency, TRANSPARENCY_RE)
    misplaced_transparency = [
        record
        for record in transparency
        if record.category_id != 34 and TRANSPARENCY_RE.match(record.title)
    ]
    asset_failures = [
        note
        for record in records
        for note in record.notes
        if note.startswith("Asset download failed")
    ]

    lines = [
        "# Avail Forum Governance Source Audit",
        "",
        f"Generated at: `{GENERATED_AT}`",
        "",
        "## Scope",
        "",
        "This migration includes visible governance and governance-reference topics discovered from the public Avail Forum Governance V1 category and its AIP, transparency report, and technical committee subcategories.",
        "",
        "It intentionally does not claim that the entire forum moved to GitHub. This repository preserves governance and reference material; future discussion happens through Avail's community channels.",
        "",
        "## Coverage Summary",
        "",
        f"- Total migrated topics: {len(records)}",
        f"- AIP topics/reference files: {len(aips)}",
        f"- Transparency report topics/reference files: {len(transparency)}",
        f"- Committee topics/reference files: {len(committees)}",
        f"- General governance reference files: {len(general)}",
        f"- Total posts included: {sum(record.posts_included for record in records)}",
        f"- Downloaded forum-hosted assets: {sum(len(record.assets) for record in records)}",
        "",
        "## AIP Audit",
        "",
        f"- Discovered AIP numbers: {', '.join(str(number) for number in aip_numbers) or 'None'}",
        f"- Missing AIP numbers in discovered range: {', '.join(str(number) for number in missing_numbers(aip_numbers)) or 'None'}",
        "",
        "## Transparency Report Audit",
        "",
        f"- Discovered transparency report numbers: {', '.join(str(number) for number in transparency_numbers) or 'None'}",
        f"- Missing transparency report numbers in discovered range: {', '.join(str(number) for number in missing_numbers(transparency_numbers)) or 'None'}",
    ]

    if misplaced_transparency:
        lines.append(
            "- Category anomaly: "
            + "; ".join(
                f"`{record.title}` was in `{CATEGORY_NAMES.get(record.category_id, record.category_id)}`"
                for record in misplaced_transparency
            )
        )
    else:
        lines.append("- Category anomaly: None")

    lines.extend(["", "## Committee And Governance Reference Audit", ""])
    for record in committees + general:
        category = CATEGORY_NAMES.get(record.category_id, f"Category {record.category_id}")
        lines.append(f"- `{record.title}` from `{category}`")

    lines.extend(["", "## Source Preservation Notes", ""])
    lines.extend(
        [
            "- Each migrated topic has a readable Markdown file.",
            "- Each migrated topic has a raw Discourse JSON snapshot.",
            "- Each migrated topic has a raw forum HTML snapshot when the public page was reachable.",
            "- Forum-hosted upload assets referenced by migrated post bodies are downloaded into `archive/assets/` and rewritten to local relative links.",
            "- Historical forum URLs remain as source identifiers, but the migrated content does not depend on those URLs remaining online.",
        ]
    )

    if audit_notes:
        lines.extend(["", "## Inventory Method", ""])
        for note in audit_notes:
            lines.append(f"- {note}")

    if asset_failures:
        lines.extend(["", "## Warnings", ""])
        for note in asset_failures:
            lines.append(f"- {note}")
    else:
        lines.extend(["", "## Warnings", "", "- None"])

    return "\n".join(lines)


def validate_records(records: Iterable[TopicRecord]) -> List[str]:
    errors = []
    for record in records:
        for path in [record.destination_path, record.topic_json_path, record.topic_html_path]:
            if not path.exists():
                errors.append(f"Missing expected file: {path.relative_to(ROOT)}")
        if record.posts_included <= 0:
            errors.append(f"Topic {record.topic_id} has no included posts.")
    return errors


def run(delay_seconds: float) -> int:
    ensure_dirs()
    fetcher = Fetcher(delay_seconds=delay_seconds)
    topic_summaries, audit_notes = collect_topic_summaries(fetcher)
    records = build_topic_records(topic_summaries)
    topic_destinations = {
        topic_id: record.destination_path for topic_id, record in records.items()
    }
    asset_cache: Dict[str, Path] = {}

    for record in sorted(records.values(), key=sort_key):
        topic_data = fetch_topic(fetcher, record)
        content = topic_markdown(
            topic_data,
            record,
            fetcher,
            topic_destinations,
            asset_cache,
        )
        write_text(record.destination_path, content)

    write_text(GOVERNANCE_DIR / "README.md", generate_readme(records.values()))
    write_text(
        GOVERNANCE_DIR / "MIGRATION_MANIFEST.md",
        generate_manifest(records.values()),
    )
    write_text(
        GOVERNANCE_DIR / "SOURCE_AUDIT.md",
        generate_source_audit(records.values(), audit_notes),
    )

    validation_errors = validate_records(records.values())
    if validation_errors:
        for error in validation_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Migrated {len(records)} topics into {GOVERNANCE_DIR.relative_to(ROOT)}")
    print(f"Included {sum(record.posts_included for record in records.values())} posts")
    print(f"Downloaded {sum(len(record.assets) for record in records.values())} assets")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Delay in seconds between forum requests.",
    )
    args = parser.parse_args()
    return run(delay_seconds=args.delay)


if __name__ == "__main__":
    raise SystemExit(main())
