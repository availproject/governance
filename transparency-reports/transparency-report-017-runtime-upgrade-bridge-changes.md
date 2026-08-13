# Transparency report 17: Runtime Upgrade - Bridge changes

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/transparency-report-17-runtime-upgrade-bridge-changes/1680 |
| Forum topic ID | 1680 |
| Original category | Governance V1 |
| Original author | Marko Petrlić (@Marko_Petrlic) |
| Created | 2025-04-25T12:31:24.470Z |
| Last posted | 2025-04-25T12:31:24.544Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1680.json](../archive/raw-json/topic-1680.json) |
| Raw HTML snapshot | [topic-1680.html](../archive/raw-html/topic-1680.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Marko Petrlić (@Marko_Petrlic) |
| Posted | 2025-04-25T12:31:24.544Z |
| Updated | 2025-04-25T12:31:57.938Z |
| Forum post number | 1 |
| Forum post ID | 2827 |
| Likes | 2 |

<div class="discourse-post-content">

<p><strong>Report Author</strong>: Marko from the Avail Technical Committee<br>
<strong>Execution Block</strong>: <a href="https://avail.subscan.io/block/1274598" class="inline-onebox">Subscan | Avail Block Details</a><br>
<strong>Technical  Committee Proposal Block</strong>: <a href="https://avail.subscan.io/block/1261637">https://avail.subscan.io/block/1261637</a><br>
<strong>Technical Committee Consenus</strong>: 5/5 singer <a href="https://avail.subscan.io/tech/30?tab=votes" class="inline-onebox">Subscan | Aggregate Substrate ecological network high-precision Web3 explorer</a></p>
<p><strong>Introduction</strong>:<br>
This report provides transparency regarding the network changes executed on the Avail Mainnet, focusing on the Vector bridge updates.</p>
<p>The existing Vector bridge was not compatible with the upcoming Ethereum Pectra upgrade, so changes were necessary to ensure its functionality.</p>
<p><strong>Executed Changes</strong>:<br>
Instead of using TelepathyX in our bridge process, we switched to SP1 Helios and added new extrinsics to the vector pallet to ensure that the Ethereum → Avail bridge continues to function after the Pectra upgrade is completed.</p>
<p><strong>Code Modification</strong>:<br>
PR: <a href="https://github.com/availproject/avail/pull/689" class="inline-onebox">Helios sp1 integration by 0xSasaPrsic · Pull Request #689 · availproject/avail · GitHub</a><br>
PR: <a href="https://github.com/availproject/avail/pull/713" class="inline-onebox">Add support for sp1 v4.0.0 by 0xSasaPrsic · Pull Request #713 · availproject/avail · GitHub</a></p>
<p><strong>Merits to the Network</strong>:<br>
The upgrade ensures seamless operation of the Vector bridge with the upcoming Ethereum Pectra upgrade.</p>
<p>Thank you</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
