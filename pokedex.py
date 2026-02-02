import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Pokédex Lucas")
fenetre.geometry("600x600")


class Pokemon:
    def __init__(self, name, level, type, attacks,region, evolution ):
        self.name=name
        self.level=level
        self.type=type
        self.attacks=attacks
        self.region=region
        self.evolution=evolution

    def afficher_infos(poke):
        label_name.config(text=f"Nom : {poke.name} ")
        label_level.config(text=f"Nom : {poke.level} ")
        label_type.config(text=f"Nom : {poke.type} ")
        label_atk.config(text=f"Nom : {poke.attacks} ")
        label_region.config(text=f"Nom : {poke.region} ")
        label_evolution.config(text=f"Nom : {poke.evolution} ")

    def fill_pokedex():
        for poke in Pokemon:
            list_pokemon.insert(poke.name)


#__________________________________________________ Methodes HORS Classe ____________________________________________________________

pokedex= []

pikachu= Pokemon("pikachu",10,"Electric", "Lightning", "kanto", 2)

Pokemon.fill_pokedex()

def add_pokemon():
    name_add=entry_name.get()
    lvl_add=entry_level.get()
    type_add=entry_type.get()
    region_add=entry_region.get()
    evo_add=entry_evolution.get()
    atk_add=entry_atk.get()
    
    poke= Pokemon(name_add,lvl_add,type_add,atk_add,region_add,evo_add)

    cacher_widgets()


def afficher_widget():
    label_entry_name.pack()
    entry_name.pack()
    
    label_entry_level.pack()
    entry_level.pack()
    
    label_entry_type.pack()
    entry_type.pack()
    
    label_entry_evo.pack()
    entry_evolution.pack()
   
    label_entry_atk.pack()
    entry_atk.pack()
    
    label_entry_region.pack()
    entry_region.pack()
    
    button_confirm_add.pack()
    
def cacher_widgets(): 
    
    label_entry_name.pack_forget()
    entry_name.pack_forget()
    
    label_entry_level.pack_forget()
    entry_level.pack_forget()
    
    label_entry_type.pack_forget()
    entry_type.pack_forget()
    
    label_entry_evo.pack_forget()
    entry_evolution.pack_forget()
   
    label_entry_atk.pack_forget()
    entry_atk.pack_forget()
    
    label_entry_region.pack_forget()
    entry_region.pack_forget()
    
    button_confirm_add.pack_forget()
    
    
    
   
# _________________________________________________ Labels d'information des pokemons _______________________________________________

label_name=tk.Label(fenetre, text="Nom :")
label_name.pack()

label_level=tk.Label(fenetre, text="Niveau :")
label_level.pack()

label_type=tk.Label(fenetre, text="Types :")
label_type.pack()

label_atk=tk.Label(fenetre, text="Attaques :")
label_atk.pack()

label_region=tk.Label(fenetre, text="Région :")
label_region.pack()

label_evolution=tk.Label(fenetre, text="Stade d'évolution :")
label_evolution.pack()

#_________________________________________________ Composants interface ______________________________________________________________
list_pokemon=tk.Listbox(fenetre)
list_pokemon.pack()


button_add_poke=tk.Button(fenetre,text="Ajouter un Pokemon", command=afficher_widget)
button_add_poke.pack()

#__________________________________________________ Ajout d'un pokemon _______________________________________________________________

label_entry_name=tk.Label(fenetre,text="Nom :")
label_entry_name.pack_forget()
entry_name=tk.Entry(fenetre)
entry_name.pack_forget()

label_entry_level=tk.Label(fenetre,text="Niveau :")
label_entry_level.pack_forget()
entry_level=tk.Entry(fenetre)
entry_level.pack_forget()

label_entry_type=tk.Label(fenetre,text="Type :")
label_entry_type.pack_forget()
entry_type=tk.Entry(fenetre)
entry_type.pack_forget()

label_entry_region=tk.Label(fenetre,text="Region :")
label_entry_region.pack_forget()
entry_region=tk.Entry(fenetre)
entry_region.pack_forget()

label_entry_atk=tk.Label(fenetre,text="Attaques :")
label_entry_atk.pack_forget()
entry_atk=tk.Entry(fenetre)
entry_atk.pack_forget()

label_entry_evo=tk.Label(fenetre,text="Stade Evolution :")
label_entry_evo.pack_forget()
entry_evolution=tk.Entry(fenetre)
entry_evolution.pack_forget()


button_confirm_add=tk.Button(fenetre, text="Ajouter le Pokémon", command=add_pokemon)
button_confirm_add.pack_forget()







fenetre.mainloop()