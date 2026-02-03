import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


frame = tk.Tk()
frame.title("Pokédex Lucas")
frame.geometry("500x800")



class Pokemon:
    def __init__(self, name, level, type, attacks,region, evolution, image ):
        self.name=name
        self.level=level
        self.type=type
        self.attacks=attacks
        self.region=region
        self.evolution=evolution
        self.image=image

    def show_infos(self):
        label_name.config(text=f"Nom : {self.name} ")
        label_name.grid(row=0, column=1, sticky="w", padx=10)
        
        label_level.config(text=f"Niveau : {self.level} ")
        label_level.grid(row=1, column=1, sticky="w", padx=10)
        
        types_txt = " / ".join(self.type)
        label_type.config(text=f"Types : {types_txt}")
        label_type.grid(row=2, column=1, sticky="w", padx=10)
            
        attaques = " / ".join(self.attacks)
        label_atk.config(text=f"Attaques : {attaques}")
        label_atk.grid(row=3, column=1, sticky="w", padx=10)
       
        label_region.config(text=f"Région : {self.region} ")
        label_region.grid(row=4, column=1, sticky="w", padx=10)
       
        label_evolution.config(text=f"Evolution : {self.evolution} ")
        label_evolution.grid(row=5, column=1, sticky="w", padx=10)

        show_image(self.image)
        




#__________________________________________________ Methodes HORS Classe ____________________________________________________________

pokedex= []

def load_save():
    with open("save_file.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")

            poke = Pokemon(
                name=data[0],
                level=data[1],
                type=data[2].split(",") if data[2] else [],
                attacks=data[3].split(",") if data[3] else [],
                region=data[4],
                evolution=data[5],
                image=data[6]
            )

            pokedex.append(poke)


def save_pokedex(pokedex):
    with open("save_file.txt", "w", encoding="utf-8") as save_file:
        for poke in pokedex:
            line = (f"{poke.name}|{poke.level}|{','.join(poke.type)}|{','.join(poke.attacks)}|{poke.region}|{poke.evolution}|{poke.image}\n")
            save_file.write(line)

def show_image(link):
    global pokemon_img
    img = Image.open(link)
    img = img.resize((200, 200))
    pokemon_img = ImageTk.PhotoImage(img)
    label_image.config(image=pokemon_img)

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
    attacks = [
    entry_atk1.get(),
    entry_atk2.get(),
    entry_atk3.get(),
    entry_atk4.get()
    ]

    types = [
    entry_type1.get(),
    entry_type2.get()
    ]

    pokeName=entry_name.get()


    name_add=entry_name.get()
    lvl_add=entry_level.get()
    type_add=types
    region_add=entry_region.get()
    evo_add=entry_evolution.get()
    atk_add=attacks
    image_add=f"./pokemon-img/{pokeName}.png"

    if not name_add:
        messagebox.showerror("Erreur", "Le nom du Pokémon est obligatoire")
        return
    elif not lvl_add.isdigit():
        messagebox.showerror("Erreur", "Le niveau doit être un nombre")
        return
    elif not region_add:
        messagebox.showerror("Erreur", "La région du Pokémon est obligatoire")
        return
    elif len(types) == 0:
        messagebox.showerror("Erreur", "Au moins un type est requis")
        return
    elif len(attacks) == 0:
        messagebox.showerror("Erreur", "Au moins une attaque est requise")
        return
    else:
        poke= Pokemon(name_add,lvl_add,type_add,atk_add,region_add,evo_add,image_add)
        pokedex.append(poke)
        fill_pokedex(pokedex)
        save_pokedex(pokedex)
        hide_widgets()
    
    
def delete_pokemon():
    selection = list_pokemon.curselection()
    
    if not selection:
        messagebox.showwarning("Attention", "Aucun Pokémon sélectionné")
        return
    
    index = selection[0]
    
    del pokedex[index]
    save_pokedex(pokedex)
    fill_pokedex(pokedex)


def show_widget():
    label_entry_name.grid(row=8, column=0, sticky="e", padx=10)
    entry_name.grid(row=8, column=1, sticky="w", padx=10)
    
    label_entry_level.grid(row=9, column=0, sticky="e", padx=10)
    entry_level.grid(row=9, column=1, sticky="w", padx=10)
    
    label_entry_type1.grid(row=10, column=0, sticky="e", padx=10)
    entry_type1.grid(row=10, column=1, sticky="w", padx=10)

    label_entry_type2.grid(row=11, column=0, sticky="e", padx=10)
    entry_type2.grid(row=11, column=1, sticky="w", padx=10)
    
    label_entry_evo.grid(row=12, column=0, sticky="e", padx=10)
    entry_evolution.grid(row=12, column=1, sticky="w", padx=10)
   
    label_entry_atk1.grid(row=13, column=0, sticky="e", padx=10)
    entry_atk1.grid(row=13, column=1, sticky="w", padx=10)

    label_entry_atk2.grid(row=14, column=0, sticky="e", padx=10)
    entry_atk2.grid(row=14, column=1, sticky="w", padx=10)

    label_entry_atk3.grid(row=15, column=0, sticky="e", padx=10)
    entry_atk3.grid(row=15, column=1, sticky="w", padx=10)

    label_entry_atk4.grid(row=16, column=0, sticky="e", padx=10)
    entry_atk4.grid(row=16, column=1, sticky="w", padx=10)
        
    label_entry_region.grid(row=17, column=0, sticky="e", padx=10)
    entry_region.grid(row=17,column=1, sticky="w", padx=10)
    
    button_confirm_add.grid(row=19, column=0, columnspan=2, pady=15)
    
