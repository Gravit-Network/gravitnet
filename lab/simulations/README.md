# Gravit Lab — Experiments

This directory contains all experimental setups, results and analysis for the Gravit Trust Protocol.

Every experiment is linked to specific GCPs and includes:
• setup description
• code / notebook
• metrics
• interpretation
• comparison with baselines

---

## Experiment Progression

**Baseline** — honest behavior (GCP-0002)
**Sybil Attack** — identity multiplication (GCP-0003)
**Collusion Attack** — coordinated reinforcement
**Multi-phase Attack** — temporal strategy evolution
**Adaptive Adversary** — rule-based adaptation
**Irreversible Trust** — scar & asymmetric decay
**Phase-aware Anomaly Detection** — contextual detection
**Reputation Tiers** — operational trust levels
**RL Adversary** — learning adversary (in progress)

---

## How to Run Experiments

1. Use the engine package in this repository (engine/)
2. Run `python core/src/runtime.py`
3. Use notebooks in this folder for analysis
4. Compare results against baseline

All experiments are reproducible with fixed random seeds.
