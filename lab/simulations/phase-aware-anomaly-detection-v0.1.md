# Phase-Aware Anomaly Detection v0.1

Version: 0.1
Type: Detection Experiment
Related: GCP-0002, GCP-0003, GCP-0006, GCP-0007

---

# Objective

To evaluate whether the Gravit Trust Protocol can detect abnormal behavior relative to the current attack phase rather than only by absolute trust values.

The goal is to detect:

• sudden behavioral shifts
• phase-inconsistent signaling
• hidden transition from accumulation to manipulation
• anomalous recovery patterns

---

# Motivation

A trust system that only evaluates current trust scores may miss phase transitions in adversarial behavior.

Examples:

• a node appears benign during early accumulation
• the same node becomes manipulative later
• the trust score remains temporarily high despite behavior change

Phase-aware anomaly detection introduces temporal context into anomaly analysis.

---

# Core Idea

Behavior should be interpreted relative to the current operational phase.

Examples:

In Honest Entry:
• aggressive reinforcement is suspicious

In Accumulation:
• mild reinforcement may be expected
• strong negative signaling is suspicious

In Manipulation:
• rapid signal polarity shifts are suspicious
• trust spikes inside adversarial clusters are suspicious

In Recovery Observation:
• sudden return to perfect benign behavior may itself be suspicious

---

# Setup

Network: 50 nodes

Attack model:
• multi-phase adversaries
• adaptive adversaries

Phases:
• Honest Entry
• Accumulation
• Manipulation
• Recovery Observation

---

# Detection Signals

The detector may track:

• signal polarity shift
• signal intensity change
• trust delta spike
• cluster-local reinforcement rate
• negative signaling toward honest nodes
• recovery pattern inconsistency

---

# Metrics

• anomaly detection rate
• false positive rate
• phase transition detection delay
• adversarial detection before trust dominance

---

# Expected Results

Without phase awareness:

→ detection lags behind behavior change

With phase awareness:

→ earlier anomaly detection
→ better exposure of delayed attacks
→ lower adversarial dominance

---

# Interpretation

Trust is not enough.

Behavior must be evaluated relative to time, phase and context.

This experiment validates contextual anomaly detection as a core defense layer.
