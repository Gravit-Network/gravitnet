# Sybil Attack Simulation v0.1

Version: 0.1
Type: Adversarial Experiment
Related: GCP-0002, GCP-0003, GCP-0007

---

# Objective

To evaluate the resilience of the Gravit Trust Protocol under Sybil attack conditions.

The experiment measures how artificially created nodes affect trust distribution and influence propagation.

---

# Setup

## Network

Total nodes: 40
Honest nodes: 32
Sybil nodes: 8 (20%)

Topology:

• honest nodes → random connections
• Sybil nodes → dense internal connections + outward links

---

## Node Behavior

### Honest Nodes

• generate consistent signals
• normal connectivity

### Sybil Nodes

• highly interconnected
• reinforce each other’s reputation
• optionally emit biased signals

---

# Parameters

λ = 0.015
η = 0.30

Sybil penalty:

ρ_max = 0.08
σ = 0.40

---

# Experiment Variants

## Variant A — No Penalty

Sybil nodes operate without restriction.

Expected:

• Sybil cluster dominates trust
• reputation inflation occurs

---

## Variant B — With Penalty

Density-based penalty applied.

Expected:

• Sybil influence reduced
• honest nodes dominate

---

# Metrics

• average trust (honest vs Sybil)
• max influence node
• trust distribution variance
• number of quarantined nodes

---

# Expected Results

Without penalty:

→ Sybil cluster gains disproportionate influence

With penalty:

→ trust stabilizes
→ Sybil nodes suppressed

---

# Interpretation

This experiment validates:

• Sybil resistance mechanism
• importance of density penalty
• robustness of trust propagation

---

# Next Steps

• signal injection under Sybil
• collusion cluster experiments
• parameter sensitivity analysis
