# Transparency Report 16: Critical Runtime Upgrade - Filtering VectorX Bridge transactions

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/transparency-report-16-critical-runtime-upgrade-filtering-vectorx-bridge-transactions/1665 |
| Forum topic ID | 1665 |
| Original category | Avail Transparency Report |
| Original author | Jackson Lewis (@SocialForging) |
| Created | 2025-03-14T23:20:07.997Z |
| Last posted | 2025-03-14T23:20:08.063Z |
| Forum posts included | 2 |
| Highest forum post number | 5 |
| Raw JSON snapshot | [topic-1665.json](../archive/raw-json/topic-1665.json) |
| Raw HTML snapshot | [topic-1665.html](../archive/raw-html/topic-1665.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-03-14T23:20:08.063Z |
| Updated | 2025-03-15T00:03:35.547Z |
| Forum post number | 1 |
| Forum post ID | 2807 |
| Likes | 4 |

<div class="discourse-post-content">

<p><strong>Report Author</strong>: Jackson Lewis<br>
<strong>Execution Details</strong>: Changes were applied at <a href="https://explorer.avail.so/?rpc=wss%3A%2F%2Fmainnet-rpc.avail.so%2Fws#/explorer/query/0xbde7deaba118f868ef2e%5B%E2%80%A6%5D26b121f193e9eb2e4473d9709904cbdc608ef1">block #1,095,300</a><br>
<strong>Technical Committee Consensus</strong>: 5/5 signers <a href="https://avail.subscan.io/tech/29?tab=votes">https://avail.subscan.io/tech/29?tab=votes</a></p>
<p><strong>Introduction:</strong></p>
<p>This report provides transparency on executed network changes for the Avail Mainnet, focusing on the VectorX Bridge Proxy/Multisig Transaction Filters.</p>
<p><code>send_message</code> from Vector pallet, when called by a multisig or proxy, was not being included in the <code>bridgeRoot</code> , making it non-claimable on Ethereum. This resulted in loss of funds and impacted the Avail → Ethereum side of the bridge.</p>
<p>After identifying the issue, working on a the fix as efficiently as possible, the Technical Committee (TC) raised the proposal and a majority consensus (5/7) was reached.</p>
<p><strong>Executed Changes:</strong></p>
<p>Changes were made to the <code>send message</code> calls, especially from <code>multisig</code> and <code>proxy.</code><br>
These changes also included updates to prevent misuse of <code>send message</code>.</p>
<p><strong>Code Changes:</strong></p>
<p>Code Changes <a href="https://github.com/availproject/avail/compare/v2.2.5.3...v2.2.5.4">can be found here</a></p>
<p><strong>Merits to the Network:</strong></p>
<p>These above stated transactions are now performing as expected and are not being omitted / are being omitted where necessary.</p>
<p>A full report will be filed in the coming days and will be available <a href="https://github.com/availproject/security-advisories/tree/main">here</a></p>

</div>

## Forum Discussion

The following replies were migrated from the original forum topic in chronological order.

<a id="post-5"></a>

### Post 5

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-03-14T23:35:51.819Z |
| Updated | 2025-03-14T23:35:51.819Z |
| Forum post number | 5 |
| Forum post ID | 2811 |
| Likes | 0 |

<div class="discourse-post-content">



</div>
