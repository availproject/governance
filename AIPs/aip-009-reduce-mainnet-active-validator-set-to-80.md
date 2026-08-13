# AIP 9: Reduce Mainnet Active Validator Set to 80

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-9-reduce-mainnet-active-validator-set-to-80/1775 |
| Forum topic ID | 1775 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Rishi | Avail (@rishitriparthi) |
| Created | 2026-05-25T11:18:43.664Z |
| Last posted | 2026-05-25T11:18:43.732Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1775.json](../archive/raw-json/topic-1775.json) |
| Raw HTML snapshot | [topic-1775.html](../archive/raw-html/topic-1775.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Rishi | Avail (@rishitriparthi) |
| Posted | 2026-05-25T11:18:43.732Z |
| Updated | 2026-05-25T11:19:09.166Z |
| Forum post number | 1 |
| Forum post ID | 2938 |
| Likes | 5 |

<div class="discourse-post-content">

<p><strong>Author:</strong> Rishi</p>
<p><strong>Description</strong>: Proposal to reduce the active validator set from ~105 to 80 to strengthen validator incentives and broaden community participation in staking.</p>
<h2><a name="p-2938-proposed-summary-1" class="anchor" href="#p-2938-proposed-summary-1" aria-label="Heading link"></a>Proposed Summary</h2>
<p>This proposal reduces the active validator set from its current size (~105) to 80. The change is applied to the <code>validatorCount</code> staking parameter. It is not a runtime upgrade and does not change consensus, slashing, or emissions.</p>
<h2><a name="p-2938-background-and-rationale-2" class="anchor" href="#p-2938-background-and-rationale-2" aria-label="Heading link"></a>Background and Rationale</h2>
<p>The active set was grown from an initial 40–50 to ~105 over the network’s first year to build out operational and geographic diversity. That goal has largely been met, and the network is now in a position to optimise the set for stronger incentives and broader participation.</p>
<p>A more focused set strengthens validator incentives and makes running a validator more attractive on its own merits. It also benefits nominators, and community members: stronger, more predictable yields are the most direct way to draw more staking and grow total staked supply, which in turn deepens the stake securing the network.</p>
<p>This is a recalibration to where the network is today, not a permanent cap. The set can be expanded again through the same process if demand or staked supply calls for it.</p>
<h2><a name="p-2938-security-considerations-or-risks-3" class="anchor" href="#p-2938-security-considerations-or-risks-3" aria-label="Heading link"></a>Security Considerations or Risks</h2>
<p>A set of 80 remains large and keeps ample redundancy for block production and proof serving. As the set adjusts, stake redistributes across the active validators, so the security of the network is maintained. Stake distribution will be monitored as a standard precaution.</p>
<h2><a name="p-2938-copyright-waiver-4" class="anchor" href="#p-2938-copyright-waiver-4" aria-label="Heading link"></a>Copyright Waiver</h2>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
