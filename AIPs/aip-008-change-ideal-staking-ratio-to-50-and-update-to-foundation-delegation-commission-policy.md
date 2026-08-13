# AIP 8: Change Ideal Staking Ratio to 50% and Update to Foundation Delegation Commission Policy

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-8-change-ideal-staking-ratio-to-50-and-update-to-foundation-delegation-commission-policy/1742 |
| Forum topic ID | 1742 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2025-12-15T07:35:09.603Z |
| Last posted | 2025-12-15T07:35:09.656Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1742.json](../archive/raw-json/topic-1742.json) |
| Raw HTML snapshot | [topic-1742.html](../archive/raw-html/topic-1742.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2025-12-15T07:35:09.656Z |
| Updated | 2025-12-23T06:38:18.881Z |
| Forum post number | 1 |
| Forum post ID | 2897 |
| Likes | 3 |

<div class="discourse-post-content">

<p><strong>Author</strong>: Toufeeq Pasha</p>
<p><strong>Description</strong>: This AIP proposes reducing the ideal staking ratio from 75% to 50% and updating the Foundation Delegation Program’s validator commission policy by increasing the acceptable commission threshold from 15% to 20%. This change supports validator operator sustainability and ensures a well-incentivised validator set as the network continues to grow.</p>
<h3><a name="p-2897-technical-summary-1" class="anchor" href="#p-2897-technical-summary-1" aria-label="Heading link"></a><strong>Technical Summary</strong></h3>
<p>This proposal introduces two coordinated updates:</p>
<ol>
<li>
<p>Reduce the ideal_stake parameter from 75% to 50%. This parameter affects inflation and reward dynamics by defining the staking participation level at which staking rewards are optimised.</p>
</li>
<li>
<p>Increase the Foundation Delegation Program’s acceptable validator commission from 15% to 20%. This is not a protocol or runtime parameter change; validators have always been free to set commission up to 100%. The change updates the Foundation’s delegation policy; validators charging up to 20% commission will remain eligible for Foundation nominations.</p>
</li>
</ol>
<p>Both updates have been evaluated on Turing and will be applied through a runtime upgrade (for the ideal_stake change) and a policy update (for the delegation threshold).</p>
<h3><a name="p-2897-motivation-2" class="anchor" href="#p-2897-motivation-2" aria-label="Heading link"></a><strong>Motivation</strong></h3>
<ol>
<li><strong>Supporting Validator Operator Sustainability</strong></li>
</ol>
<p>Validator operators perform the critical work of block production, proof serving, and infrastructure management. And their sustainability is essential to network security and reliability.</p>
<p>Increasing the Foundation Delegation Program’s acceptable commission threshold from 15% to 20% provides operators with more economic flexibility, especially for those who rely heavily on delegation to maintain competitive performance.</p>
<p>This is a targeted adjustment to address the present operational realities of running a validator and is not indicative of continued increases in the future.</p>
<ol>
<li><strong>Smoother and More Sustainable Reward Dynamics</strong></li>
</ol>
<p>With the current ideal staking ratio set at 75%, reward emissions tighten sharply when staking participation is below that threshold. Moving the ideal_stake to 50% broadens the optimal reward zone and better supports long-term stability of validator and nominator incentives.</p>
<p>This update improves the robustness of the staking economy without disrupting existing network behaviour.</p>
<h3><a name="p-2897-technical-specification-3" class="anchor" href="#p-2897-technical-specification-3" aria-label="Heading link"></a><strong>Technical Specification</strong></h3>
<p>The <strong>ideal_stake</strong> parameter directly influences Avail’s inflation dynamics and staking incentives:</p>
<ol>
<li>
<p><strong>Staking Rate (x)</strong>:</p>
<p>(StakedSupply) / (TotalSupply)</p>
<p>The staking rate determines the inflation rate (I_NPoS) and the yearly interest rate (i(x)).</p>
</li>
<li>
<p><strong>Inflation Dynamics</strong>:</p>
<ul>
<li>
<p><strong>Below χ_ideal</strong>: Inflation increases linearly with x, incentivising more staking.</p>
</li>
<li>
<p><strong>At χ_ideal</strong>: Inflation achieves its maximum value:</p>
<p>INPoS=χideal∗iidealI_NPoS = χ_ideal * i_idealINPoS=χideal∗iideal</p>
</li>
<li>
<p><strong>Above χ_ideal</strong>: Inflation decreases exponentially to discourage over-staking.</p>
</li>
</ul>
</li>
<li>
<p><strong>Proposed Update</strong>:</p>
<ul>
<li>
<p>Current χ_ideal: 0.75 (75%)</p>
</li>
<li>
<p>Proposed χ_ideal: 0.50 (50%)</p>
</li>
<li>
<p>Current acceptable validator commission by Foundation Delegation Program: 15%</p>
</li>
<li>
<p>Proposed acceptable validator commission by Foundation Delegation Program: 20%</p>
</li>
</ul>
<p><em>Note: Validator commission remains configurable up to 100% at the protocol level. This AIP only updates the delegation eligibility threshold for Foundation nominations.</em></p>
</li>
<li>
<p><strong>Testing</strong>:</p>
<p>This change has been tested on Turing, validating its effectiveness and compatibility with network parameters.</p>
</li>
</ol>
<h3><a name="p-2897-rationale-and-reasoning-4" class="anchor" href="#p-2897-rationale-and-reasoning-4" aria-label="Heading link"></a><strong>Rationale and Reasoning</strong></h3>
<ol>
<li><strong>Ensuring Validator Sustainability Without Protocol Changes</strong></li>
</ol>
<p>The validator commission ceiling is intentionally unbounded by the protocol to allow market-based differentiation. This AIP simply signals that the Foundation Delegation Program will continue supporting validators who set commission up to 20%, aligning incentives without impacting runtime logic.</p>
<ol>
<li><strong>Strengthening Reward Stability</strong></li>
</ol>
<p>Lowering the ideal staking ratio:</p>
<ul>
<li>
<p>reduces reward volatility</p>
</li>
<li>
<p>better aligns incentives across varying staking levels</p>
</li>
<li>
<p>supports a more stable validator set.</p>
</li>
</ul>
<p>These changes target current network needs and are not intended to establish a pattern of recurring adjustments.</p>
<h3><a name="p-2897-backwards-compatibility-5" class="anchor" href="#p-2897-backwards-compatibility-5" aria-label="Heading link"></a><strong>Backwards Compatibility</strong></h3>
<p>This proposal does not introduce any backwards incompatibilities. The change to the <strong>ideal_stake</strong> parameter is applied via a runtime upgrade and does not affect the consensus mechanism or validator operations. The network will continue to function as intended, with no disruptions for participants.</p>
<h3><a name="p-2897-security-considerations-or-risks-6" class="anchor" href="#p-2897-security-considerations-or-risks-6" aria-label="Heading link"></a><strong>Security Considerations or Risks</strong></h3>
<p>The runtime upgrade process ensures the change is applied uniformly across the network, introducing no security vulnerabilities. Testing on Turing has validated the safety and effectiveness of this adjustment. The increase in staking participation will further enhance network security.</p>
<h3><a name="p-2897-copyright-waiver-7" class="anchor" href="#p-2897-copyright-waiver-7" aria-label="Heading link"></a><strong>Copyright Waiver</strong></h3>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
