# AIP 3: Decrease fees to testnet levels

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-3-decrease-fees-to-testnet-levels/1526 |
| Forum topic ID | 1526 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Dan (@dan) |
| Created | 2024-09-18T20:28:09.506Z |
| Last posted | 2024-10-01T11:16:50.355Z |
| Forum posts included | 4 |
| Highest forum post number | 4 |
| Raw JSON snapshot | [topic-1526.json](../archive/raw-json/topic-1526.json) |
| Raw HTML snapshot | [topic-1526.html](../archive/raw-html/topic-1526.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Dan (@dan) |
| Posted | 2024-09-18T20:28:09.640Z |
| Updated | 2024-09-19T05:39:52.526Z |
| Forum post number | 1 |
| Forum post ID | 2593 |
| Likes | 5 |

<div class="discourse-post-content">

<p><strong>Title:</strong> AIP 3: Decrease fees to testnet levels<br>
<strong>Description:</strong> Recommendation by the Fee Pricing Committee to substantially decrease fees to match those in the Turing testnet<br>
<strong>Author:</strong> Dan Mills</p>
<h2><a name="p-2593-proposed-fee-summary-1" class="anchor" href="#p-2593-proposed-fee-summary-1" aria-label="Heading link"></a>Proposed Fee Summary</h2>
<p>The Fee Pricing Committee (FPC) is responsible for establishing and recommending data submission fees within the network (<a href="https://forum.availproject.org/t/avail-fee-pricing-committee-charter-composition-and-values/">see charter here</a>). In this recommendation, the FPC proposes reducing fees on Avail DA mainnet by 10x. Currently, sending 512 KB of data costs 9.49 AVAIL, enacting this change would make that 0.95 AVAIL (~1/10 as much), which matches what it would cost on the Turing testnet.</p>
<h2><a name="p-2593-background-and-rationale-2" class="anchor" href="#p-2593-background-and-rationale-2" aria-label="Heading link"></a>Background and Rationale</h2>
<p>Although extensive testing was performed on the Turing testnet with fees set to their current values (10x lower than mainnet), mainnet was launched with higher fees in order to reduce likelihood of spam in the initial days and weeks after the launch.</p>
<p>The committee believes that now that the network has launched and its robustness demonstrated, the risk of spam by lowering fees back to the levels of the testnet is minimal.</p>
<p>Moreover, this recommendation gets closer (though slightly higher) to USD $0.2 per MB, which the committee believes is a reasonable target. The FPC believes this target represents a reasonable balance between the need to deter spam and congestion, reward validators, and to offer a competitive and affordable service to the community.</p>
<h2><a name="p-2593-analysis-and-impact-3" class="anchor" href="#p-2593-analysis-and-impact-3" aria-label="Heading link"></a>Analysis and Impact</h2>
<p>The recommended fee equates to about 1.901 AVAIL per MB (1024 KB), or about USD $0.26 at the current AVAIL token price (as of writing).</p>
<p>As noted above, this is somewhat closer, though still somewhat higher than the committee’s rough target of $0.2 per MB. The FPC believes that given the dynamic nature of the token price and the recency of the mainnet launch, this initial adjustment is a reasonable first approximation to the target, which can be refined in future recommendations. The FPC will seek to develop more sophisticated tools to that effect.</p>
<p>Note that the token price in USD does not remain static, causing the price per MB in USD to similarly fluctuate. Do not rely on the USD price given above or the target in this recommendation without checking the current cost. Given this volatility, the target is thus only a rough guideline which the committee uses to evaluate along with other considerations.</p>
<h2><a name="p-2593-security-considerations-or-risks-4" class="anchor" href="#p-2593-security-considerations-or-risks-4" aria-label="Heading link"></a>Security Considerations or Risks</h2>
<p>The primary security consideration of lowering the data posting fees is the risk for additional spam. Based on testing on the Turing testnet as well as by observing fees on other data availability services, the committee believes that the risk of spam is minimal at the recommended fee levels.</p>
<h2><a name="p-2593-copyright-waiver-5" class="anchor" href="#p-2593-copyright-waiver-5" aria-label="Heading link"></a>Copyright Waiver</h2>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

The following replies were migrated from the original forum topic in chronological order.

<a id="post-2"></a>

### Post 2

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-09-18T21:10:09.439Z |
| Updated | 2024-09-18T21:10:09.439Z |
| Forum post number | 2 |
| Forum post ID | 2594 |
| Likes | 0 |

<div class="discourse-post-content">

<p>Great work Dan. In full support of this change</p>

</div>

<a id="post-3"></a>

### Post 3

| Field | Value |
| --- | --- |
| Author | Kyle Rojas (@kyleArojas) |
| Posted | 2024-09-18T22:23:24.557Z |
| Updated | 2024-09-18T22:23:24.557Z |
| Forum post number | 3 |
| Forum post ID | 2595 |
| Likes | 0 |

<div class="discourse-post-content">

<p>Perfect. Thanks for the update, Dan.</p>

</div>

<a id="post-4"></a>

### Post 4

| Field | Value |
| --- | --- |
| Author | Henri | Stakin (@Henri) |
| Posted | 2024-10-01T11:16:50.355Z |
| Updated | 2024-10-01T11:16:50.355Z |
| Forum post number | 4 |
| Forum post ID | 2642 |
| Likes | 0 |

<div class="discourse-post-content">

<p>Stakin supports this proposal. It is a smart move to make the network more accessible while still keeping it secure. Hopefully, this will help drive growth and network activity.</p>
<p>Henri from Stakin</p>

</div>
