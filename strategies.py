# Une stratégie = une classe avec jouer(mes_coups, coups_adv, rng) qui renvoie "C" ou "D"
# reset() est appelé avant chaque partie.

class Strategie:
    nom = "?"

    def reset(self):
        pass

    def jouer(self, mes_coups, coups_adv, rng):
        raise NotImplementedError


class AllD(Strategie):
    """Toujours D."""
    nom = "ALL-D"

    def jouer(self, mes_coups, coups_adv, rng):
        return "D"


class TitForTat(Strategie):
    """C au premier tour, puis copie le coup précédent de l'adversaire."""
    nom = "TIT-FOR-TAT"

    def jouer(self, mes_coups, coups_adv, rng):
        if not coups_adv:
            return "C"
        return coups_adv[-1]


class Random(Strategie):
    """C ou D au hasard, une chance sur deux."""
    nom = "RANDOM"

    def jouer(self, mes_coups, coups_adv, rng):
        return rng.choice(["C", "D"])


class Tester(Strategie):
    """D au premier tour. Si l'adversaire a déjà joué D, joue TFT, sinon répète C, C, D."""
    nom = "TESTER"

    def jouer(self, mes_coups, coups_adv, rng):
        if not mes_coups:
            return "D"
        if "D" in coups_adv:
            return coups_adv[-1]
        # cycle C, C, D à partir du tour 2
        if (len(mes_coups) - 1) % 3 == 2:
            return "D"
        return "C"


class Joss(TitForTat):
    """TIT-FOR-TAT, mais remplace C par D une fois sur dix."""
    nom = "JOSS"

    def jouer(self, mes_coups, coups_adv, rng):
        coup = super().jouer(mes_coups, coups_adv, rng)
        if coup == "C" and rng.random() < 0.1:
            return "D"
        return coup