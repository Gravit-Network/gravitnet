# 05-sce-integration: Tight Coupling Between SAIL and SCE

**Status:** Accepted  
**Date:** 2026-04-08

## Decision

SAIL and SCE form a closed adversarial-conflict loop:

- SAIL → produces `StressedHypothesisEvent` + `attack_trace`
- SCE → produces `ConflictReportEvent` with `weakest_points`
- SAIL → learns from the report and adjusts strategy weights

**Invariant:** Every conflict must have an associated `attack_trace`. Every attack must be evaluated through observed conflicts.

This loop is the practical realization of GQRVP’s semantic verification + weighted consensus.

**Links:** /research/distributed-execution/02-eventbus-only-decision.md
