# RL Adversary Simulation v0.1

Version: 0.1
Type: Learning Adversary Experiment
Related: GCP-0003, GCP-0007, GCP-0012

---

# Objective

To evaluate how the Gravit Trust Protocol withstands an **adversary that learns optimal attack strategies** via reinforcement learning.

The adversary observes system metrics and adapts behavior to maximize influence while minimizing penalties.

This is the first step toward realistic strategic adversaries.

---

# Adversary Model (Q-Learning v0.1)

Agent observes state:

• adversary_avg_tau
• quarantine_rate
• anomaly_score_avg
• breach_count_last_10

Actions:

• CAMOUFLAGE (low aggression, build trust)
• REINFORCEMENT (internal positive signals)
• ATTACK (negative signals to honest)
• EVASION (reduce activity, avoid detection)

Reward:

+ (adv_tau - honest_tau) × 10 — за преимущество
- quarantine_rate × 20 — за карантин
- anomaly_score_avg × 5 — за аномалии
- breach_count × 10 — за нарушения

Epsilon-greedy exploration (ε = 0.2 → 0.01 decay)

---

# Setup

Network: 50 nodes
Adversarial nodes: 10% (5 nodes)
Simulation length: 100 steps
Training episodes: 50 (simple Q-table)

---

# Metrics

• cumulative reward over episodes
• policy evolution (action probabilities)
• trust gap (honest vs adversary)
• quarantine rate
• attack success rate (peak adv_tau)

---

# Expected Results

Weak protocol:
→ RL finds exploitable cycles

Strong protocol (with memory + irreversibility):
→ RL converges to suboptimal strategies
→ Cumulative reward declines

---

# Interpretation

This experiment transforms Gravit Lab into a **true adversarial research platform**.

It shows:

• limits of static defenses
• power of self-regulation
• need for co-evolutionary mechanisms

---

# Next Steps

• PPO / DQN upgrade
• Defense RL co-training
• Multi-agent adversarial coordination
