from random import*
from Lemmings_Lemming import *
from Lemmings_Case import *
from time import*

class Jeu:
    #Constructeur
    def __init__(self,carte):
        self.grotte=[[Case(terrain,self) for terrain in ligne if terrain!='\n'] for ligne in carte.readlines()]
        self.lemmings=[]
        self.nb_entres = 0
        self.nb_sortis = 0
        self.nb_morts = 0
    #Methode
    def affiche(self):
        """Affiche la grotte avec les lemmings dedans."""
        for ligne in self.grotte:
            for colonne in ligne:
                print (str(colonne),end="")
            print()

    def tour(self):
        """Affiche l'état du jeu puis les fait agir chaque lemming une fois."""
        self.affiche()
        for l in self.lemmings:
            l.action()

    def demarre(self):
        """Demande indéfiniment à l'utilisateur d'entrée une commande."""
        while True:
            i=input("l : ajouter un lemming et jouer un tour \nentrée : Jouer un tour \nq : Quitter \nr : Relancer \nx : effectue le nombre de tours que vous aurez choisis \na : fait des tours automatiquement jusqu'à ce que tous les lemmings rentrés dans la grotte soit sortis ou morts")
            assert i=='q' or i=='l' or i=='' or i=='x 'or i=='a' or i=='r'
            if i=='q':
                print(str(self.nb_entres)+" lemmings sont entrés dans la grotte, "+str(self.nb_sortis)+" en sont sortis. Mais "+str(self.nb_morts)+" sont morts avant d'avoir atteint la sortie.")
                break
            elif i=='l':
                self.nb_entres+=1
                self.lemmings.append(Lemming(0,1,self))
                self.grotte[0][1].lemming=Lemming(0,1,self)
                self.tour()
            elif i=='':
                self.tour()
            elif i=='x':
                n=int(input("Veuille saisir le nombre de tour à effectuer : "))
                for i in range (n):
                    self.tour()
                    sleep(1)
            elif i=='a':
                while self.nb_entres!=self.nb_sortis+self.nb_morts:
                    self.tour()
                    sleep(1)
                    print(str(self.nb_entres)+" lemmings sont entrés dans la grotte, "+str(self.nb_sortis)+" en sont sortis et "+str(self.nb_morts)+" sont morts avant d'avoir atteint la sortie.")
                break
            elif i=='r':
                print(str(self.nb_entres)+" lemmings sont entrés dans la grotte, "+str(self.nb_sortis)+" en sont sortis et "+str(self.nb_morts)+" sont morts avant d'avoir atteint la sortie.")
                carte = None
                self.nb_entres = 0
                self.nb_sortis = 0
                self.nb_morts = 0
                b=False
                while b==False:
                    q = int(input("Veuillez entrer un chiffre entre 1 et 4 pour choisir la carte du jeu ou 0 pour une carte aléatoire :"))
                    if q == 0:
                        r=randint(1,4)
                        if r==1:
                            carte=open('Map1.txt')
                        elif r==2:
                            carte=open('Map2.txt')
                        elif r==3:
                            carte=open('Map3.txt')
                        elif r==4:
                            carte=open('Map4.txt')
                    if q==1:
                        carte=open('Map1.txt')
                    if q==2:
                        carte=open('Map2.txt')
                    if q==3:
                        carte=open('Map3.txt')
                    if q==4:
                        carte=open('Map4.txt')
                    a=Jeu(carte)
                    a.affiche()
                    i=input("Souhaitez-vous jouer sur cette carte? Y : oui / N : non")
                    if i=="y":
                        b=True
                a.demarre()
                break
b=False
while b==False:
    q = int(input("Veuillez entrer un chiffre entre 1 et 4 pour choisir la carte du jeu ou 0 pour une carte aléatoire: "))
    if q==0:
        r=randint(1,4)
        if r==1:
            carte=open('Map1.txt')
        elif r==2:
            carte=open('Map2.txt')
        elif r==3:
            carte=open('Map3.txt')
        elif r==4:
            carte=open('Map4.txt')
    if q==1:
        carte=open('Map1.txt')
    if q==2:
        carte=open('Map2.txt')
    if q==3:
        carte=open('Map3.txt')
    if q==4:
        carte=open('Map4.txt')
    a=Jeu(carte)
    a.affiche()
    i=input("Souhaitez-vous jouer sur cette carte? Y : oui / N : non")
    if i=="y":
        b=True
a.demarre()







