# 06-adversarial-model: Adversarial Model for Distributed Layer

**Status:** Accepted  
**Date:** 2026-04-08

## Assumptions

- QPT adversary (quantum polynomial time)
- Up to (1-θ) corrupted nodes (θ > 2/3 honest majority)
- Network is partially synchronous with known Δ

## Threats Considered

- Node compromise and Byzantine behavior
- Message reordering / dropping
- Strategy overfitting attacks
- Coordinator spoofing

## Mitigations

- EventBus with signed events + replay protection
- Coordinator HA + generation barriers
- ResilienceScore as additional verification signal

**Links:** GQRVP adversarial model section
