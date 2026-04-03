# Irreversible Trust Decay Simulation v0.1

Version: 0.1
Type: Resilience Experiment
Related: GCP-0002, GCP-0006, GCP-0011

---

# Objective

To evaluate how the Gravit Trust Protocol handles **irreversible trust loss** — once broken trust is very hard to rebuild.

This models real social reality: betrayal is remembered, forgiveness is slow.

---

# Setup

Total nodes: 50
Temporal attackers: 15%

Attack pattern:

• steps 0–20: perfect honesty
• steps 21–30: strong negative signals
• steps 31+: attempt recovery

---

# Experiment Variants

## Variant A — Symmetric Decay

Normal decay for all nodes

Expected:
→ Attacker recovers relatively fast

## Variant B — Irreversible Decay

Broken trust flag + asymmetric penalties

Expected:
→ Attacker almost never recovers
→ Honest nodes protected long-term

---

# Metrics

• trust trajectory of attackers
• time to full recovery (τ > 0.7)
• honest nodes stability
• false recovery events

---

# Expected Results

Symmetric:
→ Attacker recovers in ~20 steps

Irreversible:
→ Attacker stays low-trust indefinitely
→ System self-protects

---

# Interpretation

Validates:

• social realism of trust
• power of asymmetry
• long-term resilience against betrayal

---

# Next Steps

• Adaptive adversaries against irreversible decay
• Reputation irreversibility tuning
• Multi-node betrayal coordination
