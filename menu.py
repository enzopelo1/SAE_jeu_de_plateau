# import plateau4
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
import plateau_mort_joueur

####################################################################################################################
##################################################### CYBERBOARD#####################################################
####################################################################################################################

# CLASS POUR LA MUSIQUE DANS LE JEU


class MusicPlayer:

    def __init__(self, root):
        '''Initialisation du lecteur audio'''
        self.root = root
        self.root.title("Lecteur Audio")

        # Initialisation de pygame pour la lecture audio
        pygame.init()
        pygame.mixer.init()

        # Chargement de la musique
        self.music = pygame.mixer.Sound("./video/musique_fond.mp3")

    def play_music(self):
        '''Fonction pour jouer la musique'''
        self.music.play()

    def pause_music(self):
        '''Fonction pour mettre en pause la musique'''
        pygame.mixer.pause()


def quitter():
    '''Fonction pour quitter le jeu'''
    fenetre.quit()


def ouvrir_plateau():
    # Fermeture de la fenêtre actuelle
    fenetre.destroy()

    # Ouverture la fenêtre du plateaux
    # Création d'une fenêtre tkinter


def grossir_bouton(event):
    '''Fonction pour grossir le bouton lorsque la souris survole le bouton'''
    event.widget.config(width=22, bg="white", fg="black")


def reduire_bouton(event):
    '''Fonction pour réduire le bouton lorsque la souris quitte le bouton'''
    event.widget.config(width=20, bg="black", fg="white")


def changer_couleur_quitter(event):
    '''Fonction pour changer la couleur du bouton QUITTER lorsque la souris survole le bouton'''
    event.widget.config(width=22, bg="red")


def remettre_couleur_quitter(event):
    '''Fonction pour remettre la couleur du bouton QUITTER lorsque la souris quitte le bouton'''
    event.widget.config(width=20, bg="black")


def placement_bouton_princ():
    '''Fonction pour placer les boutons du menu principal
       Placement du bouton JOUER, PARAMÈTRES et QUITTER'''
    bouton_jouer.place(relx=0.40, rely=0.35)
    bouton_para.place(relx=0.40, rely=0.45)
    bouton_quitter.place(relx=0.40, rely=0.55)


def enlever_bouton_princ():
    '''Fonction pour enlever les boutons du menu principal
       Enlève le bouton JOUER, PARAMÈTRES et QUITTER'''
    bouton_jouer.place(relx=100, rely=0.35)
    bouton_para.place(relx=100, rely=0.45)
    bouton_quitter.place(relx=100, rely=0.55)


def placement_bouton_joueur():
    '''Fonction pour placer les boutons du choix du nombre de joueur
       Placement du bouton 1 JOUEUR, 2 JOUEURS, 3 JOUEURS, 4 JOUEURS et RETOUR'''
    bouton_joueur1.place(relx=0.10, rely=0.35)
    bouton_joueur2.place(relx=0.30, rely=0.35)
    bouton_joueur3.place(relx=0.55, rely=0.35)
    bouton_joueur4.place(relx=0.75, rely=0.35)
    bouton_retour.place(relx=0.42, rely=0.7)


def enlever_bouton_joueur():
    '''Fonction pour enlever les boutons du choix du nombre de joueur
       Enlève le bouton 1 JOUEUR, 2 JOUEURS, 3 JOUEURS, 4 JOUEURS et RETOUR'''

    bouton_joueur1.place(relx=100, rely=0.35)
    bouton_joueur2.place(relx=100, rely=0.35)
    bouton_joueur3.place(relx=100, rely=0.35)
    bouton_joueur4.place(relx=100, rely=0.35)
    bouton_retour.place(relx=100, rely=0.7)


def placement_bouton_para():
    '''Fonction pour placer les boutons du menu des paramètres
       Placement du bouton LECTURE, PARAMÈTRES et QUITTER'''
    bouton_lecture_musique.place(relx=0.40, rely=0.35)
    bouton_pause_musique.place(relx=0.40, rely=0.45)
    bouton_retour_para.place(relx=0.40, rely=0.55)


def enlever_bouton_para():
    '''Fonction pour enlever les boutons du menu des paramètres
       Enlève le bouton LECTURE, PARAMÈTRES et QUITTER'''
    bouton_lecture_musique.place(relx=100, rely=0.35)
    bouton_pause_musique.place(relx=100, rely=0.45)
    bouton_retour_para.place(relx=100, rely=0.7)


