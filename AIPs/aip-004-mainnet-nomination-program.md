# AIP 4: Mainnet Nomination Program

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-4-mainnet-nomination-program/1571 |
| Forum topic ID | 1571 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Jackson Lewis (@SocialForging) |
| Created | 2024-10-23T13:39:47.990Z |
| Last posted | 2024-10-28T11:37:33.910Z |
| Forum posts included | 8 |
| Highest forum post number | 8 |
| Raw JSON snapshot | [topic-1571.json](../archive/raw-json/topic-1571.json) |
| Raw HTML snapshot | [topic-1571.html](../archive/raw-html/topic-1571.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-10-23T13:39:48.079Z |
| Updated | 2024-12-11T14:28:39.597Z |
| Forum post number | 1 |
| Forum post ID | 2670 |
| Likes | 12 |

<div class="discourse-post-content">

<p>Author: Jackson Lewis</p>
<p><strong>Technical Summary</strong>:<br>
This AIP proposes the introduction of the Mainnet Nomination Program.<br>
This program  focuses on using Avail Foundation funds to nominate to community validators, supporting their election into the active set. This helps increase decentralization within the validator group / network due to the nomination program selection criteria.</p>
<p><strong>Motivation:</strong><br>
The intention of this program is to support the growth of the network whilst also support the participants who are contributing to the ecosystem.<br>
The nomination program includes an application process, which builds a pipeline of potential candidates.</p>
<p>The minimum requirement for eligibility are as follows:</p>
<ol>
<li>
<p>Validators must set a verified on-chain identity.</p>
</li>
<li>
<p>When operating an active set node, the entity must not have been slashed.</p>
</li>
<li>
<p>Critical/high-priority upgrades must be applied within 12 hours, and medium/low-priority within 24 hours of alert/prompt by Validator Engagement Team.</p>
</li>
<li>
<p>Validators must connect to a dedicated telemetry system for monitoring.</p>
</li>
<li>
<p>Only one node per entity/application.</p>
</li>
<li>
<p>Node operators must manage their own nodes, or work with a verifiably strong third party node operations team, however, self managed is preferred.</p>
</li>
<li>
<p>Must have a Mainnet node bonded and in wait-list.</p>
</li>
<li>
<p>Validator commission must be 10% or less.</p>
</li>
<li>
<p>Must not operate from the US, sanctioned countries, or prohibited jurisdictions and pass compliance screening.</p>
</li>
<li>
<p>Applicant or representative of the entity must complete a simply KYC through Sumsub.</p>
</li>
</ol>
<p><strong>Following these minimum requirements, further considerations are conducted on the following:</strong></p>
<ol>
<li>Their ability as a validator either in other ecosystems or testnets of Avail.</li>
<li>Ecosystem contributions (Infra, Wallets/Products, Dashboards, Dev tooling, community education / devrel hacker house assistance, global expansion strategy, strategic partnerships, custody etc)</li>
</ol>
<p>Inclusion in the program is decided and evaluated by in internal committee comprised of team leads and representatives of the foundation.<br>
In future phases of this program, community members can be added to the committee.</p>
<p>This committee has the right to add / remove nominations to participants of the program at any time.</p>
<p>Full details of this committee and its purpose / responsibilities can be found here:</p><aside class="quote quote-modified" data-post="1" data-topic="1570">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/forum.availproject.org/socialforging/48/849_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://forum.availproject.org/t/avail-s-nomination-program-committee-objectives-composition-responsibilities-values/1570">Avail’s Nomination Program Committee: Objectives, Composition, Responsibilities, Values</a> <a class="badge-category__wrapper " href="https://forum.availproject.org/c/node-operators/11"><span data-category-id="11" style="--category-badge-color: #58C8F6; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Use this space for all validator and node-related discussions and announcements."><span class="badge-category__name">Node Operators</span></span></a>
    </div>
  </div>
  <blockquote>
    The Avail Foundation sets out to provide nomination to ecosystem participants to assist in the decentralization of the network. 
Avail’s Nomination Program Committee (NPC) is tasked with the responsibility of managing the nominations that the foundation places into the network via the Nomination Program outlined in AIP 4. 
The Nomination Program Committee reviews all applications through the Nomination Program and provides a note of acceptance into the program to the applicant. 
<a name="p-2669-objectives-of-the-nomination-program-committee-1" class="anchor" href="#p-2669-objectives-of-the-nomination-program-committee-1" aria-label="Heading link"></a>Objectives of th…
  </blockquote>
</aside>

<p><strong>Committee members:</strong><br>
Tanisha Katara (Governance Facilitator)<br>
Jackson Lewis (Network Operations / Validator Engagement Lead)<br>
Toufeeq Pasha (Sr Blockchain Engineer)</p>
<p><strong>Rationale and Reasoning</strong> : The nomination program enables the foundation to support ecosystem participants while promoting the development of a healthy and robust validator set. Although nominations do not guarantee inclusion in the active validator set, they can increase the chances of being elected by strengthening the candidate’s overall position. This support helps validators grow and contribute to the network’s security and decentralisation.</p>
<p>The eligibility criteria and criteria for further consideration ensures that only the most qualified and reliable validators participate in the Nomination program.<br>
Failure to meet the minimum eligibility criteria at any point will result in disqualification from the program.</p>
<p>By maintaining a high standard, Avail aims to uphold the integrity and security of the network. By being transparent and clear, Avail aims to empower meritocratic validators coming from all walks of life.</p>
<p><strong>Monitoring Mechanisms:</strong></p>
<p>The Nomination Program will have a monitoring algorithm present that operates in the background.<br>
This algorithm is re-calculating at regular interval the spread of funds between all participants involved in the nomination program (all operators who have a foundation nomination)</p>
<p><em><strong>NOTE : These parameters in the algorithm are currently being tested, and may be subject to change at the conclusion of this testing period.<br>
This algorithm will be active at a later date.</strong></em></p>
<p>The current planned on-chain metrics are split into 3 categories and are as follows:</p>
<p><strong>Performance</strong></p>
<ul>
<li><strong>Faults: D</strong>emerits based on offline events while being a node operator. These have on-chain consequences</li>
<li><strong>Offline Time:</strong> Downtime during the time of the nomination.</li>
<li><strong>Unclaimed Rewards:</strong> Penalty for unclaimed rewards over 4 eras.</li>
<li><strong>Inclusion:</strong> Inclusion in the active set over the past 84 eras. A candidate can be assured of full score if there were no stints of active validation in 84 eras.</li>
<li><strong>Discovery: D</strong>etermined by comparing the candidate’s tenure in the program relative to other candidates. A candidate that is in the program for a longer duration relative to the entire group of validators allows for a higher score.</li>
</ul>
<p><strong>Bonded</strong></p>
<ul>
<li><strong>Bonded Stake:</strong> Higher bond yields more points to reflect commitment</li>
</ul>
<p><strong>Other Factors</strong></p>
<ul>
<li><strong>Nominated:</strong> Last nomination compared to others</li>
<li><strong>Rank:</strong> Relative rank in the validator pool</li>
<li><strong>Location:</strong> Validators in underrepresented regions.</li>
<li><strong>ISP:</strong> Rewards decentralization of ISP</li>
</ul>
<hr>
<p><strong>Backwards Compatibility:</strong> This proposal does not change the underlying consensus mechanism. As a result, there are no compatibility issues with existing validators or the network’s operation. The nomination program does not affect the core processes or introduce any disruptions, making it fully backward-compatible.</p>
<p>This program’s rollout will be managed in the following format:</p>
<p><strong>First stage:</strong><br>
AIP + Application opens.<br>
In this stage, all ecosystem participants will be able to apply to join the nomination program. (application form in comments below)<br>
Nominations will start to be provided in some congruence with active set expansions.</p>
<p><strong>Second Stage:</strong><br>
Implementation of the above mentioned algorithm for monitoring + distribution of funds.</p>
<p><strong>Third Stage:</strong><br>
Implementation of a public dashboard that has a running report of the participants in the nomination program and the algorithms management of stake.</p>
<p><strong>Expected participant numbers:</strong><br>
As outlined in previous <a href="https://blog.availproject.org/community-rollout-for-decentralized-mainnet-validators/" rel="noopener nofollow ugc">blog post</a>, the planned expansion of the network will occur over time.<br>
The nomination program has no set limitations on how many people can be included in it.</p>
<p><strong>Ensuring the successful applicants are good for the network:</strong><br>
The application process helps define to the committee how well versed the applicant is in validating. To ensure the foundation is supporting participants who will contribute to a strong on chain environment and adherence to active set operations, the operators prove-able past experience in other networks and or Avail testnets is a core component of evaluation.</p>
<p><strong>Security Considerations or Risks</strong>:<br>
The proposed nomination program will not impact the core consensus mechanisms.</p>
<p>This proposal offers a balanced approach to enhancing network scalability while maintaining security and decentralization.</p>
<p>The nominations provide assistance in active set inclusion, as the active set expands, the network becomes more decentralized. The further the network decentralizes, the more natural mitigation there is against any large outages across nodes, potential bad actors or collusion.</p>
<p>We urge the community to support this proposal to ensure the continued growth and robustness of the network.</p>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

The following replies were migrated from the original forum topic in chronological order.

<a id="post-2"></a>

### Post 2

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-10-23T13:44:19.685Z |
| Updated | 2024-10-23T13:44:19.685Z |
| Forum post number | 2 |
| Forum post ID | 2671 |
| Likes | 4 |

<div class="discourse-post-content">

<p>Ecosystem participants are welcome and encouraged to submit an application for nomination using the following link:<br>
<a href="https://forms.gle/cENpC5DHfMWiVfNP8" class="onebox" target="_blank" rel="noopener">https://forms.gle/cENpC5DHfMWiVfNP8</a></p>
<p>Thank you for your continued support!</p>

</div>

<a id="post-3"></a>

### Post 3

| Field | Value |
| --- | --- |
| Author | Shez (@shez) |
| Posted | 2024-10-23T17:06:47.433Z |
| Updated | 2024-10-23T17:08:03.488Z |
| Forum post number | 3 |
| Forum post ID | 2672 |
| Likes | 2 |

<div class="discourse-post-content">

<p>Nice addition to help grow the ecosystem.</p>
<p>I would however suggest we change point 2.</p>
<p>This should change <em>“must not have been slashed more than twice”</em> to the validator should never be slashed</p>
<p>also I assume one node per validator, so would recommend changing this <em>“If already operating an active set node”</em> to something like the foundation will only provide nomination for one node per validator. Provides the impression maybe you can have 2-3 nominations from foundation.</p>
<p>But other than that, looks good.</p>

</div>

<a id="post-4"></a>

### Post 4

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-10-23T17:51:35.821Z |
| Updated | 2024-10-23T17:51:35.821Z |
| Forum post number | 4 |
| Forum post ID | 2673 |
| Likes | 1 |

<div class="discourse-post-content">

<p>Hey Shez thanks for your inputs!</p>
<p>Ill take that suggestion of slashable offense, being any, not just twice, under consideration.</p>
<p>As for the “if already operating an active set node” this will remain the same, as validators can enter the active set through their own stake entirely, yet still apply for nomination consideration due to ecosystem participation etc.</p>

</div>

<a id="post-5"></a>

### Post 5

| Field | Value |
| --- | --- |
| Author | Adam VNBnode (@Adam_VNBnode) |
| Posted | 2024-10-24T02:41:17.628Z |
| Updated | 2024-10-24T03:07:06.327Z |
| Forum post number | 5 |
| Forum post ID | 2675 |
| Likes | 1 |

<div class="discourse-post-content">

<p>i have some feedback as below:<br>
Validators must manage their node by themself and never get slashed even once.<br>
One party can only operate 1 validator and get nominate once from foundation only.<br>
Please consider</p>

</div>

<a id="post-6"></a>

### Post 6

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-10-24T08:07:51.776Z |
| Updated | 2024-10-24T08:07:51.776Z |
| Forum post number | 6 |
| Forum post ID | 2676 |
| Likes | 2 |

<div class="discourse-post-content">

<p>Hey Adam, thanks for your contribution!</p>
<p>The point here about only operating their own node, doesn’t always work. Many entities that wish to join even work with some our genesis validators / other well known validating entities due to jurisdictional / legal requirements.</p>
<p>We have it set as such, so that we would effectively evaluate that third party in the same way we would evaluate an in house team.<br>
That third party would need to have all of the following:</p>
<ol>
<li>Dedicated team of 24 hour period</li>
<li>Sufficient monitoring processes and SecOps</li>
<li>Experience operating in substrate networks and others</li>
</ol>
<p>As for the Second point, this is already the case. Any one entity can only receive nomination for one node. One application.</p>

</div>

<a id="post-7"></a>

### Post 7

| Field | Value |
| --- | --- |
| Author | @CoinStudio |
| Posted | 2024-10-24T11:16:34.727Z |
| Updated | 2024-10-24T11:16:34.727Z |
| Forum post number | 7 |
| Forum post ID | 2677 |
| Likes | 2 |

<div class="discourse-post-content">

<p>The program seems well thought out and clearly defined. I support the Program as it promotes decentralization, independence, and geographic distribution of validators, which strengthens the network’s security and resilience.</p>

</div>

<a id="post-8"></a>

### Post 8

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-10-28T11:37:33.910Z |
| Updated | 2024-10-28T11:37:33.910Z |
| Forum post number | 8 |
| Forum post ID | 2684 |
| Likes | 2 |

<div class="discourse-post-content">

<aside class="quote no-group" data-username="SocialForging" data-post="1" data-topic="1571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/forum.availproject.org/socialforging/48/849_2.png" class="avatar"> SocialForging:</div>
<blockquote>
<p>When operating an active set node, the entity must not have been slashed.</p>
</blockquote>
</aside>
<p>An edit has been made to this section, based on community input listed in comments above.</p>

</div>
