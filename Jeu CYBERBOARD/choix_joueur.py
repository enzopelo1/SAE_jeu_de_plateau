import tkinter as tk
from PIL import Image, ImageTk
import json


# Crée une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Sélection de personnages")

# Obtient la résolution de l'écran
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()
fenetre.overrideredirect(True)

# Définit la taille de la fenêtre en fonction de la résolution de l'écran
fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}")

# Définit la couleur de fond de la fenêtre en noir
fenetre.configure(bg="black")

# Liste des images de personnages
personnages = [
    "personnage/Gaia.png",
    "personnage/Even.png",
    "personnage/Raven.png",
    "personnage/Phoenix.png",
    "personnage/Kyre.png",
    "personnage/Altea.png",
    "personnage/Ash.png",
]

# Liste des noms de personnages correspondants
noms_personnages = [
    "Gaia",
    "Even",
    "Raven",
    "Phoenix",
    "Kyre",
    "Altea",
    "Ash",
]

# Liste des joueurs
joueurs = ["Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4"]
indice_joueur = 0  # Indice du joueur actuel

# variable pour enregistrer le personnage choisi par chaque joueur
personnages_selectionnes = {}

# Redimensionne les images à une taille fixe
largeur_image = 200  # Changement de la largeur souhaitée
hauteur_image = 300  # Changement la hauteur souhaitée


def choisir_personnage(image_path):
    '''Fonction appelée lorsqu'un joueur clique sur une image de personnage'''
    global indice_joueur

    # Enregistre le personnage choisi pour le joueur actuel
    personnages_selectionnes[joueurs[indice_joueur]] = image_path

    # Incrémente l'indice du joueur
    indice_joueur += 1

    # Si tous les joueurs ont choisi un personnage, ferme la fenêtre
    if indice_joueur >= len(joueurs):
        fenetre.destroy()
    else:
        # Affiche le nom du joueur actuel
        label_nom_joueur.config(
            text=f"{joueurs[indice_joueur]}, choisissez un personnage :")


# Affiche le nom du joueur actuel qui doit choisir un personnage
label_nom_joueur = tk.Label(
    fenetre, text=f"{joueurs[indice_joueur]}, choisissez un personnage :", bg="black", fg="white", font=("Arial", 16))
label_nom_joueur.pack(pady=20)

# Création d'un cadre pour centrer les images au milieu de l'écran
cadre_images = tk.Frame(fenetre, bg="black")
cadre_images.pack(expand=True, fill="both")

# Création d'une grille pour organiser les images
grille_images = tk.Frame(cadre_images, bg="black")
grille_images.pack()

# Affiche les images des personnages et associe le clic à la fonction de choix
for i, image_path in enumerate(personnages):
    img = Image.open(image_path)
    img_redimensionnee = img.resize(
        (largeur_image, hauteur_image), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img_redimensionnee)
    label_image = tk.Label(grille_images, image=img_tk, cursor="hand2")
    label_image.image = img_tk
    label_image.grid(row=i // 4, column=i % 4, padx=10, pady=10)
    label_image.bind("<Button-1>", lambda event,
                     image_path=image_path: choisir_personnage(image_path))


# Lance la boucle principale de l'interface Tkinter
fenetre.mainloop()

# Une fois que tous les joueurs ont choisi leurs personnages, affiche les choix
for joueur, personnage in personnages_selectionnes.items():
    print(
        f"{joueur} a choisi {noms_personnages[personnages.index(personnage)]}.")

# Crée un dictionnaire pour stocker les choix des joueurs
choix_joueurs = {}

# Enregistre les personnages choisis dans le dictionnaire
for joueur, personnage in personnages_selectionnes.items():
    choix_joueurs[joueur] = personnage

# Enregistre le dictionnaire dans un fichier JSON
with open("choix_joueurs.json", "w") as fichier:
    json.dump(choix_joueurs, fichier)
