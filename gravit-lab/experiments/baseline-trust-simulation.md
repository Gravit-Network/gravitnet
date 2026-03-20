# Baseline Trust Simulation

Version: 0.1
Type: Baseline Experiment
Related: GCP-0002, GCP-0007

---

# Objective

To evaluate the behavior of the Gravit Trust Model under non-adversarial conditions.

This experiment establishes a baseline for:

• trust convergence
• stability of propagation
• distribution of trust scores

---

# Setup

## Network

Number of nodes: 8
Topology: random graph
Average connections per node: 3

---

## Node Behavior

All nodes are honest.

• no adversarial activity
• signals are consistent
• no manipulation

---

## Parameters

λ = 0.015
η = 0.30

Thresholds:

θ_w = 0.55
θ_q = 0.35
θ_r = 0.65

---

# Execution

Simulation runs for:

10 time steps

At each step:

1. trust decay applied
2. reputation propagated
3. node states updated

---

# Observations

Expected behavior:

• trust values stabilize over time
• no nodes enter QUARANTINE
• system converges to equilibrium

---

# Metrics

Tracked metrics:

• average trust score
• variance of trust
• number of WARNING nodes
• number of QUARANTINED nodes

---

# Example Output (Engine)

Step 0:
τ ≈ random distribution

Step 5:
τ begins stabilizing

Step 10:
τ converges to narrow range

---

# Expected Results

• system stability
• absence of extreme divergence
• smooth trust propagation

---

# Interpretation

This experiment validates:

• correctness of trust aggregation
• stability of propagation
• absence of false positives

---

# Next Experiments

Following experiments:

• Sybil attack simulation
• collusion cluster modeling
• parameter sensitivity analysis

---

# Notes

This baseline is critical.

All future adversarial experiments must be compared against it.
