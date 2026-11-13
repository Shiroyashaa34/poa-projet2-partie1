"""Moteur du tournoi : une partie entre deux stratégies, puis un tournoi tous contre tous."""

import random
from itertools import combinations

# (coup de i, coup de j) -> (gain de i, gain de j)
GAINS = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (2, 2),
}


def partie(s1, s2, nb_tours, rng):
    """Joue une partie de nb_tours entre s1 et s2. Renvoie (score s1, score s2)."""
    s1.reset()
    s2.reset()
    coups1, coups2 = [], []
    score1 = score2 = 0
    for _ in range(nb_tours):
        c1 = s1.jouer(coups1, coups2, rng)
        c2 = s2.jouer(coups2, coups1, rng)
        g1, g2 = GAINS[(c1, c2)]
        score1 += g1
        score2 += g2
        coups1.append(c1)
        coups2.append(c2)
    return score1, score2


def tournoi(strategies, nb_parties=5, nb_tours=200, graine=42):
    """Chaque stratégie affronte chaque autre (sans auto-affrontement).
    Renvoie un dict {nom: score total}."""
    rng = random.Random(graine)
    scores = {s.nom: 0 for s in strategies}
    for s1, s2 in combinations(strategies, 2):
        for _ in range(nb_parties):
            g1, g2 = partie(s1, s2, nb_tours, rng)
            scores[s1.nom] += g1
            scores[s2.nom] += g2
    return scores


def afficher_classement(scores):
    classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for rang, (nom, score) in enumerate(classement, 1):
        print(f"{rang}. {nom:<15} {score}")
