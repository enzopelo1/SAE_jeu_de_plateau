import tkinter as tk
import math
import random
from tkinter import Label


class Personnage:
    def __init__(self, canvas, x, y, taille, couleur, joueur_numero, largeur_ecran, hauteur_ecran):
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

        # Ajout une étiquette de titre pour le joueur
        self.titre_label = Label(
            canvas, text=f"Stats Joueur {joueur_numero}", fg="white", bg="black")

        # Ajout des étiquettes pour la vie, le shield et le bouclier
        self.vie_label = Label(
            canvas, text=f"Vie: {self.vie}", fg="white", bg="black")
        self.shield_label = Label(
            canvas, text=f"Shield: {self.shield}", fg="white", bg="black")
        self.force_label = Label(
            canvas, text=f"Force: {self.force}", fg="white", bg="black")
        self.joueur_numero = joueur_numero

        # Placement les étiquettes de statistiques en fonction du coin de l'écran
        if joueur_numero == 1:
            self.titre_label.place(x=10, y=10)
            self.vie_label.place(x=10, y=30)
            self.shield_label.place(x=10, y=50)
            self.force_label.place(x=10, y=70)
        elif joueur_numero == 2:
            self.titre_label.place(x=largeur_ecran - 100, y=10)
            self.vie_label.place(x=largeur_ecran - 68, y=30)
            self.shield_label.place(x=largeur_ecran - 78, y=50)
            self.force_label.place(x=largeur_ecran - 75, y=70)
        elif joueur_numero == 3:
            self.titre_label.place(x=10, y=hauteur_ecran - 110)
            self.vie_label.place(x=10, y=hauteur_ecran - 90)
            self.shield_label.place(x=10, y=hauteur_ecran - 70)
            self.force_label.place(x=10, y=hauteur_ecran - 50)
        elif joueur_numero == 4:
            self.titre_label.place(x=largeur_ecran - 100,
                                   y=hauteur_ecran - 110)
            self.vie_label.place(x=largeur_ecran - 68, y=hauteur_ecran - 90)
            self.shield_label.place(x=largeur_ecran - 78, y=hauteur_ecran - 70)
            self.force_label.place(x=largeur_ecran - 75, y=hauteur_ecran - 50)

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
        if joueur_actuel == self.joueur_numero:
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
        # Changement de joueur après un déplacement réussi
        global joueur_actuel
        joueur_actuel = (joueur_actuel % 4) + 1  # Passe au joueur suivant

        # Mettez à jour l'interface utilisateur pour afficher le joueur en cours
        mettre_a_jour_joueur_en_cours()

    def collision(self, new_x, new_y):
        '''Fonction qui vérifie si un personnage se trouve sur un carré occupé par un autre personnage'''
        for personnage in liste_personnages:
            if personnage != self:  # Ignore le personnage lui-même
                if (new_x >= personnage.x and new_x < personnage.x + personnage.taille and
                        new_y >= personnage.y and new_y < personnage.y + personnage.taille):
                    return True
        return False

    def mettre_a_jour_vie(self, nouvelle_vie):
        '''Fonction qui met à jour la vie du personnage'''
        self.vie = nouvelle_vie
        self.vie_label.config(text=f"Vie: {self.vie}")

    def mettre_a_jour_shield(self, nouveau_shield):
        '''Fonction qui met à jour le shield du personnage'''
        self.shield = nouveau_shield
        self.shield_label.config(text=f"Shield: {self.shield}")

    def mettre_a_jour_force(self, nouvelle_force):
        '''Fonction qui met à jour la force du personnage'''
        self.force = nouvelle_force
        self.force_label.config(text=f"Force: {self.force}")


def mettre_a_jour_joueur_en_cours():
    # Récupérez la couleur correspondant au joueur en cours
    joueur_en_cours = liste_personnages[joueur_actuel - 1]
    couleur_joueur_en_cours = joueur_en_cours.couleur

    # Mettez à jour l'interface utilisateur pour indiquer le joueur en cours avec la couleur
    joueur_label.config(
        text=f"Joueur en cours : Joueur {joueur_actuel}", fg=couleur_joueur_en_cours)


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


def creer_personnage(joueur_numero, largeur_ecran, hauteur_ecran):
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

    # Création du personnage avec le numéro du joueur et les dimensions de l'écran
    personnage = Personnage(canvas, x, y, taille_carré,
                            couleur, joueur_numero, largeur_ecran, hauteur_ecran)

    # Ajoutez l'attribut joueur_numero au personnage
    personnage.joueur_numero = joueur_numero

    liste_personnages.append(personnage)


if __name__ == '__main__':

    # Création d'une fenêtre tkinter
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

    # Création d'une liste de dictionnaires pour stocker les informations de chaque carré
    informations_carrés = []

    creation_plateau()

    joueur_actuel = 1

    # Récupération des informations de chaque carré
    for index, info in enumerate(informations_carrés):
        print(
            f"Carré {index + 1}: x={info['x']}, y={info['y']}, taille={info['taille']}")

    # Liste des coordonnées spécifiques
    coordonnees_specifiques = [(889, 313), (609, 33), (329, 313), (609, 593)]
    couleurs_disponibles = ["red", "blue", "green", "yellow"]
    liste_personnages = []

    # Création des personnages
    for joueur_numero in range(1, 5):
        creer_personnage(joueur_numero, largeur_ecran, hauteur_ecran)

    # test de vie
    personnage_a_mettre_a_jour = liste_personnages[3]

    personnage_a_mettre_a_jour.mettre_a_jour_vie(
        personnage_a_mettre_a_jour.vie - 20)

    # Ajoutez cette ligne après avoir créé la fenêtre tkinter
    joueur_label = Label(canvas, text="", fg="white", bg="black")
    joueur_label.place(x=largeur_ecran/2.3, y=10)
    mettre_a_jour_joueur_en_cours()  # Affiche le joueur initial

    # Démarrage la boucle principale Tkinter
    fenetre_plateau.mainloop()
