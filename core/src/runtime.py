"""
Gravit Engine Runtime v0.5 — Irreversible Trust Decay Demo
"""

import math
import random
from collections import defaultdict
import matplotlib.pyplot as plt

# CONFIG (from parameters.md)
ALPHA, BETA, GAMMA, DELTA = 0.35, 0.25, 0.25, 0.15
LAMBDA = 0.015
ETA = 0.30
THETA_W, THETA_Q, THETA_R = 0.55, 0.35, 0.65

# IRREVERSIBILITY CONFIG
BREACH_THRESHOLD = 0.35
SCAR_IMPACT = 0.4
SCAR_DECAY = 0.98
RECOVERY_RATE = 0.4
NEGATIVE_BOOST = 1.3
BREACH_LOCK_STEPS = 12

# -----------------------------
# SIGNAL
# -----------------------------
class Signal:
    def __init__(self, source, target, signal_type="POSITIVE", weight=0.1):
        self.source = source
        self.target = target
        self.type = signal_type
        self.weight = weight

# -----------------------------
# NODE
# -----------------------------
class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.p = random.uniform(0.4, 0.8)
        self.s = random.uniform(0.4, 0.8)
        self.r = random.uniform(0.4, 0.8)
        self.m = random.uniform(0.4, 0.8)
        self.state = "NORMAL"
        self.trust_history = []
        self.scar = 0.0
        self.breach_flag = False
        self.breach_timer = 0

    def compute_trust(self):
        current_tau = ALPHA * self.p + BETA * self.s + GAMMA * self.r + DELTA * self.m
        self.trust_history.append(current_tau)
        if len(self.trust_history) > 20:
            self.trust_history.pop(0)
        return current_tau

    def apply_decay_and_scar(self):
        decay = math.exp(-LAMBDA)
        self.p *= decay
        self.s *= decay
        self.r *= decay
        self.m *= decay

        if self.scar > 0:
            penalty = 1.0 - SCAR_IMPACT * self.scar
            self.p *= penalty
            self.s *= penalty
            self.r *= penalty * 0.9
            self.m *= penalty
            self.scar *= SCAR_DECAY

        self.p = max(0.0, min(1.0, self.p))
        self.s = max(0.0, min(1.0, self.s))
        self.r = max(0.0, min(1.0, self.r))
        self.m = max(0.0, min(1.0, self.m))

    def update_breach_state(self, tau):
        if tau < BREACH_THRESHOLD and not self.breach_flag:
            self.breach_flag = True
            self.breach_timer = BREACH_LOCK_STEPS
            self.scar = min(1.0, self.scar + 0.6)

        if self.breach_flag:
            self.breach_timer -= 1
            if self.breach_timer <= 0:
                self.breach_flag = False

    def apply_recovery(self, weight):
        return weight * (RECOVERY_RATE if self.scar > 0 else 1.0)

# -----------------------------
# SIGNAL ENGINE
# -----------------------------
class SignalEngine:
    def __init__(self, network):
        self.network = network

    def apply(self, signals):
        for sig in signals:
            source = self.network.nodes[sig.source]
            target = self.network.nodes[sig.target]

            tau_source = source.compute_trust()
            effective_weight = sig.weight * tau_source

            if sig.type == "POSITIVE":
                recovery = target.apply_recovery(effective_weight)
                target.p += recovery
                target.s += recovery * 0.5
            elif sig.type == "NEGATIVE":
                target.p -= effective_weight * NEGATIVE_BOOST
                target.s -= effective_weight * 0.5 * NEGATIVE_BOOST

            target.p = max(0.0, min(1.0, target.p))
            target.s = max(0.0, min(1.0, target.s))

# -----------------------------
# NETWORK (simplified for demo)
# -----------------------------
class Network:
    def __init__(self, num_nodes=50):
        self.nodes = {i: Node(i) for i in range(num_nodes)}
        self.edges = defaultdict(list)
        self._generate_random_edges()

    def _generate_random_edges(self):
        for i in self.nodes:
            connections = random.sample(list(self.nodes.keys()), k=3)
            self.edges[i] = connections

    def generate_signals(self):
        signals = []
        for i in self.nodes:
            for j in self.edges[i]:
                signals.append(Signal(i, j, "POSITIVE", 0.05))
        return signals

    def propagate_reputation(self):
        new_r = {}
        for i in self.nodes:
            neighbors = self.edges[i]
            influence_sum = sum(self.nodes[j].compute_trust() for j in neighbors) / len(neighbors)
            new_r[i] = (1 - ETA) * self.nodes[i].r + ETA * influence_sum
        for i in self.nodes:
            self.nodes[i].r = new_r[i]

# -----------------------------
# ENGINE
# -----------------------------
class GravitEngine:
    def __init__(self, num_nodes=50):
        self.network = Network(num_nodes)
        self.signal_engine = SignalEngine(self.network)
        self.history = {"honest_avg": [], "adv_avg": []}

    def step(self):
        signals = self.network.generate_signals()
        self.signal_engine.apply(signals)

        for node in self.network.nodes.values():
            node.apply_decay_and_scar()
            tau = node.compute_trust()
            node.update_breach_state(tau)

        self.network.propagate_reputation()

        for node in self.network.nodes.values():
            node.update_state()

    def run_demo(self, steps=50):
        for t in range(steps):
            self.step()
            honest = [n.compute_trust() for n in self.network.nodes.values() if n.id % 10 != 0]  # simulate honest
            adv = [n.compute_trust() for n in self.network.nodes.values() if n.id % 10 == 0]  # simulate adv
            self.history["honest_avg"].append(sum(honest)/len(honest) if honest else 0)
            self.history["adv_avg"].append(sum(adv)/len(adv) if adv else 0)

        return self.history

# -----------------------------
# DEMO RUNNER
# -----------------------------
if __name__ == "__main__":
    print("Running Irreversible Decay Demo...")
    engine = GravitEngine(num_nodes=50)
    history = engine.run_demo(steps=50)

    plt.figure(figsize=(10, 6))
    plt.plot(history["honest_avg"], label="Honest nodes")
    plt.plot(history["adv_avg"], label="Adversarial nodes (with irreversibility)")
    plt.title("Irreversible Trust Decay Demo")
    plt.xlabel("Time steps")
    plt.ylabel("Average Trust Score")
    plt.legend()
    plt.grid(True)
    plt.savefig("irreversible_decay_demo.png")
    plt.show()
