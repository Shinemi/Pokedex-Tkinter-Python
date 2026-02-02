import tkinter as tk
from tkinter import messagebox

frame = tk.Tk()
frame.title("Pokédex Lucas")
frame.geometry("600x600")


class Pokemon:
    def __init__(self, name, level, type, attacks,region, evolution ):
        self.name=name
        self.level=level
        self.type=type
        self.attacks=attacks
        self.region=region
        self.evolution=evolution

    def show_infos(self):
        label_name.config(text=f"Nom : {self.name} ")
        label_level.config(text=f"Nom : {self.level} ")
        label_type.config(text=f"Nom : {self.type} ")
        label_atk.config(text=f"Nom : {self.attacks} ")
        label_region.config(text=f"Nom : {self.region} ")
        label_evolution.config(text=f"Nom : {self.evolution} ")




#__________________________________________________ Methodes HORS Classe ____________________________________________________________

pokedex= []


def select_list(event):
    selection = list_pokemon.curselection()
    if selection:
        index = selection[0]
        pokedex[index].show_infos()

def fill_pokedex(pokedex):
    list_pokemon.delete(0, tk.END)
    for poke in pokedex:
        list_pokemon.insert(tk.END, poke.name)


def add_pokemon():
    name_add=entry_name.get()
    lvl_add=entry_level.get()
    type_add=entry_type.get()
    region_add=entry_region.get()
    evo_add=entry_evolution.get()
    atk_add=entry_atk.get()
    
    poke= Pokemon(name_add,lvl_add,type_add,atk_add,region_add,evo_add)
    pokedex.append(poke)
    fill_pokedex(pokedex)
    hide_widgets()






def show_widget():
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
    
def hide_widgets(): 
    
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

label_name=tk.Label(frame, text="Nom :")
label_name.pack()

label_level=tk.Label(frame, text="Niveau :")
label_level.pack()

label_type=tk.Label(frame, text="Types :")
label_type.pack()

label_atk=tk.Label(frame, text="Attaques :")
label_atk.pack()

label_region=tk.Label(frame, text="Région :")
label_region.pack()

label_evolution=tk.Label(frame, text="Stade d'évolution :")
label_evolution.pack()

#_________________________________________________ Composants interface ______________________________________________________________
list_pokemon=tk.Listbox(frame)
list_pokemon.pack()
list_pokemon.bind("<<ListboxSelect>>", select_list)


button_add_poke=tk.Button(frame,text="Ajouter un Pokemon", command=show_widget)
button_add_poke.pack()

#__________________________________________________ Ajout d'un pokemon _______________________________________________________________

label_entry_name=tk.Label(frame,text="Nom :")
label_entry_name.pack_forget()
entry_name=tk.Entry(frame)
entry_name.pack_forget()

label_entry_level=tk.Label(frame,text="Niveau :")
label_entry_level.pack_forget()
entry_level=tk.Entry(frame)
entry_level.pack_forget()

label_entry_type=tk.Label(frame,text="Type :")
label_entry_type.pack_forget()
entry_type=tk.Entry(frame)
entry_type.pack_forget()

label_entry_region=tk.Label(frame,text="Region :")
label_entry_region.pack_forget()
entry_region=tk.Entry(frame)
entry_region.pack_forget()

label_entry_atk=tk.Label(frame,text="Attaques :")
label_entry_atk.pack_forget()
entry_atk=tk.Entry(frame)
entry_atk.pack_forget()

label_entry_evo=tk.Label(frame,text="Stade Evolution :")
label_entry_evo.pack_forget()
entry_evolution=tk.Entry(frame)
entry_evolution.pack_forget()


button_confirm_add=tk.Button(frame, text="Ajouter le Pokémon", command=add_pokemon)
button_confirm_add.pack_forget()




poke= Pokemon("pikachu",10,"Electric", "Lightning", "kanto", 2)
pokedex.append(poke)
fill_pokedex(pokedex)


frame.mainloop()