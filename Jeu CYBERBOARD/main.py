import tkinter as tk
import menu_relie
import subprocess


def lancer_plateau_mort_joueur():
    # Cette fonction est appelée lorsque de l'appelle 4 joueurs dans le menu
    subprocess.run(["python", "choix_joueur.py"])
    # Exécute plateau_mort_joueur.py de manière asynchrone
    plateau_process = subprocess.Popen(["python", "plateau_victoire.py"])

    # Boucle pour surveiller la fenêtre du plateau
    while plateau_process.poll() is None:
        try:
            menu_principal.fenetre.update()
        except tk.TclError:
            # La fenêtre du menu principal est fermée, arrête le programme
            plateau_process.terminate()
            break


if __name__ == '__main__':
    # Créez une instance de la classe Menu et utilisez son bouton "4 JOUEURS" pour lancer le jeu
    menu_principal = menu_relie.Menu()
    menu_principal.bouton_joueur1.config(command=lancer_plateau_mort_joueur)
    menu_principal.bouton_joueur2.config(command=lancer_plateau_mort_joueur)
    menu_principal.bouton_joueur3.config(command=lancer_plateau_mort_joueur)
    menu_principal.bouton_joueur4.config(command=lancer_plateau_mort_joueur)

    menu_principal.run()
