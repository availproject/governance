# AIP 5: Increase Ideal Staking Ratio to 75%

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-5-increase-ideal-staking-ratio-to-75/1632 |
| Forum topic ID | 1632 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Jackson Lewis (@SocialForging) |
| Created | 2025-01-14T13:39:39.053Z |
| Last posted | 2025-01-22T11:19:14.543Z |
| Forum posts included | 8 |
| Highest forum post number | 8 |
| Raw JSON snapshot | [topic-1632.json](../archive/raw-json/topic-1632.json) |
| Raw HTML snapshot | [topic-1632.html](../archive/raw-html/topic-1632.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-01-14T13:39:39.114Z |
| Updated | 2025-01-27T14:56:46.303Z |
| Forum post number | 1 |
| Forum post ID | 2760 |
| Likes | 12 |

<div class="discourse-post-content">

<p><strong>Authors</strong>: Jackson Lewis, Tanisha Katara</p>
<p><strong>Description</strong>: This AIP proposes increasing the ideal staking ratio from 50% to 75% to align with network scaling, ensure sustainable APY, and strengthen network security.</p>
<h3><a name="p-2760-technical-summary-1" class="anchor" href="#p-2760-technical-summary-1" aria-label="Heading link"></a><strong>Technical Summary</strong></h3>
<p>This AIP proposes raising the <strong>ideal_stake</strong> parameter in Avail’s inflation model from 50% to 75%. The <strong>ideal_stake</strong> defines the staking rate at which the network achieves an optimal balance between security and liquidity. Increasing this parameter ensures sustainable APY for nominators and validators, reflects the network’s maturity, and supports the scaling of staking participation through the Foundation Delegation Program.</p>
<p>This adjustment has been tested on Turing and will be implemented via a runtime upgrade.</p>
<h3><a name="p-2760-motivation-2" class="anchor" href="#p-2760-motivation-2" aria-label="Heading link"></a><strong>Motivation</strong></h3>
<p>At genesis, the <strong>ideal_stake</strong> parameter was set at 50% to encourage early staking participation by offering high APY to nominators and validators. Over time, the network has scaled significantly, with an increasing amount of tokens staked due to organic growth and the Foundation Delegation Program.</p>
<p>If the ideal staking ratio remains at 50%, the inflation model will lead to abrupt APY drops as staking rates exceed the ideal threshold, potentially discouraging participation. Increasing the <strong>ideal_stake</strong> to 75% aligns with the network’s growth and ensures the long-term sustainability of staking incentives.</p>
<h3><a name="p-2760-technical-specification-3" class="anchor" href="#p-2760-technical-specification-3" aria-label="Heading link"></a><strong>Technical Specification</strong></h3>
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
<p><strong>Below χ_ideal</strong>: Inflation increases linearly with x, incentivizing more staking.</p>
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
<li>Current χ_ideal = 0.50 (50%)</li>
<li>Proposed χ_ideal = 0.75 (75%)</li>
</ul>
</li>
<li>
<p><strong>Testing</strong>:</p>
<p>This change has been tested on Turing, validating its effectiveness and compatibility with network parameters.</p>
</li>
</ol>
<h3><a name="p-2760-rationale-and-reasoning-4" class="anchor" href="#p-2760-rationale-and-reasoning-4" aria-label="Heading link"></a><strong>Rationale and Reasoning</strong></h3>
<p>The decision to increase the ideal staking ratio (χ_ideal) to 75% is driven by the following considerations:</p>
<ol>
<li>
<p><strong>Network Scaling and Ecosystem Maturity</strong>:</p>
<p>The total stake has grown significantly due to organic participation and the Foundation Delegation Program. A higher χ_ideal aligns with this natural growth and avoids excessive APY dilution for stakers. A higher χ_ideal reflects the network’s evolution from incentivizing early participants to ensuring long-term stability for all stakeholders.</p>
</li>
<li>
<p><strong>Sustainable APY</strong>:</p>
<p>While increasing χ_ideal may result in a marginal decrease in individual APY, it ensures a smoother and more sustainable APY curve as the network matures. Without this adjustment, APY would drop abruptly when the staking rate exceeds the current ideal ratio (50%).</p>
</li>
</ol>
<h3><a name="p-2760-backwards-compatibility-5" class="anchor" href="#p-2760-backwards-compatibility-5" aria-label="Heading link"></a><strong>Backwards Compatibility</strong></h3>
<p>This proposal does not introduce any backwards incompatibilities. The change to the <strong>ideal_stake</strong> parameter is applied via a runtime upgrade and does not affect the consensus mechanism or validator operations. The network will continue to function as intended, with no disruptions for participants.</p>
<h3><a name="p-2760-security-considerations-or-risks-6" class="anchor" href="#p-2760-security-considerations-or-risks-6" aria-label="Heading link"></a><strong>Security Considerations or Risks</strong></h3>
<p>The runtime upgrade process ensures the change is applied uniformly across the network, introducing no security vulnerabilities. Testing on Turing has validated the safety and effectiveness of this adjustment. The increase in staking participation will further enhance network security.</p>
<h3><a name="p-2760-copyright-waiver-7" class="anchor" href="#p-2760-copyright-waiver-7" aria-label="Heading link"></a><strong>Copyright Waiver</strong></h3>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

The following replies were migrated from the original forum topic in chronological order.

<a id="post-2"></a>

### Post 2

| Field | Value |
| --- | --- |
| Author | Ryan Haczynski, Head of Protocol Partnerships, GlobalStake 🌎🥩 (@Phunky) |
| Posted | 2025-01-14T20:21:33.183Z |
| Updated | 2025-01-14T20:21:33.183Z |
| Forum post number | 2 |
| Forum post ID | 2761 |
| Likes | 2 |

<div class="discourse-post-content">

<p>Looks good to me, gang!</p>
<p>We’ve had similar issues over the years with the Polkadot network, and over time these sorts of adjustments are necessary to foster the best possible solution for all ecosystem participants, whether individual stakers such as myself or validator operators such as our company, GlobalStake.</p>
<p>Kudos to the team for their foresight in this matter. If you’d like me / us to create any content to share on social media to make others aware of this necessary and timely change, please do not hesitate to ask!</p>
<p>Best,</p>
<p>Ryan / Phunky</p>

</div>

<a id="post-3"></a>

### Post 3

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-01-14T20:37:06.226Z |
| Updated | 2025-01-14T20:37:06.226Z |
| Forum post number | 3 |
| Forum post ID | 2762 |
| Likes | 0 |

<div class="discourse-post-content">

<p>Thanks for the feedback Phunky!</p>
<p>Always welcome to put something on socials if you’d like, we’d love to amplify!</p>

</div>

<a id="post-4"></a>

### Post 4

| Field | Value |
| --- | --- |
| Author | Aleksandr Tishin (@Aleksandr_Tishin) |
| Posted | 2025-01-15T12:56:27.707Z |
| Updated | 2025-01-15T12:56:27.707Z |
| Forum post number | 4 |
| Forum post ID | 2765 |
| Likes | 0 |

<div class="discourse-post-content">

<p>Hey, I have several questions:</p>
<ol>
<li>
<p>What are the specific reasons to believe that the staking ratio will increase from 15% to over 50%, as reported by Subscan? What key factors or mechanisms are expected to drive this 3x growth in staking participation?</p>
</li>
<li>
<p>A similar proposal was implemented on Polkadot last year, but in that case, the staking ratio was several pp close to the ideal ratio. However, after it led to a shift toward a fixed inflation model, entirely abandoning the complex non-linear dependency between staking ratio, APR, and treasury inflows. Has the Avail team explored adopting a similar fixed inflation approach? What are the pros and cons of such a model in Avail’s context?</p>
</li>
<li>
<p>Why is Avail’s proposal still being approached in a centralized manner rather than leveraging on-chain governance (giving substrate framework and governance palette) and trackable voting, which are now standard practices in many protocols? What are the challenges preventing the implementation of decentralized governance mechanisms?</p>
</li>
</ol>

</div>

<a id="post-5"></a>

### Post 5

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-01-16T18:48:59.879Z |
| Updated | 2025-01-16T18:48:59.879Z |
| Forum post number | 5 |
| Forum post ID | 2767 |
| Likes | 4 |

<div class="discourse-post-content">

<p>Thanks for your comments Aleks!</p>
<ol>
<li>
<p>We have had many applications to the Foundation Nomination Program, we are now bumping additions to the nomination program at 10 per time (roughly ten per week) so there will be sufficient stake entering network.</p>
</li>
<li>
<p>Avail has fixed inflation of 5%.<br>
<a href="https://docs.availproject.org/user-guides/staking-governance/overview" class="inline-onebox">AVAIL - Avail Developer Docs</a><br>
I am not familair with these changes in polkadot, would need references to comment further.</p>
</li>
<li>
<p>We have phased decentralised governance clearly <a href="https://docs.availproject.org/user-guides/staking-governance/governance-on-avail/overview">outlined here</a>.<br>
Progressive decentralization is the norm, as we are only a matter of months out from mainnet launch, its a gradual process.  The community / network is not yet at a stage where we can actively decentralize all operations.<br>
We are of course committed to decentralization and will continue to work towards it as the network matures.</p>
</li>
</ol>

</div>

<a id="post-6"></a>

### Post 6

| Field | Value |
| --- | --- |
| Author | Brightly Stake (@Brightly_Stake) |
| Posted | 2025-01-17T16:57:51.780Z |
| Updated | 2025-01-17T16:57:51.780Z |
| Forum post number | 6 |
| Forum post ID | 2769 |
| Likes | 1 |

<div class="discourse-post-content">

<p>in support of this proposal, with more validators joining active set this can be crucial for avail’s success.</p>

</div>

<a id="post-7"></a>

### Post 7

| Field | Value |
| --- | --- |
| Author | Igor (@IgorK) |
| Posted | 2025-01-22T09:28:17.628Z |
| Updated | 2025-01-22T09:28:17.628Z |
| Forum post number | 7 |
| Forum post ID | 2775 |
| Likes | 1 |

<div class="discourse-post-content">

<p>Sounds like a solid move to raise the ideal_stake to 75%. It helps boost network security, keeps APY stable, and matches the ecosystem’s growth. The runtime upgrade approach also seems straightforward and safe.</p>

</div>

<a id="post-8"></a>

### Post 8

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2025-01-22T11:19:14.543Z |
| Updated | 2025-01-22T11:19:14.543Z |
| Forum post number | 8 |
| Forum post ID | 2777 |
| Likes | 3 |

<div class="discourse-post-content">

<p>This change has been implemented</p>
<aside class="quote quote-modified" data-post="1" data-topic="1640">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/forum.availproject.org/toufeeq_pasha/48/858_2.png" class="avatar">
    <a href="../transparency-reports/transparency-report-012-increased-ideal-stake-to-75.md">Transparency Report 12: Increased ideal_stake to 75%</a> <a class="badge-category__wrapper " href="https://forum.availproject.org/c/governance/avail-transparency-report/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #0088CC;" data-parent-category-id="32" data-drop-close="true" class="badge-category --has-parent" title="Avail Transparency Reports (ATR) are simple summaries of upcoming or executed changes made to the Avail Network.
Go to the docs to learn more about Avail Transparency Reports (ATR)."><span class="badge-category__name">Avail Transparency Report</span></span></a>
  </div>
  <blockquote>
    Report Author: Toufeeq from the Avail Technical Committee [5CoVaWrZnaV3BSeUJCA8Ca3SPMJDtjT1zPvZkzovkxJU7dkr] 
Change Executed: Changes will be applied at block #877,679 
Technical Committee Consensus: 5/7 signers <a href="https://avail.subscan.io/tech/25?tab=votes">https://avail.subscan.io/tech/25?tab=votes</a> 
Introduction: 
This report aims to provide transparency to the Avail community regarding both upcoming and executed network changes. The Avail Technical Committee (TC) has approved a runtime upgrade on Avail Mainnet to increase the ideal_stake …
  </blockquote>
</aside>

</div>
