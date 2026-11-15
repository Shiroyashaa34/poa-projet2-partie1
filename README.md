# HAI716I - Projet 2 (partie 1) : tournoi d'Axelrod modifié

BENENES Nassim

Tournoi de dilemme du prisonnier itéré (moteur + stratégies), en Python sans bibliothèque externe.
 
Le journal de bord est dans `journal.md`, les captures dans `captures/`.
 
## Prérequis
 
Python 3. Toutes les commandes se lancent depuis la racine du dépôt.
 
## Relancer les tournois
 
La graine est fixée à 42 : chaque commande redonne exactement les mêmes scores.
 
| Tournoi | Commande |
|---|---|
| Test du moteur (exemple du cours, 18 / 23) | `python test_moteur.py` |
| Étape 1 : les 5 stratégies du cours | `python etape1.py` |
| Étape 1 : détail des scores match par match | `python detail_etape1.py` |
| Étape 1 sans RANDOM | dans `etape1.py`, décommenter la ligne sans RANDOM, puis `python etape1.py` |
| Étape 2 : + GRIM et PAVLOV | `python etape2.py` |
| Étape 2 : détail match par match | `python detail_etape2.py` |
| Étape 3 : bruit à 5 % | `python etape3_bruit.py` |
| Étape 3 : bruit, détail match par match | `python detail_etape3_bruit.py` |
| Étape 3 : horizon inconnu (continuation 0,995) | `python etape3_horizon.py` |
| Étape 3 : horizon, détail match par match | `python detail_etape3_horizon.py` |
 
## Fichiers
 
- `moteur.py` : matrice de gains, `partie()` et `tournoi()`, avec les options `bruit` et `continuation`
- `strategies.py` : une classe par stratégie (ALL-D, TIT-FOR-TAT, RANDOM, TESTER, JOSS, GRIM, PAVLOV)