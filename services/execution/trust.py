AGENTS = {}

def update_trust(actor_id, decision):
    score = AGENTS.get(actor_id, 0.5)

    if decision == "ALLOW":
        score += 0.05
    if decision == "DENY":
        score -= 0.1

    score = max(0, min(1, score))
    AGENTS[actor_id] = score

    return score
