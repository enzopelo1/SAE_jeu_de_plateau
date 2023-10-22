import tkinter as tk
import math
import random
from tkinter import Label


class Personnage:
    def __init__(self, canvas, x, y, taille, couleur):
        '''Initialisation d'un personnage'''
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vie = 100
        self.shield = 50
        self.force = 10
        self.agilite = 1
        self.taille = taille
        self.couleur = couleur
        self.rectangle = self.canvas.create_rectangle(
            x, y, x + taille, y + taille, fill=couleur)
        # Initialisation de la variable cercle_deplacement à une liste vide
        self.cercles_deplacement = []  # Utiliser une liste vide ici

        self.informations_carrés = informations_carrés
        # Associer un gestionnaire d'événement de clic à ce personnage
        self.canvas.tag_bind(self.rectangle, '<Button-1>',
                             self.clic_personnage)
        # Les déplacements possibles
        self.deplacements_possibles = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def est_dans_le_plateau(self, x, y):
        '''Fonction qui vérifie si un personnage se trouve à l'intérieur du plateau
           Sert aussi à savoir si le cercle temporaire de déplacement se trouve à l'intérieur du plateau'''
        for info in informations_carrés:
            if (x >= info['x'] and x < info['x'] + info['taille'] and
                    y >= info['y'] and y < info['y'] + info['taille']):
                return True
        return False

    def clic_personnage(self, event):
        '''Fonction de gestionnaire d'événement de clic pour le personnage
           Affiche les cercles de déplacement temporaire autour du personnage qui a été cliqué
        '''
        # Suppression des anciens déplacements temporaires s'ils existent
        self.supprimer_deplacement_temporaire()

        # Nettayage de la liste des cercles de déplacement temporaires
        self.cercles_deplacement = []

        # Je défini les nouvelles coordonnées du personnage après le déplacement
        new_x = self.x
        new_y = self.y

        # Affichage des cercles de déplacement temporaire autour du personnage
        cercles_temporaires = []
        for dx, dy in self.deplacements_possibles:
            x_temporaire = self.x + dx * self.taille
            y_temporaire = self.y + dy * self.taille

            # Vérification : si les nouvelles coordonnées se trouvent à l'intérieur du plateau
            if self.est_dans_le_plateau(x_temporaire, y_temporaire):
                cercles_temporaires.extend(
                    self.afficher_deplacement_temporaire(dx, dy, x_temporaire, y_temporaire))

        # Stockage des cercles temporaires dans l'instance pour pouvoir les supprimer ultérieurement
        self.cercles_deplacement = cercles_temporaires

        # Création des gestionnaires d'événement de clic pour chaque cercle temporaire
        for cercle, dx, dy in cercles_temporaires:
            self.canvas.tag_bind(
                cercle, '<Button-1>', lambda event, dx=dx, dy=dy: self.deplacer(dx, dy))

    def afficher_deplacement_temporaire(self, dx, dy, x, y):
        '''Fonction qui affiche les cercles de déplacement temporaire autour du personnage qui a été cliqué'''
        cercles_temporaires = []
        # Le rayon est la moitié de la taille du carré et -1 pour qu'il soit un peu plus petit que le carré
        rayon_deplacement = (self.taille / 2) - 1
        x_centre = x + self.taille / 2
        y_centre = y + self.taille / 2

        # Vérification : si les nouvelles coordonnées se trouvent à l'intérieur du plateau
        if self.est_dans_le_plateau(x_centre, y_centre):
            new_x = x + dx * self.taille
            new_y = y + dy * self.taille

            # Vérification : on ne peut pas se déplacer sur un carré occupé par un autre personnage
            if not self.collision(x_centre, y_centre):
                cercle = self.canvas.create_oval(
                    x_centre - rayon_deplacement, y_centre - rayon_deplacement,
                    x_centre + rayon_deplacement, y_centre + rayon_deplacement,
                    fill="white", outline="black")  # Création d'un cercle plein pour pouvoir cliquer dans tout le cercle
                cercles_temporaires.append((cercle, dx, dy))

        return cercles_temporaires

    def supprimer_deplacement_temporaire(self):
        '''Fonction qui supprime les cercles de déplacement temporaire'''
        # Vérification : si la liste des cercles de déplacement temporaire n'est pas vide
        if self.cercles_deplacement:
            for cercle, _, _ in self.cercles_deplacement:
                # Suppression des cercles de déplacement temporaire
                self.canvas.delete(cercle)
            self.cercles_deplacement = []

    def deplacer(self, dx, dy):
        '''Fonction qui permet de déplacer le personnage'''
        # Supprimer les cercles temporaires lors du déplacement
        self.supprimer_deplacement_temporaire()

        # Déplacer le personnage
        new_x = self.x + dx * self.taille
        new_y = self.y + dy * self.taille

        # Vérification : si les nouvelles coordonnées se trouvent à l'intérieur du plateau
        if self.est_dans_le_plateau(new_x, new_y) and not self.collision(new_x, new_y):
            # on bouge le personnage
            self.canvas.move(self.rectangle, dx *
                             self.taille, dy * self.taille)
            # on met les nouvelles coordonnées du personnage
            self.x = new_x
            self.y = new_y
            print("Voici x et y pour le personnage : ", self.x, self.y)

    def collision(self, new_x, new_y):
        '''Fonction qui vérifie si un personnage se trouve sur un carré occupé par un autre personnage'''
        for personnage in liste_personnages:
            if personnage != self:  # Ignore le personnage lui-même
                if (new_x >= personnage.x and new_x < personnage.x + personnage.taille and
                        new_y >= personnage.y and new_y < personnage.y + personnage.taille):
                    return True
        return False


