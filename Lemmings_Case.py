from Lemmings_Lemming import*

class Case:

    def __init__(self, terrain,jeu):
        self.terrain = terrain
        self.lemming = None
        self.jeu = jeu

    def __str__(self):
        """Affiche le contenu de la case."""
        if self.lemming is not None:
            return(str(self.lemming))
        else:
            return(self.terrain)

    def libre(self):
        """Vérifie si la case donnée est libre."""
        if self.lemming == None and self.terrain == " " or self.terrain =="O":
            return 1
        if self.lemming == None and self.terrain == "_":
            return 2
        else:
            return 0

    def depart(self):
        """Retire le lemming de la case."""
        self.lemming = None

    def arrivee(self, lem):
        """Place le lemming sur sa nouvelle case."""
        if self.terrain=="O":
            lem.sort()
            self.jeu.nb_sortis+=1
        else:
            self.lemming = lem


