import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

frame = tk.Tk()
frame.title("Pokédex Lucas")
frame.geometry("600x600")


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
        label_name.grid(row=0 ,column=20)
        
        label_level.config(text=f"Niveau : {self.level} ")
        label_level.grid(row=1 ,column=20)
        
        label_type.config(text=f"Type : {self.type} ")
        label_type.grid(row=2 ,column=20)
        
        label_atk.config(text=f"Attaques : {self.attacks} ")
        label_atk.grid(row=3 ,column=20)
       
        label_region.config(text=f"Région : {self.region} ")
        label_region.grid(row=4 ,column=20)
       
        label_evolution.config(text=f"Evolution : {self.evolution} ")
        label_evolution.grid(row=5 ,column=20)

        show_image(self.image)




#__________________________________________________ Methodes HORS Classe ____________________________________________________________

pokedex= []


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
    label_entry_name.grid(row=15,column=0)
    entry_name.grid(row=15,column=1)
    
    label_entry_level.grid(row=16,column=0)
    entry_level.grid(row=16,column=1)
    
    label_entry_type.grid(row=17,column=0)
    entry_type.grid(row=17,column=1)
    
    label_entry_evo.grid(row=15,column=3)
    entry_evolution.grid(row=15,column=4)
   
    label_entry_atk.grid(row=16,column=3)
    entry_atk.grid(row=16,column=4)
    
    label_entry_region.grid(row=17,column=3)
    entry_region.grid(row=17,column=4)
    
    button_confirm_add.grid(row=19,column=2)
    
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

label_image = tk.Label(frame)
label_image.grid(row=0 ,column=0, rowspan=7)

label_name=tk.Label(frame, text="Nom :")
label_name.pack_forget()

label_level=tk.Label(frame, text="Niveau :")
label_level.pack_forget()

label_type=tk.Label(frame, text="Types :")
label_type.pack_forget()

label_atk=tk.Label(frame, text="Attaques :")
label_atk.pack_forget()

label_region=tk.Label(frame, text="Région :")
label_region.pack_forget()

label_evolution=tk.Label(frame, text="Stade d'évolution :")
label_evolution.pack_forget()

#_________________________________________________ Composants interface ______________________________________________________________

list_pokemon=tk.Listbox(frame)
list_pokemon.grid(row=9 ,column=2, columnspan=5)
list_pokemon.bind("<<ListboxSelect>>", select_list)


button_add_poke=tk.Button(frame,text="Ajouter un Pokemon", command=show_widget)
button_add_poke.grid(row=11 ,column=2, columnspan=5)

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




poke= Pokemon("pikachu",10,"Electric", "Lightning", "kanto", 2, "./pokemon-img/Pikachu.png")
pokedex.append(poke)
fill_pokedex(pokedex)


frame.mainloop()




#Ameliorer appel d'image (preparer le chemin d'acces) / mise en page / conditions (si le champ n'est pas vide)