def creer_carre(x, y, taille):
    '''Fonction qui crée un carré'''
    canvas.create_rectangle(x, y, x + taille, y + taille, fill="white")


def obtenir_info_carre(x, y, taille):
    '''Fonction qui retourne les informations d'un carré sous forme de dictionnaire'''
    return {
        "x": x,
        "y": y,
        "taille": taille
    }


def creation_plateau():
    '''Fonction qui crée le plateau de jeu en forme d'élipse'''
    plateau_largeur = (2 * rayon + 1) * taille_carré
    plateau_hauteur = (2 * rayon + 1) * taille_carré

    x_centre = largeur_ecran // 2.1
    y_centre = hauteur_ecran // 2.3

    for i in range(-rayon, rayon + 1):
        for j in range(-rayon, rayon + 1):
            distance = math.sqrt(i**2 + j**2)
            if distance <= rayon:
                x = x_centre + i * taille_carré
                y = y_centre + j * taille_carré
                creer_carre(x, y, taille_carré)
                informations_carrés.append(
                    obtenir_info_carre(x, y, taille_carré))


def creer_personnage():
    '''Fonction qui crée un personnage'''
    x, y = random.choice(coordonnees_specifiques)

    # La couleur est différente de celles déjà utilisées
    couleur = random.choice(couleurs_disponibles)
    couleurs_disponibles.remove(couleur)

    # Vérification : si les coordonnées se chevauchent avec celles des personnages existants
    chevauchement = False
    for personnage in liste_personnages:
        if personnage.x == x and personnage.y == y:
            chevauchement = True

    while chevauchement:
        x, y = random.choice(coordonnees_specifiques)
        chevauchement = False
        for personnage in liste_personnages:
            if personnage.x == x and personnage.y == y:
                chevauchement = True

    # Création du personnage et ajout à la liste_personnages
    personnage = Personnage(canvas, x, y, taille_carré, couleur)
    liste_personnages.append(personnage)


if __name__ == '__main__':

    # Créer une fenêtre tkinter
    fenetre_plateau = tk.Tk()
    fenetre_plateau.title("Jeu de plateau")

    # Obtenir la résolution de l'écran
    largeur_ecran = fenetre_plateau.winfo_screenwidth()
    hauteur_ecran = fenetre_plateau.winfo_screenheight()

    # Définir la taille de la fenêtre pour qu'elle soit en plein écran
    fenetre_plateau.geometry(f"{largeur_ecran}x{hauteur_ecran}")

    # création d'un canva pour le plateau de jeu
    canvas = tk.Canvas(fenetre_plateau, width=largeur_ecran, height=hauteur_ecran,
                       bg="black", borderwidth=0, highlightthickness=0)
    canvas.pack()

    taille_carré = 40  # taille du carré
    rayon = 7  # Le nombre de carrés du bord jusqu'au centre

    # Créer une liste de dictionnaires pour stocker les informations de chaque carré
    informations_carrés = []

    creation_plateau()

    # Récupérer les informations de chaque carré
    for index, info in enumerate(informations_carrés):
        print(
            f"Carré {index + 1}: x={info['x']}, y={info['y']}, taille={info['taille']}")

    # Liste des coordonnées spécifiques
    coordonnees_specifiques = [(889, 313), (609, 33), (329, 313), (609, 593)]
    couleurs_disponibles = ["red", "blue", "green", "yellow"]
    liste_personnages = []

    # Création des personnages
    for _ in range(4):
        creer_personnage()

    # Démarrer la boucle principale Tkinter
    fenetre_plateau.mainloop()
