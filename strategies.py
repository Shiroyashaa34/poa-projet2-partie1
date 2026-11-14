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