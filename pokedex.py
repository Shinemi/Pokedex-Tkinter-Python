import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Exercice 32")
fenetre.geometry("400x300")


class Pokemon:
    def __init__(self, nom, niveau, type, attaque,region, evolution ):
        self.nom=nom
        self.niveau=niveau
        self.type=type
        self.attaque=attaque
        self.region=region
        self.evolution=evolution


fenetre.mainloop()