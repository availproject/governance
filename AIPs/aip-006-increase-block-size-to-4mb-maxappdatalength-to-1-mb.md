# AIP 6: Increase Block Size to 4MB & MaxAppDataLength to 1 MB

> **Migration notice:** This material was migrated from the Avail Forum to GitHub ahead of the forum's permanent closure on August 22, 2026. The original forum URL is retained as a historical source identifier, but the migrated content and source snapshots are preserved in this repository.

| Field | Value |
| --- | --- |
| Historical forum URL | https://forum.availproject.org/t/aip-6-increase-block-size-to-4mb-maxappdatalength-to-1-mb/1648 |
| Forum topic ID | 1648 |
| Original category | Avail Improvement Proposal (AIP) |
| Original author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Created | 2025-01-29T03:15:11.457Z |
| Last posted | 2025-01-29T03:15:11.528Z |
| Forum posts included | 1 |
| Highest forum post number | 1 |
| Raw JSON snapshot | [topic-1648.json](../archive/raw-json/topic-1648.json) |
| Raw HTML snapshot | [topic-1648.html](../archive/raw-html/topic-1648.html) |

## Original Post

<a id="post-1"></a>

### Post 1

| Field | Value |
| --- | --- |
| Author | Toufeeq  Pasha (@Toufeeq_Pasha) |
| Posted | 2025-01-29T03:15:11.528Z |
| Updated | 2025-01-29T03:15:11.528Z |
| Forum post number | 1 |
| Forum post ID | 2784 |
| Likes | 7 |

<div class="discourse-post-content">

<p><strong>Author:</strong> Toufeeq</p>
<p><strong>Technical Summary:</strong></p>
<p>This AIP proposes two changes:</p>
<ul>
<li>Raising the block size limit on Avail mainnet from 2MB to 4MB.</li>
<li>Increasing maximum DA tx size (MaxAppDataLength) from 0.5MB to 1MB.</li>
</ul>
<p>Avail’s 20-second block time ensures smooth propagation of larger blocks, and testing on the Turing testnet confirms no adverse impact on network performance or validation times for these changes.</p>
<p><strong>Motivation:</strong></p>
<p>The current 2MB block size and 512KB DA transaction size are becoming bottlenecks due to the growing demand for blockspace and larger data submissions. Increasing the block size to 4MB and DA transaction size to 1MB addresses these limitations, ensuring that Avail remains scalable, efficient, and competitive for the community.</p>
<p><strong>Rationale and Reasoning:</strong></p>
<p>The proposed changes have been successfully tested on the Turing testnet, which mirrors the mainnet environment. These tests demonstrate:</p>
<ul>
<li>Smooth block propagation within the 20-second interval.</li>
<li>No significant additional resource burden on validators.</li>
<li>Sustained network performance metrics.</li>
</ul>
<p>Increasing the max DA transaction size allows users to submit larger data in a single transaction, reducing overhead and improving efficiency. Combined with the increased block size, Avail can better support applications requiring large data submissions without operational trade-offs.</p>
<p><strong>Security Considerations or Risks:</strong></p>
<p>Extensive testing on the Turing confirms that these changes pose no risks to network stability or security. The proposed changes can be implemented via a single governance call containing both increasing the block matrix size and updating the runtime parameter MaxAppDataLength to 1MB, with no changes needed to consensus or other core mechanisms.</p>
<p><strong>Copyright Waiver:</strong></p>
<p>Copyright and related rights waived via CC0.</p>

</div>

## Forum Discussion

_No replies were present in the migrated forum topic._
