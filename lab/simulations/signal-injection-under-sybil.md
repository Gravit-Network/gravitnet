# Signal Injection under Sybil

Version: 0.1
Type: Adversarial Signal Experiment
Related: GCP-0002, GCP-0003, GCP-0006, GCP-0007

---

# Objective

To evaluate how the Gravit Trust Protocol responds to adversarial signal injection.

Specifically:

• Sybil nodes emit biased signals
• honest nodes emit consistent signals
• system must resist manipulation

---

# Setup

## Network

Total nodes: 40
Sybil nodes: 20%

Topology:

• Sybil cluster dense
• honest nodes random

---

## Signal Behavior

### Honest Nodes

• send positive signals to neighbors
• low variance

### Sybil Nodes

• reinforce each other (strong positive signals)
• send negative signals to honest nodes

---

# Parameters

λ = 0.015
η = 0.30

Signal weights:

• honest: +0.05
• Sybil internal: +0.1
• Sybil external: -0.05

---

# Experiment Variants

## Variant A — No Epistemic Filtering

Signals applied directly.

Expected:

• Sybil cluster amplifies itself
• honest nodes suppressed

---

## Variant B — With Filtering (future)

Introduce:

• credibility weighting
• source trust scaling

Expected:

• Sybil influence reduced

---

# Metrics

• average trust (honest vs Sybil)
• signal impact on p and s
• number of false trust elevations
• recovery time

---

# Expected Results

Without filtering:

→ Sybil nodes dominate via signal spam

With filtering:

→ trust stabilizes
→ manipulation reduced

---

# Interpretation

This experiment demonstrates:

• importance of epistemology (GCP-0006)
• vulnerability of naive signal models
• need for signal weighting by trust

---

# Next Steps

• implement trust-weighted signals
• introduce credibility scoring
• test delayed attacks
