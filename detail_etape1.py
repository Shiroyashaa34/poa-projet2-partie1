# Détail du tournoi de l'étape 1 : score de chaque stratégie contre chaque autre.
# Même ordre de matchs et même graine que tournoi(), donc mêmes scores.
import random
from itertools import combinations

from moteur import partie
from strategies import AllD, Random, TitForTat, Tester, Joss

strategies = [AllD(), Random(), TitForTat(), Tester(), Joss()]
rng = random.Random(42)

detail = {}
for s1, s2 in combinations(strategies, 2):
    total1 = total2 = 0
    for _ in range(5):
        g1, g2 = partie(s1, s2, 200, rng)
        total1 += g1
        total2 += g2
    detail[(s1.nom, s2.nom)] = total1
    detail[(s2.nom, s1.nom)] = total2

noms = [s.nom for s in strategies]
print(f"{'':<13}" + "".join(f"{n:>13}" for n in noms))
for a in noms:
    ligne = f"{a:<13}"
    for b in noms:
        ligne += f"{'-' if a == b else detail[(a, b)]:>13}"
    print(ligne)