# 03-resilience-score-evolution: From Simple Survival Rate to GQRVP-aligned ResilienceScore

**Status:** Accepted  
**Date:** 2026-04-08

## Evolution Path

- v1: Simple survival_rate = 1.0 - (attacks × 0.15)
- v2: Weighted dimensions (semantic, provenance, temporal)
- v3 (current): Full GQRVP-aligned formula

\[
\text{ResilienceScore}(h, t) = \sum_{k=1}^{4} w_k(t) \cdot d_k(h, t)
\]

where \( d_k \) = semantic_stability, provenance_integrity, temporal_consistency, trust_alignment.

## Why this evolution matters

ResilienceScore became the computable bridge between SAIL attacks and Trust Engine v2, directly modifying \( V(c, a_i, t) \).

**Links:** /research/distributed-execution/05-resilience-metrics.md
