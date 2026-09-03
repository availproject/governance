# Transparency Report 21: Technical Committee Actions During Mainnet Recovery

**Report Author:** Toufeeq [5CoVaWrZnaV3BSeUJCA8Ca3SPMJDtjT1zPvZkzovkxJU7dkr]

**Execution Details:** The Technical Committee approved and executed a series of emergency proposals beginning with Technical Committee proposal #44.

**Technical Committee Consensus:** All the proposals covered by this report received the required Technical Committee votes.

## Introduction

This report provides transparency to the Avail community regarding the emergency actions approved by the Avail Technical Committee (TC) in response to the recent Mainnet incident.

The incident affected both block production and finality. Following the initial runtime upgrade, validators continued producing blocks successfully, but a bug in the upgraded runtime prevented production of the next epoch-transition block. Because the chain could not advance beyond that boundary, block production halted for approximately 3 hours and 45 minutes.

Block production was restored operationally by running the node with a previously stable Wasm runtime through the runtime-override mechanism. This restoration occurred before the subsequent corrective governance proposals were executed. The emergency proposals that followed were primarily required to recover stalled GRANDPA finality and to normalize the on-chain runtime, staking, and validator state.

A separate incident report will provide the detailed technical analysis, impact assessment, and response timeline. This transparency report focuses on the Technical Committee's actions and the reasons for using emergency governance.

## Why Emergency Governance Was Used

After block production resumed, GRANDPA finality remained stalled. Recovering finality required a coordinated transition of the GRANDPA authority set together with changes to staking and validator state. These actions could not safely wait the 3-day execution delay associated with the standard governance process.

Emergency governance was used to:

- mitigate the originally reported block-production vulnerability through the initial runtime v54 upgrade
- force a new era and establish a smaller validator set for recovery
- prevent validators from being penalized for downtime caused by the protocol-level incident and coordinated recovery
- signal stalled GRANDPA finality and enable an authority-set transition
- begin expanding the validator set after finality and network stability were restored

The emergency actions were limited to the changes needed to mitigate the vulnerability, recover finality, and normalize network state.

## Governance Proposals and Code References

| Proposal | Approved action | Purpose |
| --- | --- | --- |
| [#44](https://avail.subscan.io/tech/44) | Upgrade to runtime v54 through `System::set_code` | Mitigate the privately reported block-production vulnerability by reserving resources for the mandatory post-inherent |
| [#49](https://avail.subscan.io/tech/49) & [#56](https://avail.subscan.io/tech/56) | Cancel all deferred slashes from eras 816 and 817, respectively | Prevent validators from being penalized for incident-related downtime |
| [#50](https://avail.subscan.io/tech/50) | Force a new era, set the validator count to 10, and designate some invulnerable validators | Decrease the validator set for finality recovery |
| [#52](https://avail.subscan.io/tech/52) | Invoke `Grandpa::note_stalled` with a 3-block delay and block 3,403,743 as the best finalized block | Signal stalled finality and enable the required GRANDPA authority-set transition |
| [#53](https://avail.subscan.io/tech/53) | Upgrade to runtime v55 through `System::set_code` | Update the on-chain runtime to the previously stable runtime after block production had already resumed through the Wasm runtime override |
| [#54](https://avail.subscan.io/tech/54) | Increase the validator count from 10 to 15 | Begin controlled expansion of the validator set after network stabilization |
| [#55](https://avail.subscan.io/tech/55) | Upgrade to corrected runtime v56 through `System::set_code` | Update the runtime to correctly fix the originally reported vulnerability |

The initial validator-count reduction was a temporary recovery measure and should not be interpreted as a change to Avail's long-term decentralization objectives. Additional Technical Committee proposals will be created to gradually increase the active validator set until the previous validator count is restored. Similarly, the slash cancellation was limited to slash records arising from the affected eras and did not alter Avail's general slashing policy.

Code references:

- [v56 runtime to fix the originally reported vulnerability](https://github.com/availproject/avail/pull/852)
- [Mainnet code-substitute change](https://github.com/availproject/avail/pull/847)

## Supporting Node Releases

The Wasm runtime override used during the incident allowed validators to execute the previously stable runtime and resume block production before the stable runtime was updated on-chain. It was an operational recovery mechanism and was not itself a Technical Committee proposal.

The Avail node's embedded Mainnet chain specification was subsequently updated with a runtime code substitute. This allows nodes syncing from an earlier snapshot or replaying Mainnet history to pass through the affected runtime range and follow the canonical chain. Once a node reaches the on-chain v55 runtime, it resumes using the on-chain runtime normally.

The code substitute does not rewrite finalized chain state. It is a client-side compatibility measure for node operators joining or resynchronizing after the incident.

## Consolidated Outcome

The Wasm runtime override restored block production and network liveness. The Technical Committee proposals then:

- decreased the validator set for recovery
- cancelled incident-related slashes
- forced a new era to rotate the validator set
- updated the stable runtime on-chain
- enabled recovery of stalled GRANDPA finality
- began the controlled expansion of validator participation.

Although these were separate governance proposals, they formed one coordinated finality and network-state recovery objective.

The Technical Committee used emergency governance because these finality-recovery actions were time-sensitive and had to be coordinated across multiple validator operators.

If you have any questions or concerns regarding these governance actions, please write to us.

Thank you.
