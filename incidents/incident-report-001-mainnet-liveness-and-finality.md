# Avail DA Mainnet Incident Report

**Date:** September 3, 2026
**Status:** Mitigated
**Impact:** Critical network outage affecting block production and finality

---

## Executive Summary

On August 31, 2026, the Avail DA mainnet experienced a critical outage that halted block production for about ~4 hours and delayed finality for an additional ~12 hours. The outage was triggered by a faulty emergency runtime upgrade that failed on the first epoch-transitioning block after it was applied.

Normal block production was restored within ~4 hours, but block production slowed down and finality got stuck again due to a cascade of validator set changes triggered by the first outage. Chain operation was fully restored at 04:58 UTC on September 1, and all network services, including the VectorX bridge, are now fully operational. For details of the emergency Technical Committee proposals used during the recovery, see [Transparency Report 21: Technical Committee Actions During Mainnet Recovery](../transparency-reports/transparency-report-021-technical-committee-actions-during-mainnet-recovery.md).

We sincerely apologise to our users, validators, and the broader Avail community for the disruption. Below, we provide an account of what happened, how we responded, and the steps we are taking to prevent this from happening again.

---

## What Happened

| Time (UTC) | Event |
| --- | --- |
| **Aug 28** | Private report of critical vulnerability received, team began working on an emergency fix |
| **Aug 31, 10:41** | Fix for the critical vulnerability applied to turing testnet via Technical Committee proposal |
| **Aug 31, 10:54** | Same fix applied to mainnet via a Technical Committee emergency proposal |
| **Aug 31, 12:38** | Block production halts due to a bug in the runtime upgrade which prevented validators from creating the epoch-transitioning block |
| **Aug 31, 16:23** | Block production resumed after validators started applying a manual WASM override.  |
| **Aug 31, 16:23-22:00** | Validators were urged to apply the wasm override in order to participate in block production and finality votes. |
| **Aug 31, ~22:00** | 2/3 of active set updated. Finality briefly resumed but stalled again due to validator set changes at block #3403743. The set change was a result of slashing events during the halt period. |
| **Sep 1, 04:58** | Finality fully restored after Technical Committee action and coordinated validator effort |
| **Sep 1, 07:54** | Network services, including the VectorX bridge, fully operational |

---

## Impact

**During the outage:**

- **DA submissions** were not possible during the ~3h45m block production halt. Submissions made after liveness returned were not finalised until 04:58 UTC.
- **The VectorX bridge** (Avail → Ethereum) was temporarily unavailable while finality was down. It briefly resumed when finality first returned (~22:00 UTC) and was fully restored after the chain stabilised.
- **Validators and nominators:** Many validators were slashed and removed from the active set as a side effect of the outage.  All slashing event have been cancelled by the Technical Committee. **No validator or nominator stake has been lost.**
- **Staking rewards:** Some validators missed rewards for the affected eras. The active set was temporarily reduced to 10 validators (4 Foundation-operated, 6 external) to restore finality with minimal coordination.

---

## Root Cause

The outage was triggered by an **emergency runtime upgrade** applied via Technical Committee proposal #44 at block #3403608. The upgrade was intended to fix a privately-reported critical vulnerability and had been applied to Turing testnet minutes earlier.

The new runtime failed when executing **epoch-transitioning block #3403664** at 12:38 UTC. No node was able to produce this block, causing block production and finality to halt.

**Why did this reach mainnet?**

1. **Insufficient testnet soak:** The upgrade was applied to mainnet only minutes after Turing, before Turing had crossed an epoch boundary. The failure mode, triggered by epoch transition, was never revealed on testnet.
2. **Emergency RTU process:** The current emergency runtime upgrade process has no required soak period or explicit requirement to survive N epochs/eras on testnet before mainnet deployment.
3. **No offline testing:** The epoch-transition path was not exercised offline using `try-runtime` or fork-off simulation. Normal blocks were tested and they had passed.

---

## What Went Wrong (Process Failures)

### 1. Slashing Cascade

When the chain halted, the network's offence logic treated every validator as unresponsive and slashed them in two waves. At block #3403743, these slashes removed many validators from the active set and activated a new 26-validator authority set that did not have the patch and were not able to produce and finalise blocks.

A protection mechanism designed for malicious nodes misbehaving turned a recoverable liveness fault into a validator-set and governance crisis, and was the main driver of the ~12h additional finality outage.

### 2. Recovery Coordination Delays

Restoring finality required manual coordination with external validators to run a node flag, which is slow and depends on operator availability.

### 3. No On-Chain Rollback Path

Once the chain halted, the Technical Committee could roll back Turing on-chain, but mainnet required node-level overrides because no blocks could be produced to execute a rollback.

---

## What We Are Doing to Prevent Recurrence

### Runtime Upgrade Policy (P0)

All future emergency runtime upgrades will test the epoch-transitioning block production before being applied to mainnet. Even in emergency situations, at least offline testing of this scenario must be done.

### Slashing Logic Review (P0)

We are reviewing and updating the network's offence and validator-set rotation logic so that **a network-wide halt does not slash honest validators or rotate in a new set that is also unable to produce or finalise blocks.** This is the most critical technical change to emerge from this incident.

### Detection Improvements (P1)

We are implementing automated alerts for:

- No new best block for >90 seconds
- Finality lag beyond a defined threshold

### Recovery Readiness (P2)

- Formalising a **chain-halt runbook** with pre-tested recovery procedures, verified WASM artefacts with checksums, and documented Technical Committee action sequences
- Maintaining a **validator operator contact list** with escalation channels and expected response times
- Conducting **tabletop exercises** of chain-halt scenarios on Turing

### Validator Set Restoration

We are now working to restore the validator set to its previous size. External validators will be re-added in phases. The Technical Committee will remove invulnerable status from Foundation nodes once the set is stable. A full restoration timeline will be communicated in the coming days.

---

## Acknowledgments

We want to thank our **validators**, the **Technical Committee**, and the broader **Avail community** for their patience and cooperation during this incident. We also acknowledge the impact on our users and integrators.

We are committed to transparency and continuous improvement. This incident has highlighted critical areas for improvement in our testing, alerting, and recovery processes, and we are acting on each of them.

---

## Questions?

If you have any questions about this incident, please reach out via our [Discord](https://app.notion.com/p/avail-project/link) or existing community groups.
