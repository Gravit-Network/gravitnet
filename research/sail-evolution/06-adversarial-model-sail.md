# 06-adversarial-model-sail: Adversarial Model Specific to SAIL

**Status:** Accepted  
**Date:** 2026-04-08

## Threats

- Overfitting to current weaknesses (strategy collapse)
- Noise amplification through feedback loop
- Coordinated multi-hypothesis attacks
- Gradient-like exploitation of ResilienceScore

## Mitigations

- Exploration rate in strategy selection
- Threshold filtering on feedback
- Diversity requirement across SAIL nodes
- Periodic reset of strategy weights

**Links:** /research/distributed-execution/06-adversarial-model.md