def hide_widgets(): 
    
    label_entry_name.grid_forget()
    entry_name.grid_forget()
    
    label_entry_level.grid_forget()
    entry_level.grid_forget()
    
    label_entry_type1.grid_forget()
    entry_type1.grid_forget()
    label_entry_type2.grid_forget()
    entry_type2.grid_forget()
    
    label_entry_evo.grid_forget()
    entry_evolution.grid_forget()
   
    label_entry_atk1.grid_forget()
    entry_atk1.grid_forget()
    label_entry_atk2.grid_forget()
    entry_atk2.grid_forget()
    label_entry_atk3.grid_forget()
    entry_atk3.grid_forget()
    label_entry_atk4.grid_forget()
    entry_atk4.grid_forget()
    
    label_entry_region.grid_forget()
    entry_region.grid_forget()

    button_confirm_add.grid_forget()
    
    
    
   
# _________________________________________________ Labels d'information des pokemons _______________________________________________

label_image = tk.Label(frame)
label_image.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

label_name=tk.Label(frame, text="Nom :")
label_name.grid_forget()

label_level=tk.Label(frame, text="Niveau :")
label_level.grid_forget()

label_type=tk.Label(frame, text="Types :")
label_type.grid_forget()

label_atk=tk.Label(frame, text="Attaques :")
label_atk.grid_forget()

label_region=tk.Label(frame, text="Région :")
label_region.grid_forget()

label_evolution=tk.Label(frame, text="Stade d'évolution :")
label_evolution.grid_forget()

#_________________________________________________ Composants interface ______________________________________________________________

list_pokemon=tk.Listbox(frame, bg="red", fg="white")
list_pokemon.grid(row=6, column=0, columnspan=2,sticky="ew", pady=10)
list_pokemon.bind("<<ListboxSelect>>", select_list)


button_del_poke=tk.Button(frame,text="Supprimer le Pokemon sélectionné", command=delete_pokemon, bg="black", fg="red")
button_del_poke.grid(row=20, column=0, columnspan=2,sticky="ew", pady=5)

button_add_poke=tk.Button(frame,text="Ajouter un Pokemon", command=show_widget, bg="red", fg="white")
button_add_poke.grid(row=7, column=0, columnspan=2,sticky="ew", pady=5)
#__________________________________________________ Ajout d'un pokemon _______________________________________________________________

label_entry_name=tk.Label(frame,text="Nom :")
label_entry_name.grid_forget()
entry_name=tk.Entry(frame)
entry_name.grid_forget()

label_entry_level=tk.Label(frame,text="Niveau :")
label_entry_level.grid_forget()
entry_level=tk.Entry(frame)
entry_level.grid_forget()

label_entry_type1 = tk.Label(frame, text="Type 1 :")
label_entry_type1.grid_forget()
entry_type1 = tk.Entry(frame)
entry_type1.grid_forget()

label_entry_type2 = tk.Label(frame, text="Type 2 :")
label_entry_type2.grid_forget()
entry_type2 = tk.Entry(frame)
entry_type2.grid_forget()

label_entry_region=tk.Label(frame,text="Region :")
label_entry_region.grid_forget()
entry_region=tk.Entry(frame)
entry_region.grid_forget()

label_entry_atk1 = tk.Label(frame, text="Attaque 1 :")
label_entry_atk1.grid_forget()
entry_atk1 = tk.Entry(frame)
entry_atk1.grid_forget()

label_entry_atk2 = tk.Label(frame, text="Attaque 2 :")
label_entry_atk2.grid_forget()
entry_atk2 = tk.Entry(frame)
entry_atk2.grid_forget()

label_entry_atk3 = tk.Label(frame, text="Attaque 3 :")
label_entry_atk3.grid_forget()
entry_atk3 = tk.Entry(frame)
entry_atk3.grid_forget()

label_entry_atk4 = tk.Label(frame, text="Attaque 4 :")
label_entry_atk4.grid_forget()
entry_atk4 = tk.Entry(frame)
entry_atk4.grid_forget()

label_entry_evo=tk.Label(frame,text="Stade Evolution :")
label_entry_evo.grid_forget()
entry_evolution=tk.Entry(frame)
entry_evolution.grid_forget()

button_confirm_add=tk.Button(frame, text="Confirmer", command=add_pokemon, background="red", fg="white")
button_confirm_add.grid_forget()




load_save()
fill_pokedex(pokedex)

frame.mainloop()




#Ameliorer appel d'image (preparer le chemin d'acces en fonction du nom) / modifier / supprimer