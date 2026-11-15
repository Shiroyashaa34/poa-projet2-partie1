# Étape 3, modification 2 : les 7 stratégies de l'étape 2 avec un horizon inconnu.
# Après chaque tour, la partie continue avec une probabilité de 0,995 (200 tours en moyenne).
from moteur import tournoi, afficher_classement
from strategies import AllD, Random, TitForTat, Tester, Joss, Grim, Pavlov

strategies = [AllD(), Random(), TitForTat(), Tester(), Joss(), Grim(), Pavlov()]
scores = tournoi(strategies, nb_parties=5, graine=42, continuation=0.995)
afficher_classement(scores)