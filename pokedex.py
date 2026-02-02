import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

frame = tk.Tk()
frame.title("Pokédex Lucas")
frame.geometry("400x700")



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
        
        label_type.config(text=f"Type : {self.type} ")
        label_type.grid(row=2, column=1, sticky="w", padx=10)
        
        label_atk.config(text=f"Attaques : {self.attacks} ")
        label_atk.grid(row=3, column=1, sticky="w", padx=10)
       
        label_region.config(text=f"Région : {self.region} ")
        label_region.grid(row=4, column=1, sticky="w", padx=10)
       
        label_evolution.config(text=f"Evolution : {self.evolution} ")
        label_evolution.grid(row=5, column=1, sticky="w", padx=10)

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
    image_add=entry_image.get()
    
    poke= Pokemon(name_add,lvl_add,type_add,atk_add,region_add,evo_add,image_add)
    pokedex.append(poke)
    fill_pokedex(pokedex)
    hide_widgets()



def show_widget():
    label_entry_name.grid(row=8, column=0, sticky="e", padx=10)
    entry_name.grid(row=8, column=1, sticky="w", padx=10)
    
    label_entry_level.grid(row=9, column=0, sticky="e", padx=10)
    entry_level.grid(row=9, column=1, sticky="w", padx=10)
    
    label_entry_type.grid(row=10, column=0, sticky="e", padx=10)
    entry_type.grid(row=10, column=1, sticky="w", padx=10)
    
    label_entry_evo.grid(row=11, column=0, sticky="e", padx=10)
    entry_evolution.grid(row=11, column=1, sticky="w", padx=10)
   
    label_entry_atk.grid(row=12, column=0, sticky="e", padx=10)
    entry_atk.grid(row=12, column=1, sticky="w", padx=10)
    
    label_entry_region.grid(row=13, column=0, sticky="e", padx=10)
    entry_region.grid(row=13,column=1, sticky="w", padx=10)
    
    label_image_entry.grid(row=14, column=0, sticky="e", padx=10)
    entry_image.grid(row=14,column=1, sticky="w", padx=10)
    
    button_confirm_add.grid(row=15, column=0, columnspan=2, pady=15)
    
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
label_image.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

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

list_pokemon=tk.Listbox(frame, bg="red", fg="white")
list_pokemon.grid(row=6, column=0, columnspan=2, pady=10)
list_pokemon.bind("<<ListboxSelect>>", select_list)


button_add_poke=tk.Button(frame,text="Ajouter un Pokemon", command=show_widget, bg="red", fg="white")
button_add_poke.grid(row=7, column=0, columnspan=2, pady=5)
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

label_image_entry=tk.Label(frame,text="Image :")
label_image_entry.pack_forget()
entry_image=tk.Entry(frame)
entry_image.insert(END,"./pokemon-img/")
entry_image.pack_forget()


button_confirm_add=tk.Button(frame, text="Confirmer", command=add_pokemon, background="red", fg="white")
button_confirm_add.pack_forget()




poke= Pokemon("pikachu",10,"Electric", "Lightning", "kanto", 2, "./pokemon-img/Pikachu.png")
pokedex.append(poke)
fill_pokedex(pokedex)


frame.mainloop()




#Ameliorer appel d'image (preparer le chemin d'acces) / mise en page / conditions (si le champ n'est pas vide) / fix les entry (double types), 4 attaques.