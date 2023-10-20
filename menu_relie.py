import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import pygame
from tkinter import ttk, font as tkFont


class Menu:
    def __init__(self):
        '''Initialisation de la fenêtre du menu'''
        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu de plateau")
        self.fenetre.overrideredirect(True)

        # Obtention de la résolution de l'écran
        self.largeur_ecran = self.fenetre.winfo_screenwidth()
        self.hauteur_ecran = self.fenetre.winfo_screenheight()

        # Définition de la taille de la fenêtre pour qu'elle soit en plein écran
        self.fenetre.geometry(f"{self.largeur_ecran}x{self.hauteur_ecran}")

        # Chargement de l'image de fond
        self.image_de_fond = Image.open("./photo/DOUBLE_fond.png")
        self.image_de_fond = ImageTk.PhotoImage(self.image_de_fond)

        # Création d'un Canvas pour afficher l'image de fond
        self.canvas = tk.Canvas(self.fenetre, width=self.largeur_ecran,
                                height=self.hauteur_ecran, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        # Affichage de l'image de fond sur le Canvas
        self.canvas.create_image(0, 0, image=self.image_de_fond, anchor="nw")

        # Création d'une instance du lecteur audio
        self.music_player = MusicPlayer(self.fenetre)

        # Personnalisation des boutons
        self.bouton_jouer = self.create_button("JOUER", self.afficher_joueur)
        self.bouton_jouer.config(font=("photo\Cyborg_Punk.ttf", 14))
        self.bouton_para = self.create_button(
            "PARAMÈTRES", self.placement_bouton_para)
        self.bouton_quitter = self.create_button("QUITTER", self.quitter)
        self.bouton_joueur1 = self.create_button(
            "1 JOUEUR", self.placeholder_function)
        self.bouton_joueur2 = self.create_button(
            "2 JOUEURS", self.placeholder_function)
        self.bouton_joueur3 = self.create_button(
            "3 JOUEURS", self.placeholder_function)
        self.bouton_joueur4 = self.create_button(
            "4 JOUEURS", self.placeholder_function)
        self.bouton_retour = self.create_button("RETOUR", self.remettre_bouton)
        self.bouton_sauvegarde = self.create_button(
            "Sauvegardes", self.placeholder_function)
        self.bouton_lecture_musique = self.create_button(
            "Lire Musique", self.music_player.play_music)
        self.bouton_pause_musique = self.create_button(
            "Pause", self.music_player.pause_music)
        self.bouton_retour_para = self.create_button(
            "Retour", self.enlever_bouton_para)
        self.label_credit = tk.Label(
            self.fenetre, text="Crédit", font=("Arial", 12))
        self.texte_credit = tk.Text(self.fenetre, font=("Arial", 12))
        # Insertion du texte des crédits
        self.texte_credit.insert(
            "1.0", "Crédits du jeu CYBERBOARD: \n\nL'image de RAVEN à été faite par : @isongeoff sur pinterest,\nL'image de ASH à été faite par : @R4Y4N69 sur pinterest, \nToutes les autres images ont été généré par une IA qui s'appelle léonardo\nLa musique est une musique libre de droit.")

        self.bouton_lecture_musique.pack(pady=10)
        self.bouton_pause_musique.pack(pady=10)
        self.placement_bouton_princ()

        # Gestionnaires des événements au survol de la souris
        self.bouton_jouer.bind("<Enter>", self.grossir_bouton)
        self.bouton_jouer.bind("<Leave>", self.reduire_bouton)
        self.bouton_para.bind("<Enter>", self.grossir_bouton)
        self.bouton_para.bind("<Leave>", self.reduire_bouton)

        # Gestionnaires des événements au survol du bouton QUITTER
        self.bouton_quitter.bind("<Enter>", self.changer_couleur_quitter)
        self.bouton_quitter.bind("<Leave>", self.remettre_couleur_quitter)

        # Lier le clic sur le texte "Crédit"
        self.label_credit.bind("<Button-1>", self.basculer_credit)

        self.credit_visible = False  # Variable pour suivre l'état d'affichage des crédits

        self.label_regles = tk.Label(
            self.fenetre, text="Règles du jeu", font=("Arial", 12))
        self.label_regles.bind("<Button-1>", self.basculer_regles)
        self.label_regles.place(relx=0.05, rely=0.94)

        self.texte_regles = tk.Text(self.fenetre, font=("Arial", 12))
        self.texte_regles.insert(
            "1.0", "Règles du jeu CYBERBOARD :\n\nChaque personnage apprarait aléatoirement dans les 4 coins du plateau de jeu\nVous devez être le dernier joueur en vie pour pouvoir remporter la partie.\nPour cela vous devrez mettre en place des stratégies défensive ou offensives à vous de choisir.\nIl y a des cases mystères sur le plateau mais gare à vous cela peut être \nsoit positif soit négatif.\nAlors bonne chance à vous et que le meilleur gagne !")

        self.regles_visible = False

    def changer_fond_ecran(self, nom_image):
        '''Fonction pour changer l'image de fond de l'écran'''
        # Supprimer l'ancienne image de fond
        self.canvas.delete(self.image_de_fond)

        # Chargement de la nouvelle image de fond
        nouvelle_image = Image.open(nom_image)
        self.image_de_fond = ImageTk.PhotoImage(nouvelle_image)

        # Afficher la nouvelle image de fond sur le Canvas
        self.canvas.create_image(0, 0, image=self.image_de_fond, anchor="nw")

    def create_button(self, text, command):
        '''Fonction pour créer un bouton'''
        return tk.Button(self.fenetre, text=text, width=20, height=2, bg="black", fg="white", font=("Arial", 14), relief="raised", command=command)

    def quitter(self):
        '''Fonction pour quitter le jeu'''
        self.fenetre.quit()

    def placeholder_function(self):
        '''Fonction pour afficher un message d'erreur lorsque le bouton n'est pas encore implémenté'''
        pass

    def grossir_bouton(self, event):
        '''Fonction pour grossir le bouton lorsque la souris est dessus'''
        event.widget.config(width=22, bg="white", fg="black")

    def reduire_bouton(self, event):
        '''Fonction pour réduire le bouton lorsque la souris n'est plus dessus'''
        event.widget.config(width=20, bg="black", fg="white")

    def changer_couleur_quitter(self, event):
        '''Fonction pour changer la couleur du bouton QUITTER lorsque la souris est dessus'''
        event.widget.config(width=22, bg="red")

    def remettre_couleur_quitter(self, event):
        '''Fonction pour remettre la couleur du bouton QUITTER lorsque la souris n'est plus dessus'''
        event.widget.config(width=20, bg="black")

    def placement_bouton_princ(self):
        '''Fonction pour placer les boutons principaux'''
        self.bouton_jouer.place(relx=0.40, rely=0.35)
        self.bouton_para.place(relx=0.40, rely=0.45)
        self.bouton_quitter.place(relx=0.40, rely=0.55)
        self.label_credit.place(relx=0.9, rely=0.94)

    def enlever_bouton_princ(self):
        '''Fonction pour enlever les boutons principaux'''
        self.bouton_jouer.place(relx=100, rely=0.35)
        self.bouton_para.place(relx=100, rely=0.45)
        self.bouton_quitter.place(relx=100, rely=0.55)
        self.label_credit.place(relx=100, rely=0.95)

    def placement_bouton_joueur(self):
        '''Fonction pour placer les boutons de choix du nombre de joueurs'''
        self.bouton_joueur1.place(relx=0.10, rely=0.35)
        self.bouton_joueur2.place(relx=0.30, rely=0.35)
        self.bouton_joueur3.place(relx=0.55, rely=0.35)
        self.bouton_joueur4.place(relx=0.75, rely=0.35)
        self.bouton_sauvegarde.place(relx=0.42, rely=0.6)
        self.bouton_retour.place(relx=0.42, rely=0.7)

    def enlever_bouton_joueur(self):
        '''Fonction pour enlever les boutons de choix du nombre de joueurs'''
        self.bouton_joueur1.place(relx=100, rely=0.35)
        self.bouton_joueur2.place(relx=100, rely=0.35)
        self.bouton_joueur3.place(relx=100, rely=0.35)
        self.bouton_joueur4.place(relx=100, rely=0.35)
        self.bouton_sauvegarde.place(relx=100, rely=0.6)
        self.bouton_retour.place(relx=100, rely=0.7)

    def placement_bouton_para(self):
        '''Fonction pour placer les boutons du menu paramètres'''
        self.bouton_lecture_musique.place(relx=0.40, rely=0.35)
        self.bouton_pause_musique.place(relx=0.40, rely=0.45)
        self.bouton_retour_para.place(relx=0.40, rely=0.55)

    def enlever_bouton_para(self):
        '''Fonction pour enlever les boutons du menu paramètres'''
        self.bouton_lecture_musique.place(relx=100, rely=0.35)
        self.bouton_pause_musique.place(relx=100, rely=0.45)
        self.bouton_retour_para.place(relx=100, rely=0.7)

    def placement_credit(self):
        self.bouton_retour.place(relx=0.42, rely=0.7)

    def afficher_joueur(self):
        '''Fonction pour afficher les boutons de choix du nombre de joueurs'''
        self.enlever_bouton_princ()
        self.placement_bouton_joueur()

    def remettre_bouton(self):
        '''Fonction pour remettre les boutons principaux'''
        self.enlever_bouton_joueur()
        self.placement_bouton_princ()

    def affiche_bouton_para(self):
        '''Fonction pour afficher les boutons du menu paramètres'''
        self.enlever_bouton_princ()
        self.placement_bouton_para()

    def basculer_credit(self, event):
        '''Fonction pour afficher les crédits du jeu'''
        if self.credit_visible:
            self.texte_credit.place_forget()  # Masquer le texte des crédits
            self.credit_visible = False
            # Revenir à l'image de fond par défaut
            self.changer_fond_ecran("./photo/DOUBLE_fond.png")
            # print("je reviens")
        else:
            self.texte_credit.place(
                relx=0.3, rely=0.1, relwidth=0.4, relheight=0.6)
            self.credit_visible = True
            # Changer l'image de fond
            self.changer_fond_ecran("./photo/DOUBLE_fond_flou.png")
            # print("je change")

    def basculer_regles(self, event):
        '''Fonction pour afficher les règles du jeu'''
        if self.regles_visible:
            self.texte_regles.place_forget()
            self.regles_visible = False
            self.changer_fond_ecran("./photo/DOUBLE_fond.png")
        else:
            self.texte_regles.place(
                relx=0.3, rely=0.1, relwidth=0.4, relheight=0.6)
            self.regles_visible = True
            self.changer_fond_ecran("./photo/DOUBLE_fond_flou.png")

    def play_music(self):
        '''Fonction pour jouer la musique'''
        self.music_player.play_music()

    def run(self):
        '''Fonction pour lancer la boucle principale de l'interface Tkinter'''
        self.fenetre.mainloop()


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


if __name__ == "__main__":
    menu = Menu()
    menu.run()
