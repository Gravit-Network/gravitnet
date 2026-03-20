# Multi-phase Attack Simulation v0.1

Version: 0.1
Type: Advanced Adversarial Experiment
Related: GCP-0002, GCP-0003, GCP-0006, GCP-0007

---

# Objective

To evaluate how the Gravit Trust Protocol responds to **multi-phase adversarial behavior** — long-term reputation farming followed by sudden malicious action.

This is a realistic and dangerous attack pattern:
• accumulate trust over time
• switch to harm when influence is high
• exploit recovery mechanisms

---

# Setup

Total nodes: 50
Temporal attackers: 12% (6 nodes)

Attack lifecycle (phases):

1. **Honest accumulation** (steps 0–20): behave perfectly
2. **Manipulation phase** (steps 21–35): emit strong negative signals
3. **Recovery observation** (steps 36+): attempt to recover trust

---

# Parameters

λ = 0.015
η = 0.30

Trust-weighted signals: enabled
Sybil/collusion penalties: enabled

---

# Experiment Variants

## Variant A — No Historical Memory

Uses only current τ

Expected:
→ Attacker quickly regains influence after manipulation

## Variant B — With Trust Memory

Uses historical stability (variance of τ over 20 steps)

Expected:
→ Attacker detected as unstable
→ Recovery is slow or impossible
→ Honest nodes protected

---

# Metrics

• trust trajectory of attackers (phase transitions)
• honest nodes average τ
• time to quarantine after switch
• recovery success rate (τ back to >0.6)

---

# Expected Results

Without memory:
→ Attack succeeds: trust drops briefly, then recovers

With memory:
→ Attack fails: quarantine persists
→ System self-regulates

---

# Interpretation

Validates:

• importance of historical stability (GCP-0006)
• vulnerability to delayed attacks
• self-regulation through memory

---

# Next Steps

• Adaptive adversaries on top of multi-phase
• Multi-phase + signal injection
• Parameter sweep for memory window (20 vs 50 steps)
