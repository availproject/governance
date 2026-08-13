# Transparency Report 20: Avail Bridge Wrapped Transaction Safety Fix

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/transparency-report-20-avail-bridge-wrapped-transaction-safety-fix/1773 |
| Forum topic ID | 1773 |
| Original category | Avail Transparency Report |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2026-05-13T03:48:35.350Z |
| Last posted | 2026-05-13T03:48:35.416Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1773.json](../archive/raw-json/topic-1773.json) |
| Raw HTML snapshot | [topic-1773.html](../archive/raw-html/topic-1773.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2026-05-13T03:48:35.416Z |
| Updated | 2026-05-13T03:48:35.416Z |
| Forum post number | 1 |
| Forum post ID | 2936 |
| Likes | 0 |

<div class="discourse-post-content">

<p><strong>Report Author:</strong>  Toufeeq [5CoVaWrZnaV3BSeUJCA8Ca3SPMJDtjT1zPvZkzovkxJU7dkr]</p>
<p><strong>Execution Details:</strong> Changes have been applied at block #<strong>2920735</strong></p>
<p><strong>Technical Committee Consensus:</strong> 5/7 signers <a href="https://avail.subscan.io/tech/38?tab=proposal" class="inline-onebox">Subscan | Aggregate Substrate ecological network high-precision Web3 explorer</a></p>
<h3><a name="p-2936-introduction-1" class="anchor" href="#p-2936-introduction-1" aria-label="Heading link"></a><strong>Introduction</strong></h3>
<p>This report aims to provide transparency to the Avail community regarding an emergency proposal that has been executed on Avail Mainnet. The Avail Technical Committee (TC) approved a runtime upgrade to address a bridge transaction handling issue involving wrapped Vector::send_message calls.</p>
<p>The issue affected bridge send transactions submitted inside call wrappers such as Proxy, Multisig, Scheduler, or Utility batch calls. The runtime upgrade ensures that bridge messages are generated only from direct bridge send transactions, and that wrapped bridge send transactions are rejected during transaction validation.</p>
<p>The TC chose the emergency proposal path for this upgrade because the issue affected the safety of bridge transactions. Waiting through the normal proposal execution delay would have prolonged the period in which wrapped bridge transactions could create unsafe bridge behavior or stuck user funds. The emergency execution allowed the fix to be applied promptly, while this ATR provides post-execution transparency to the community.</p>
<h3><a name="p-2936-executed-changes-2" class="anchor" href="#p-2936-executed-changes-2" aria-label="Heading link"></a>Executed changes</h3>
<p>This upgrade changed the runtime bridge filtering and transaction validation rules for Avail bridge send transactions.</p>
<p>After the upgrade:</p>
<ul>
<li>Direct Vector::send_message bridge transactions continue to work as expected.</li>
<li>Wrapped bridge send transactions are rejected.</li>
<li>Normal non-bridge Proxy, Multisig, Scheduler, and Utility batch transactions continue to work as expected.</li>
</ul>
<h3><a name="p-2936-code-modifications-3" class="anchor" href="#p-2936-code-modifications-3" aria-label="Heading link"></a>Code Modifications:</h3>
<p>For those interested, you can review the necessary code modifications in the following PR:</p>
<p><a href="https://github.com/availproject/avail/pull/823">PR1</a></p>
<h3><a name="p-2936-potential-merits-to-the-network-4" class="anchor" href="#p-2936-potential-merits-to-the-network-4" aria-label="Heading link"></a>Potential Merits to the Network:</h3>
<p>This change improves bridge safety by ensuring bridge data is derived only from supported direct bridge transactions. Previously, wrapped bridge transactions could create an unsafe mismatch between transaction structure and actual execution. In some wrapper cases, an inner bridge call may not execute, while the bridge filter could still interpret the transaction as bridge data.</p>
<p>The upgrade removes this unsafe behaviour by disallowing wrapped bridge sends and keeping bridge proof generation aligned with direct Vector::send_message execution. This helps protect users from stuck bridge transfers and strengthens the integrity of Avail-to-Ethereum bridge message generation.</p>
<p>If you have any questions, feel free to share them on the forum.</p>
<p>Thank you.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
