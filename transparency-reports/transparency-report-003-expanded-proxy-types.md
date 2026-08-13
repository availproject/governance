# Avail Transparency Report 3: Expanded Proxy Types

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/avail-transparency-report-3-expanded-proxy-types/1519 |
| Forum topic ID | 1519 |
| Original category | Avail Transparency Report |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2024-09-02T07:00:53.748Z |
| Last posted | 2024-09-02T07:00:53.855Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1519.json](../archive/raw-json/topic-1519.json) |
| Raw HTML snapshot | [topic-1519.html](../archive/raw-html/topic-1519.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2024-09-02T07:00:53.855Z |
| Updated | 2024-09-02T07:00:53.855Z |
| Forum post number | 1 |
| Forum post ID | 2578 |
| Likes | 1 |

<div class="discourse-post-content">

<p><img src="../archive/assets/1498/a8bcf6a2b80e-paperclip.png" title=":paperclip:" class="emoji" alt=":paperclip:" loading="lazy" width="20" height="20"> <strong>Report Author:</strong> Toufeeq from the Avail Technical Committee [5CoVaWrZnaV3BSeUJCA8Ca3SPMJDtjT1zPvZkzovkxJU7dkr]<br>
<strong>Changes to be Executed:</strong> Changes will be applied at block <span class="hashtag-raw">#271</span>,803<br>
<strong>Technical Committee Consensus:</strong> 5/7 signers <a href="https://avail.subscan.io/tech/12?tab=proposal">https://avail.subscan.io/tech/12?tab=proposal</a></p>
<p><strong>Introduction:</strong> This document aims to provide transparency to the Avail community concerning both upcoming and executed network changes. The Technical Committee (TC) has thoroughly assessed the proposal to add additional proxy types to the Avail mainnet. After careful consideration of their effectiveness, potential impact, execution parameters, and security implications, the TC has reached a majority consensus of 5/7.</p>
<p><strong>Proposed / Executed Changes:</strong> Here’s a summary of the proposed changes:</p>
<ul>
<li>Introduce an <code>IdentityJudgement</code> proxy type, enabling identity registrars to delegate judgments to other accounts.</li>
<li>Introduce a <code>NominationPool</code> proxy type, allowing nomination pool users to delegate pool-related operations.</li>
<li>Expand the <code>Staking</code> proxy type to include support for nomination pool operations.</li>
</ul>
<p><strong>Code Modifications:</strong> For those interested, you can review this <a href="https://github.com/availproject/avail/releases/tag/v2.2.5.0">release notes</a> &amp; here are some notable PR’s: Runtime Changes:</p>
<ul>
<li><a href="https://github.com/availproject/avail/pull/624">Added IdentityJudgement proxy type</a></li>
<li><a href="https://github.com/availproject/avail/pull/638">Added NominationPool proxy type &amp; updated Staking proxy type to allow pool transactions</a></li>
</ul>
<p><strong>Potential Merits to the Network:</strong> The proposed changes significantly benefit the network by enhancing flexibility and user experience. Introducing the <code>IdentityJudgement</code> proxy type enables identity registrars to delegate verification tasks, streamlining identity management and potentially increasing the number of verified users. The <code>NominationPool</code> proxy type simplifies the management of nomination pools, encouraging broader participation in staking activities by reducing operational burdens on users. Additionally, expanding the <code>Staking</code> proxy type to include nomination pool operations unifies and simplifies the staking process, fostering greater engagement in network governance.</p>
<p>If you need any additional resources or information, please feel free to leave a comment.</p>
<p>Thank you.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
