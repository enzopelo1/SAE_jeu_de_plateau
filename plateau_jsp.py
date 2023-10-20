import tkinter as tk
import math


class Personnage:
    def __init__(self, canvas, x, y, taille, couleur):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.taille = taille
        self.couleur = couleur
        self.rectangle = self.canvas.create_rectangle(
            x, y, x + taille, y + taille, fill=couleur)
        # Initialisation de la variable cercle_deplacement à None
        self.cercle_deplacement = None

        self.informations_carrés = informations_carrés
        # Associer un gestionnaire d'événement de clic à ce personnage
        self.canvas.tag_bind(self.rectangle, '<Button-1>',
                             self.clic_personnage)
        # Les déplacements possibles
        self.deplacements_possibles = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def est_dans_le_plateau(self, x, y):
        for info in informations_carrés:
            if (x >= info['x'] and x < info['x'] + info['taille'] and
                    y >= info['y'] and y < info['y'] + info['taille']):
                return True
        return False

    def afficher_deplacement_temporaire(self, dx, dy):
        cercles_temporaires = []
        # Le rayon est la moitié de la taille du carré
        rayon_deplacement = self.taille / 2
        x_centre = self.x + self.taille / 2 + dx * self.taille
        y_centre = self.y + self.taille / 2 + dy * self.taille

        if self.est_dans_le_plateau(x_centre, y_centre):
            cercle = self.canvas.create_oval(
                x_centre - rayon_deplacement, y_centre - rayon_deplacement,
                x_centre + rayon_deplacement, y_centre + rayon_deplacement,
                outline="black", dash=(4, 4))  # Créer le cercle temporaire
            cercles_temporaires.append((cercle, dx, dy))

        return cercles_temporaires

    def clic_personnage(self, event):
        # Lorsqu'un personnage est cliqué, afficher les cercles de déplacement temporaire
        # pour toutes les directions possibles
        cercles_temporaires = []
        for dx, dy in self.deplacements_possibles:
            cercles_temporaires.extend(
                self.afficher_deplacement_temporaire(dx, dy))

        # Stocker les cercles temporaires dans l'instance pour pouvoir les supprimer ultérieurement
        self.cercles_deplacement = cercles_temporaires

        # Créer des gestionnaires d'événement de clic pour chaque cercle temporaire
        for cercle, dx, dy in cercles_temporaires:
            self.canvas.tag_bind(
                cercle, '<Button-1>', lambda event, dx=dx, dy=dy: self.deplacer(dx, dy))

    def supprimer_deplacement_temporaire(self):
        if self.cercles_deplacement:
            for cercle, _, _ in self.cercles_deplacement:
                self.canvas.delete(cercle)
            self.cercles_deplacement = []

    def deplacer(self, dx, dy):
        # Supprimer les cercles temporaires lors du déplacement
        self.supprimer_deplacement_temporaire()

        # Déplacer le personnage
        self.canvas.move(self.rectangle, dx * self.taille, dy * self.taille)
        self.x += dx
        self.y += dy

# Fonction pour créer un carré à l'intérieur du plateau


def creer_carre(x, y, taille):
    canvas.create_rectangle(x, y, x + taille, y + taille, fill="white")

# Fonction pour obtenir les informations d'un carré sous forme de dictionnaire


def obtenir_info_carre(x, y, taille):
    return {
        "x": x,
        "y": y,
        "taille": taille
    }


# Créer une fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Jeu de plateau")

# Obtenir la résolution de l'écran
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

# Définir la taille de la fenêtre pour qu'elle soit en plein écran
fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}")

# création d'un canva pour le plateau de jeu
canvas = tk.Canvas(fenetre, width=largeur_ecran, height=hauteur_ecran,
                   bg="black", borderwidth=0, highlightthickness=0)
canvas.pack()

taille_carré = 40  # taille du carré
rayon = 7  # Le nombre de carrés du bord jusqu'au centre

# Créer une liste de dictionnaires pour stocker les informations de chaque carré
informations_carrés = []


def creation_plateau():
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


creation_plateau()


# Récupérer les informations de chaque carré
for index, info in enumerate(informations_carrés):
    print(
        f"Carré {index + 1}: x={info['x']}, y={info['y']}, taille={info['taille']}")

# Création des personnages
personnage1 = Personnage(canvas, 849, 313, taille_carré, "red")
personnage2 = Personnage(canvas, 609, 33, taille_carré, "blue")
personnage3 = Personnage(canvas, 329, 313, taille_carré, "green")
personnage4 = Personnage(canvas, 609, 593, taille_carré, "yellow")

# Exemple d'affichage du cercle de déplacement temporaire pour le personnage 1
# dx = -1  # Déplacement horizontal
# dy = 0  # Déplacement vertical
# personnage1.afficher_deplacement_temporaire(dx, dy)


# Démarrer la boucle principale Tkinter
fenetre.mainloop()
