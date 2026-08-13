# AIP 1: Update Nomination Pool Configuration

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-1-update-nomination-pool-configuration/1498 |
| Forum topic ID | 1498 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Jackson Lewis (@SocialForging) |
| Created | 2024-08-09T15:35:40.892Z |
| Last posted | 2024-08-13T11:52:24.729Z |
| Forum posts included | 9 |
| Highest forum post number | 9 |
| Raw JSON snapshot | [topic-1498.json](../archive/raw-json/topic-1498.json) |
| Raw HTML snapshot | [topic-1498.html](../archive/raw-html/topic-1498.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-08-09T15:35:40.943Z |
| Updated | 2024-08-09T15:51:41.081Z |
| Forum post number | 1 |
| Forum post ID | 2540 |
| Likes | 7 |

<div class="discourse-post-content">

<p><strong>Author:</strong> Jackson Lewis</p>
<p><strong>Technical Summary:</strong><br>
This AIP contains 3 main changes to the Nomination Pool Configuration.<br>
<strong>Limit of nomination pools:</strong> Increase to 100 (from 50)<br>
(The foundation will reserve 10 of these 100 nomination pools to manage nominations.)<br>
<strong>Limit of participants in each pool:</strong> 5000 (from 1000)<br>
<strong>Pool commission rate limit:</strong> 10%</p>
<p><strong>Motivation:</strong><br>
Nomination pools are currently maxed out across both the number of pools and participant limits.<br>
To further ensure an open and accessible staking experience for all ecosystem partners, wallets and stakers, this proposals purpose is to increase these limits.</p>
<p><strong>Rationale and Reasoning:</strong><br>
During the first stages of AVAIL DA Mainnet launch, it’s imperative to ensure that the expansion of active set, nomination pools and participants is increased gradually.</p>
<p>As the limits of individual nomination pools and individual participants have been reached, there is increased demand from community and ecosystem participants.<br>
It’s time to expand these limits within a suitable range.</p>
<p>For example:<br>
Wallets like SubWallet, have hit their pool limits early after Mainnet deployment and are requiring higher limits as their user base is large.</p>
<p>The Nomination pool commission limit:<br>
Setting a 10% maximum is sufficient enough reward for pool handlers, whilst still allowing fluctuation from 0 - 10 dependent on the pool owners choice.</p>
<p><strong>Security Considerations or Risks:</strong><br>
The proposed changes to the nomination pool <strong>does not affect</strong> the Phragmen election process nor consensus mechanisms. Therefore, there are no direct Security Concerns.</p>
<p><strong>Copyright Waiver:</strong> Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

The following replies were migrated from the original forum topic in chronological order.

<a id="post-2"></a>

### Post 2

| Field | Value |
| --- | --- |
| Author | Ryan Haczynski, Head of Protocol Partnerships, GlobalStake 🌎🥩 (@Phunky) |
| Posted | 2024-08-09T16:56:23.915Z |
| Updated | 2024-08-09T16:56:23.915Z |
| Forum post number | 2 |
| Forum post ID | 2541 |
| Likes | 1 |

<div class="discourse-post-content">

<p>Full support. Ship it! <img src="../archive/assets/1498/8b504a698910-ship.png" title=":ship:" class="emoji" alt=":ship:" loading="lazy" width="20" height="20"></p>

</div>

<a id="post-3"></a>

### Post 3

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-08-10T09:25:30.674Z |
| Updated | 2024-08-10T09:25:30.674Z |
| Forum post number | 3 |
| Forum post ID | 2542 |
| Likes | 2 |

<div class="discourse-post-content">

<p>Also: There will be details to come soon re nomination program!</p>

</div>

<a id="post-4"></a>

### Post 4

| Field | Value |
| --- | --- |
| Author | Brightly Stake (@Brightly_Stake) |
| Posted | 2024-08-10T20:44:08.775Z |
| Updated | 2024-08-10T20:44:08.775Z |
| Forum post number | 4 |
| Forum post ID | 2543 |
| Likes | 1 |

<div class="discourse-post-content">

<p>in support of this proposal</p>

</div>

<a id="post-5"></a>

### Post 5

| Field | Value |
| --- | --- |
| Author | Henri | Stakin (@Henri) |
| Posted | 2024-08-12T06:14:33.259Z |
| Updated | 2024-08-12T06:14:33.259Z |
| Forum post number | 5 |
| Forum post ID | 2545 |
| Likes | 5 |

<div class="discourse-post-content">

<p>Hi everyone,</p>
<p>Henri from Stakin here. We support this proposal, but sharing some thoughts for future consideration.</p>
<ul>
<li>
<p>Limit of nomination pools - Yes, we reached this limit quite fast, so increasing the limit to 100 could make sense. However, at the same time, we also need to review the nominations of each pool, to ensure all validators get represented. Not sure how to tackle this yet.</p>
</li>
<li>
<p>Limit of participants in each pool - Full support. We could increase the limit even higher, to avoid the situation where SubWallet needs to create multiple pools just for their users, thus using up the limited space for nomination pools.</p>
</li>
<li>
<p>Commission limit - Don’t see the need for this, to be honest. Is there an issue with too high fees on nomination pools? Generally, this works in the opposite, that there is a minimum fee, so we avoid dumping the market and allow everyone to earn a fair fee while still letting the market to self-regulate.</p>
</li>
</ul>
<p>Thank you!</p>

</div>

<a id="post-6"></a>

### Post 6

| Field | Value |
| --- | --- |
| Author | Dimitri Nikolaros (@diminiko) |
| Posted | 2024-08-12T10:39:45.215Z |
| Updated | 2024-08-12T10:39:45.215Z |
| Forum post number | 6 |
| Forum post ID | 2546 |
| Likes | 1 |

<div class="discourse-post-content">

<p>bountyblok in support for this proposal. Personally, I think it’s a big win for large user base projects which can then benefit the entire ecosystem.</p>

</div>

<a id="post-7"></a>

### Post 7

| Field | Value |
| --- | --- |
| Author | Shez (@shez) |
| Posted | 2024-08-12T10:58:47.644Z |
| Updated | 2024-08-12T10:58:47.644Z |
| Forum post number | 7 |
| Forum post ID | 2548 |
| Likes | 1 |

<div class="discourse-post-content">

<p>Hi</p>
<p>Agree with the proposal. We aka Staking4all currently have a pool, it is growing fast and we expect we will hit the 1000 limit of participants per pool. Would be great if we can increase this limit.</p>
<p>Also due to all 50 pools already been created, we can not create a 2nd pool.</p>
<p>So happy with all suggestions in this post so that pools can be used more easily with less limitations.</p>
<p>Thanks</p>

</div>

<a id="post-8"></a>

### Post 8

| Field | Value |
| --- | --- |
| Author | @CoinStudio |
| Posted | 2024-08-12T12:40:49.370Z |
| Updated | 2024-08-12T12:40:49.370Z |
| Forum post number | 8 |
| Forum post ID | 2550 |
| Likes | 1 |

<div class="discourse-post-content">

<p>Hey everyone,</p>
<p>I’m positively surprised by the pace and number of users participating in the nomination pools—it’s truly remarkable! A big thumbs up to the Subwallet team for exceeding all expectations and onboarding this many nominators.</p>
<p>Our main Pool <span class="hashtag-raw">#6</span> is now close to reaching the current limit of 1000 users, which is an exciting milestone. We are looking forward to the removal of the user upper limit limitation to accommodate even more participants.</p>
<p>CoinStudio is fully in support of AIP1, and we believe it will greatly benefit the community as a whole.</p>
<p>Best,</p>
<p>CoinStudio Team</p>

</div>

<a id="post-9"></a>

### Post 9

| Field | Value |
| --- | --- |
| Author | Jackson Lewis (@SocialForging) |
| Posted | 2024-08-13T11:52:24.729Z |
| Updated | 2024-08-13T11:52:24.729Z |
| Forum post number | 9 |
| Forum post ID | 2554 |
| Likes | 3 |

<div class="discourse-post-content">

<p>AIP1 passes the TC with 5/7 votes. <img src="../archive/assets/1498/34adef7b68b4-rocket.png" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>The activation of these changes will be processed in 2 days.</p>
<p>Transparency report blow <img src="../archive/assets/1498/ad3b624f0581-2.png" title=":point_down:t2:" class="emoji" alt=":point_down:t2:" loading="lazy" width="20" height="20"></p>
<aside class="quote quote-modified" data-post="1" data-topic="1501">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/forum.availproject.org/toufeeq_pasha/48/858_2.png" class="avatar">
    <a href="../transparency-reports/transparency-report-002-nomination-pool-configuration.md">Transparency Report 2: Nomination Pool Configuration</a> <a class="badge-category__wrapper " href="https://forum.availproject.org/c/governance/avail-transparency-report/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #0088CC;" data-parent-category-id="32" data-drop-close="true" class="badge-category --has-parent" title="Avail Transparency Reports (ATR) are simple summaries of upcoming or executed changes made to the Avail Network.
Go to the docs to learn more about Avail Transparency Reports (ATR)."><span class="badge-category__name">Avail Transparency Report</span></span></a>
  </div>
  <blockquote>
    <img width="20" height="20" src="../archive/assets/1498/a8bcf6a2b80e-paperclip.png" title="paperclip" alt="paperclip" class="emoji"> Report Author: Toufeeq from the Avail Technical Committee [5CoVaWrZnaV3BSeUJCA8Ca3SPMJDtjT1zPvZkzovkxJU7dkr] 
Changes to be Executed: Changes will be applied at block #182,680 
Technical Committee Consensus: 5/7 signers <a href="https://avail.subscan.io/tech/11?tab=proposal">https://avail.subscan.io/tech/11?tab=proposal</a> 
Introduction: 
This document aims to provide transparency to the Avail community concerning both upcoming and executed network changes. The Technical Committee (TC) has thoroughly assessed the proposed nomination pool cha…
  </blockquote>
</aside>

</div>
