# 05-resilience-metrics: Origin and Role of ResilienceMetrics

**Status:** Accepted  
**Date:** 2026-04-08

## Origin

ResilienceMetrics evolved from the need to make `V(c, a_i, t)` from GQRVP computable under adversarial pressure.

## Definition

```math
ResilienceScore(h, t) = w₁·semantic_stability + w₂·provenance_integrity + w₃·temporal_consistency + w₄·trust_alignment
```

It serves as the bridge between SAIL attacks and Trust Engine v2.

## Role in Distributed Layer

* Returned by Rust SAIL kernel via gRPC
* Used as feedback for strategy learning (self-targeting)
* Becomes part of StressedHypothesisEvent and eventually Anchor(c)

**Links:** /research/sail-evolution/ (future), GQRVP spec
