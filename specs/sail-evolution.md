# SAIL — Adversarial Co-Evolution Layer

**Version:** 4.2  
**Status:** Active  
**Date:** 2026-04-08  
**Related Research:** /research/sail-evolution/  
**Related ADR:** ADR-002

## 1. Purpose

SAIL is the mandatory L4 layer in the GCES architecture. Its purpose is to subject every hypothesis to adaptive adversarial pressure before it can influence semantic conflict resolution or trust computation.

SAIL replaces random adversarial testing with a **self-targeting co-evolution loop**.

## 2. Core Invariants

- No hypothesis may enter SCE without a valid `ResilienceMetrics` record from SAIL.
- Every conflict reported by SCE must be traceable to specific attacks (`attack_trace`).
- Every attack strategy must be evaluated and adapted based on observed conflicts and resilience degradation.
- SAIL must maintain diversity of attack strategies (exploration rate ≥ 0.10).

## 3. ResilienceScore (formal definition)

\[
\text{ResilienceScore}(h, t) = \sum_{k=1}^{4} w_k(t) \cdot d_k(h, t)
\]

where:
- \( d_1 \) = semantic_stability ∈ [0,1]
- \( d_2 \) = provenance_integrity ∈ [0,1]
- \( d_3 \) = temporal_consistency ∈ [0,1]
- \( d_4 \) = trust_alignment ∈ [0,1]
- \( w_k(t) \) — dynamic weights derived from GQRVP agent weighting model (Acc, Div, Indep + recent impact)

Default initial weights: semantic=0.35, provenance=0.25, temporal=0.20, trust=0.20.

## 4. Main Components

### 4.1 Attack Engine
- Adaptive strategy selection (weighted + exploration)
- Self-targeting: increases weight of strategies targeting the current `weakest_dimension`
- Attack types: semantic_contradiction, temporal_drift, provenance_corruption, coordinated

### 4.2 Resilience Evaluator
- Computes ResilienceScore using the formula above
- Produces `StressedHypothesisEvent` with degradation vector and weakest_dimension

### 4.3 Learning Loop
- Receives `ConflictReportEvent` from SCE
- Updates strategy weights based on weakest_points and resilience degradation
- Feeds updated strategies back into the next generation

## 5. Event Flow (mandatory sequence)

1. HypothesisEvent → SAIL
2. SAIL generates attacks → AdversarialAttackEvent
3. SAIL applies attacks → StressedHypothesisEvent + ResilienceMetrics
4. SCE processes → ConflictReportEvent
5. SAIL learns → SAILEvolutionEvent (strategy updates)
6. Updated hypotheses → Trust Engine / Consensus (only if ResilienceScore meets threshold)

## 6. Integration Points

- **With GQRVP**: ResilienceScore modifies \( V(c, a_i, t) \) and contributes to \( \mathcal{S}(c) \)
- **With Distributed Layer**: SAIL Node calls Rust kernel via gRPC for ComputeResilience and LearnFromFeedback
- **With Trust Engine v2**: ResilienceScore becomes primary input for trust profile update

## 7. Thresholds (configurable)

- Minimum ResilienceScore to proceed: 0.65 (recommended)
- Exploration rate: 0.10 – 0.20
- Strategy weight bounds: [0.4, 2.5]

This specification defines the stable interface and invariants of SAIL. Implementation details and historical reasoning are kept in /research/sail-evolution/.