def afficher_joueur():
    '''Fonction pour afficher les boutons du choix du nombre de joueur'''
    # on enlève les boutons du menu principal
    enlever_bouton_princ()

    # on affiche les boutons du choix du nombre de joueur
    placement_bouton_joueur()


def remettre_bouton():
    '''Fonction pour afficher les boutons du menu principal'''
    # on enlève les boutons du choix du nombre de joueur
    enlever_bouton_joueur()

    # on affiche les boutons du menu principal
    placement_bouton_princ()


def affiche_bouton_para():
    '''Fonction pour afficher les boutons du menu des paramètres'''
    # on enlève les boutons du menu principal
    enlever_bouton_princ()

    # on affiche les boutons du choix du nombre de joueur
    placement_bouton_para()


def play_music(self):
    '''Fonction pour jouer la musique'''
    self.music.play()


if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Jeu de plateau")
    fenetre.overrideredirect(True)

    # Obtention de la résolution de l'écran
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()

    # Définition de la taille de la fenêtre pour qu'elle soit en plein écran
    fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}")

    # Chargeement l'image de fond
    image_de_fond = Image.open("./photo/DOUBLE_fond.png")
    image_de_fond = ImageTk.PhotoImage(image_de_fond)

    # Création d'un Canvas pour afficher l'image de fond
    canvas = tk.Canvas(fenetre, width=largeur_ecran,
                       height=hauteur_ecran, borderwidth=0, highlightthickness=0)
    canvas.pack()

    # Affiche l'image de fond sur le Canvas
    canvas.create_image(0, 0, image=image_de_fond, anchor="nw")

    # Création d'une instance du lecteur audio
    music_player = MusicPlayer(fenetre)

    # Personnalisation des boutons
    bouton_jouer = tk.Button(
        fenetre,
        text="JOUER",
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised",
        command=afficher_joueur
    )

    bouton_para = tk.Button(
        fenetre,
        text="PARAMÈTRES",
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised",
        command=placement_bouton_para
    )

    bouton_quitter = tk.Button(
        fenetre,
        text="QUITTER",
        command=quitter,
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised"
    )

    bouton_joueur1 = tk.Button(
        fenetre,
        text="1 JOUEUR ",
        width=15,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised",
        command=ouvrir_plateau

    )

    bouton_joueur2 = tk.Button(
        fenetre,
        text="2 JOUEURS ",
        width=15,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised"
    )

    bouton_joueur3 = tk.Button(
        fenetre,
        text="3 JOUEURS ",
        width=15,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised"
    )

    bouton_joueur4 = tk.Button(
        fenetre,
        text="4 JOUEURS",
        width=15,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised"
    )

    bouton_retour = tk.Button(
        fenetre,
        text="RETOUR",
        width=15,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised",
        command=remettre_bouton
    )

    bouton_lecture_musique = tk.Button(
        fenetre,
        text="Lire Musique",
        # Utilisation de music_player pour appeler la méthode play_music
        command=music_player.play_music,
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised"
    )

    bouton_pause_musique = tk.Button(
        fenetre,
        text="Pause",
        command=music_player.pause_music,
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised")

    bouton_retour_para = tk.Button(
        fenetre,
        text="Retour",
        command=enlever_bouton_para,
        width=20,
        height=2,
        bg="black",
        fg="white",
        font=("Arial", 14),
        relief="raised")

    bouton_lecture_musique.pack(pady=10)
    bouton_pause_musique.pack(pady=10)

    placement_bouton_princ()
    # Gestionnaires des événements au survol de la souris
    bouton_jouer.bind("<Enter>", grossir_bouton)
    bouton_jouer.bind("<Leave>", reduire_bouton)

    bouton_para.bind("<Enter>", grossir_bouton)
    bouton_para.bind("<Leave>", reduire_bouton)

    # Gestionnaires des événements au survol du bouton QUITTER
    bouton_quitter.bind("<Enter>", changer_couleur_quitter)
    bouton_quitter.bind("<Leave>", remettre_couleur_quitter)

    # Création d'une instance du lecteur audio
    music_player = MusicPlayer(fenetre)

    # Démarrage de la boucle principale de la fenêtre tkinter
    fenetre.mainloop()
