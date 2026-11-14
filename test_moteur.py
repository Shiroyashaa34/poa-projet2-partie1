# Exemple du cours : TFT contre ALL-D sur 10 tours doit donner 18 / 23.

import random

from moteur import partie
from strategies import AllD, TitForTat

score_tft, score_alld = partie(TitForTat(), AllD(), 10, random.Random(42))
print(f"TFT : {score_tft}   ALL-D : {score_alld}")
assert (score_tft, score_alld) == (18, 23), "le moteur ne colle pas au cours"
print("OK : identique à la diapo du cours (18 / 23)")
