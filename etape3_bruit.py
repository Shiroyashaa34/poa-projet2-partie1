# Étape 3, modification 1 : les 7 stratégies de l'étape 2 avec 5 % de bruit.
from moteur import tournoi, afficher_classement
from strategies import AllD, Random, TitForTat, Tester, Joss, Grim, Pavlov

strategies = [AllD(), Random(), TitForTat(), Tester(), Joss(), Grim(), Pavlov()]
scores = tournoi(strategies, nb_parties=5, nb_tours=200, graine=42, bruit=0.05)
afficher_classement(scores)