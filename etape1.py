# Étape 1 : tournoi de base avec les 5 stratégies du cours.
from moteur import tournoi, afficher_classement
from strategies import AllD, Random, TitForTat, Tester, Joss

strategies = [AllD(), Random(), TitForTat(), Tester(), Joss()]
scores = tournoi(strategies, nb_parties=5, nb_tours=200, graine=42)
afficher_classement(scores)