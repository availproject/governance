# Transparency Report 18: Update SP1-SDK & Verification Key

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/transparency-report-18-update-sp1-sdk-verification-key/1681 |
| Forum topic ID | 1681 |
| Original category | Avail Transparency Report |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2025-06-17T13:00:08.911Z |
| Last posted | 2025-06-17T13:00:08.991Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1681.json](../archive/raw-json/topic-1681.json) |
| Raw HTML snapshot | [topic-1681.html](../archive/raw-html/topic-1681.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2025-06-17T13:00:08.991Z |
| Updated | 2025-06-17T13:00:08.991Z |
| Forum post number | 1 |
| Forum post ID | 2829 |
| Likes | 0 |

<div class="discourse-post-content">

<p><strong>Report Author:</strong> Toufeeq</p>
<p><strong>Execution Details:</strong> Changes have been applied at block <span class="hashtag-raw">#1</span>,443,438</p>
<p><strong>Technical Committee Consensus:</strong> 5/7 signers <a href="https://avail.subscan.io/tech/32?tab=proposal" class="inline-onebox">Subscan | Aggregate Substrate ecological network high-precision Web3 explorer</a></p>
<h3><a name="p-2829-introduction-1" class="anchor" href="#p-2829-introduction-1" aria-label="Heading link"></a><strong>Introduction</strong></h3>
<p>This document provides transparency on executed network changes. A vulnerability was identified in <strong>Plonky3</strong>, an external dependency of the sp1-sdk, which has since been addressed in sp1-sdk version <strong>5.0.0</strong>. You can learn more about the vulnerability <a href="https://github.com/Plonky3/Plonky3/security/advisories/GHSA-f69f-5fx9-w9r9">here</a>.</p>
<p>The Technical Committee (TC) has approved and executed the emergency proposal to perform a runtime upgrade of the network, along with updating the SP1 verification key. After assessing their <strong>effectiveness, impact, execution feasibility, and security implications</strong>, the TC reached a <strong>5/7 majority consensus</strong> to proceed with the upgrade.</p>
<h3><a name="p-2829-executed-changes-2" class="anchor" href="#p-2829-executed-changes-2" aria-label="Heading link"></a><strong>Executed Changes</strong></h3>
<p>The emergency proposal included two key changes:</p>
<ol>
<li>
<p>Runtime upgrade to use sp1-sdk v5.0.0 in pallet_vector (Bridge)</p>
</li>
<li>
<p>Update the SP1 verification key</p>
</li>
</ol>
<h3><a name="p-2829-code-modifications-3" class="anchor" href="#p-2829-code-modifications-3" aria-label="Heading link"></a><strong>Code Modifications</strong></h3>
<p>For those interested, you can review the necessary code modifications in the following PR:</p>
<ul>
<li><a href="https://github.com/availproject/avail/pull/752">PR</a></li>
</ul>
<p>If you need further details or have any concerns, please feel free to leave a comment.</p>
<p><strong>Thank you.</strong></p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
