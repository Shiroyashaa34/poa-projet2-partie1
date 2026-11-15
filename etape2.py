# Étape 2 : les 5 stratégies du cours + GRIM et PAVLOV.
from moteur import tournoi, afficher_classement
from strategies import AllD, Random, TitForTat, Tester, Joss, Grim, Pavlov

strategies = [AllD(), Random(), TitForTat(), Tester(), Joss(), Grim(), Pavlov()]
scores = tournoi(strategies, nb_parties=5, nb_tours=200, graine=42)
afficher_classement(scores)