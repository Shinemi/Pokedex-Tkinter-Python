import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Exercice 32")
fenetre.geometry("600x600")


class Pokemon:
    def __init__(self, nom, niveau, type, attaque,region, evolution ):
        self.nom=nom
        self.niveau=niveau
        self.type=type
        self.attaque=attaque
        self.region=region
        self.evolution=evolution

    def afficher_infos():
        pass

    def fill_pokedex():
        pass


#__________________________________________________ Methodes HORS Classe ____________________________________________________________

def add_pokemon():
    pass

def afficher_widget():
    label_entry_nom.pack()
    entry_nom.pack()
    
    label_entry_niveau.pack()
    entry_niveau.pack()
    
    label_entry_type.pack()
    entry_type.pack()
    
    label_entry_evo.pack()
    entry_evolution.pack()
   
    label_entry_attaque.pack()
    entry_attaque.pack()
    
    label_entry_region.pack()
    entry_region.pack()
    
    bouton_valider_ajout.pack()
    
    
    
    
    
   
# _________________________________________________ Labels d'information des pokemons _______________________________________________

label_nom=tk.Label(fenetre, text="Nom :")
label_nom.pack()

label_niveau=tk.Label(fenetre, text="Niveau :")
label_niveau.pack()

label_type=tk.Label(fenetre, text="Types :")
label_type.pack()

label_attaque=tk.Label(fenetre, text="Attaques :")
label_attaque.pack()

label_region=tk.Label(fenetre, text="Région :")
label_region.pack()

label_evolution=tk.Label(fenetre, text="Stade d'évolution :")
label_evolution.pack()

#_________________________________________________ Composants interface ______________________________________________________________
liste_pokemon=tk.Listbox(fenetre)
liste_pokemon.pack()


bouton_ajouter_poke=tk.Button(fenetre,text="Ajouter un Pokemon", command=afficher_widget)
bouton_ajouter_poke.pack()

#__________________________________________________ Ajout d'un pokemon _______________________________________________________________

label_entry_nom=tk.Label(fenetre,text="Nom :")
label_entry_nom.pack_forget()
entry_nom=tk.Entry(fenetre)
entry_nom.pack_forget()

label_entry_niveau=tk.Label(fenetre,text="Niveau :")
label_entry_niveau.pack_forget()
entry_niveau=tk.Entry(fenetre)
entry_niveau.pack_forget()

label_entry_type=tk.Label(fenetre,text="Type :")
label_entry_type.pack_forget()
entry_type=tk.Entry(fenetre)
entry_type.pack_forget()

label_entry_region=tk.Label(fenetre,text="Region :")
label_entry_region.pack_forget()
entry_region=tk.Entry(fenetre)
entry_region.pack_forget()

label_entry_attaque=tk.Label(fenetre,text="Attaques :")
label_entry_attaque.pack_forget()
entry_attaque=tk.Entry(fenetre)
entry_attaque.pack_forget()

label_entry_evo=tk.Label(fenetre,text="Stade Evolution :")
label_entry_evo.pack_forget()
entry_evolution=tk.Entry(fenetre)
entry_evolution.pack_forget()


bouton_valider_ajout=tk.Button(fenetre, text="Ajouter le Pokémon", command=add_pokemon)
bouton_valider_ajout.pack_forget()







fenetre.mainloop()