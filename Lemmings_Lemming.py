from Lemmings_Case import*

class Lemming:
    #Constructeur
    def __init__(self,ligne,colonne,jeu):
        self.ligne = ligne
        self.colonne = colonne
        self.jeu = jeu
        self.direction = 1
        self.compteur = 0

    #Méthode
    def __str__(self):
        """Renvoie ">" ou "<" selon la direction du lemming"""
        if self.compteur >= 5:
            return "X"
        else:
            if self.direction == 1:
                return ">"
            if self.direction == 2:
                return "v"
            if self.direction == 3:
                return "^"
            if self.direction == -1:
                return "<"
            if self.direction == -2:
                return "v"
            if self.direction == -3:
                return "^"

    def action(self):
        """La méthode action déplace le lemming en fonction des cases libres autour lui"""
        if self.jeu.grotte[self.ligne-1][self.colonne].libre() == 2 :
            self.jeu.grotte[self.ligne][self.colonne].depart()
            self.ligne=self.ligne-1
            if self.direction == 1:
                self.direction = 3
            elif self.direction ==-1:
                self.direction ==-3
            self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
            self.compteur = 0
        elif self.jeu.grotte[self.ligne+1][self.colonne].libre() == 1 :
            self.jeu.grotte[self.ligne][self.colonne].depart()
            self.ligne=self.ligne+1
            if self.direction == 1:
                self.direction = 2
            elif self.direction ==-1:
                self.direction =-2
            self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
            self.compteur = 0
        elif self.direction == 1 or self.direction == 2 or self.direction == 3:
            if self.jeu.grotte[self.ligne][self.colonne+1].libre() == 1 :
                self.jeu.grotte[self.ligne][self.colonne].depart()
                self.colonne=self.colonne+1
                self.direction = 1
                self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
            else:
                self.direction = -1
                self.compteur = self.compteur + 1
                if self.__str__() == "X":
                    self.sort()
                    self.jeu.nb_morts+=1
        elif self.direction == -1 or self.direction == -2 or self.direction == -3:
            if self.jeu.grotte[self.ligne][self.colonne-1].libre() == 1 :
                self.jeu.grotte[self.ligne][self.colonne].depart()
                self.colonne=self.colonne-1
                self.direction = -1
                self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
                self.compteur = 0
            else :
                self.direction = 1
                self.compteur = self.compteur + 1
                if self.__str__() == "X":
                    self.sort()
                    self.jeu.nb_morts+=1

    def sort(self):
        """Retire le lemming du jeu."""
        self.jeu.lemmings.remove(self)

