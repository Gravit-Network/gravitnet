# Reputation Tiers v0.1

Version: 0.1
Type: Trust Structure Experiment
Related: GCP-0002, GCP-0004, GCP-0006

---

# Objective

To evaluate whether discrete reputation tiers improve system stability, interpretability and resistance to manipulation.

---

# Motivation

A continuous trust score is useful for computation, but many systems require decision layers.

Examples:

• whether a node may strongly influence others
• whether a node may issue high-impact attestations
• whether a node is under restricted influence

Reputation tiers transform trust into operational classes.

---

# Proposed Tiers

## Tier 0 — Quarantined

Trust too low for meaningful influence.

Properties:

• no propagation influence
• restricted signaling weight
• high monitoring priority

---

## Tier 1 — Restricted

Low trust, limited impact.

Properties:

• reduced signal weight
• reduced propagation impact
• recovery possible but slow

---

## Tier 2 — Standard

Normal operating tier.

Properties:

• normal signal participation
• normal propagation role

---

## Tier 3 — Trusted

High and stable trust.

Properties:

• stronger signal credibility
• higher propagation relevance
• lower suspicion unless behavior changes sharply

---

## Tier 4 — Anchor

Very high and historically stable trust.

Properties:

• strongest signal weighting
• governance relevance may increase
• severe penalties if breach occurs

---

# Tier Boundaries

Suggested example thresholds:

Tier 0: τ < 0.35
Tier 1: 0.35 ≤ τ < 0.55
Tier 2: 0.55 ≤ τ < 0.70
Tier 3: 0.70 ≤ τ < 0.85
Tier 4: τ ≥ 0.85 and stable history

---

# Additional Rule

Tier promotion should depend on:

• current trust
• trust history
• behavior stability
• scar level

This prevents rapid adversarial promotion.

---

# Metrics

• tier distribution over time
• frequency of tier jumps
• adversarial tier penetration
• honest node tier stability

---

# Expected Results

With tiers:

→ easier interpretation
→ stronger policy control
→ reduced adversarial escalation speed

---

# Interpretation

Reputation tiers create a governance-ready layer above raw trust computation.

They make the protocol easier to use, regulate and defend.
