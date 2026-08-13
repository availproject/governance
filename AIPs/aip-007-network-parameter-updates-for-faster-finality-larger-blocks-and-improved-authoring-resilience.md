# AIP 7: Network Parameter Updates for Faster Finality, Larger Blocks, and Improved Authoring Resilience

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-7-network-parameter-updates-for-faster-finality-larger-blocks-and-improved-authoring-resilience/1734 |
| Forum topic ID | 1734 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2025-10-09T10:44:38.736Z |
| Last posted | 2025-10-09T10:44:38.793Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1734.json](../archive/raw-json/topic-1734.json) |
| Raw HTML snapshot | [topic-1734.html](../archive/raw-html/topic-1734.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2025-10-09T10:44:38.793Z |
| Updated | 2025-10-09T10:44:38.793Z |
| Forum post number | 1 |
| Forum post ID | 2889 |
| Likes | 3 |

<div class="discourse-post-content">

<p><strong>Author:</strong> Toufeeq</p>
<p><strong>Technical Summary</strong></p>
<p>This AIP proposes a set of network parameters and node configuration updates that have already been deployed and validated on the <strong>Turing testnet</strong>. These updates aim to improve block finality times, increase block capacity at the node level, and enhance network resilience during temporary finality stalls. The key changes are:</p>
<ul>
<li>
<p><strong>Decrease finality gap</strong> from 2 blocks to <strong>1 block</strong> from the best block, enabling blocks to finalise in ~20 seconds (down from ~40 seconds).</p>
</li>
<li>
<p><strong>Increase supported block size</strong> in the node binary up to <strong>64 MiB</strong>, allowing for significantly higher data throughput and scalability.</p>
</li>
<li>
<p><strong>Update block authoring backoff strategy</strong> to limit the maximum delay to <strong>5 minutes</strong> during finality stalls, preventing extended authoring inactivity.</p>
</li>
<li>
<p><strong>Increase the number of primary slots</strong> to a probability of <strong>1/3</strong> (from 1/4), improving slot utilisation and reducing missed block production when some validators are offline.</p>
</li>
</ul>
<h2><a name="p-2889-motivation-1" class="anchor" href="#p-2889-motivation-1" aria-label="Heading link"></a><strong>Motivation</strong></h2>
<p>These proposed updates are part of the ongoing optimisation of Avail’s consensus and data-availability layers to support larger workloads, faster confirmations, and smoother authoring behaviour under varied network conditions.</p>
<ol>
<li>
<p><strong>Faster Finality:</strong></p>
<p>Reducing the finality gap from 2 → 1 block allows GRANDPA to finalise blocks roughly twice as fast, cutting the perceived finality latency from ~40 seconds to ~20 seconds.</p>
</li>
<li>
<p><strong>Higher Block Capacity:</strong></p>
<p>Increasing block size support to 64 MiB prepares Avail for future data-heavy use cases and scaling tests.</p>
</li>
<li>
<p><strong>Authoring Stability During Finality Stalls:</strong></p>
<p>The revised backoff mechanism (capped at 5 minutes) ensures nodes resume block production promptly even when finality temporarily stalls, improving overall network liveness.</p>
</li>
<li>
<p><strong>Improved Slot Coverage:</strong></p>
<p>Adjusting the probability of primary slots from 1/4 to 1/3 reduces the likelihood of missed slots when a subset of validators is down, improving block production consistency.</p>
</li>
</ol>
<h2><a name="p-2889-rationale-and-reasoning-2" class="anchor" href="#p-2889-rationale-and-reasoning-2" aria-label="Heading link"></a><strong>Rationale and Reasoning</strong></h2>
<p>All proposed changes have been successfully tested and validated on the <strong>Turing testnet</strong> under realistic network conditions. The results demonstrated:</p>
<ul>
<li>
<p><strong>No degradation in block propagation or finality metrics</strong> at higher block sizes.</p>
</li>
<li>
<p><strong>Stable validator performance</strong> and resource usage during increased load.</p>
</li>
<li>
<p><strong>Significant improvement in block finalisation speed</strong>, now consistently around 20 seconds.</p>
</li>
<li>
<p><strong>Reduced missed-slot occurrences</strong> under partial validator downtime scenarios.</p>
</li>
</ul>
<p>These adjustments ensure that Avail remains performant, responsive, and ready for scaling use cases that demand higher throughput and reduced confirmation latency.</p>
<h2><a name="p-2889-security-considerations-or-risks-3" class="anchor" href="#p-2889-security-considerations-or-risks-3" aria-label="Heading link"></a><strong>Security Considerations or Risks</strong></h2>
<p>Testing on Turing confirms that these updates introduce <strong>no additional security or stability risks</strong>.</p>
<ul>
<li>
<p>The finality gap reduction maintains safety guarantees of GRANDPA while improving finality.</p>
</li>
<li>
<p>Larger block size support only expands node capacity limits and does not alter consensus rules.</p>
</li>
<li>
<p>The backoff cap ensures predictable authoring recovery</p>
</li>
<li>
<p>Adjusted slot probabilities retain fairness while improving overall slot utilisation.</p>
</li>
</ul>
<p>The first three changes can be enacted through a binary release, while the fourth requires a governance proposal to update the relevant runtime configuration parameters.</p>
<h2><a name="p-2889-copyright-waiver-4" class="anchor" href="#p-2889-copyright-waiver-4" aria-label="Heading link"></a><strong>Copyright Waiver</strong></h2>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
