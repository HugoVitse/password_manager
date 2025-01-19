import tkinter as tk
from utils import aes
import requests


fenetre = tk.Tk()
fenetre.title("Password Manager")
row_count = 0
col_count = 0

    

def clear():
    for i in range(row_count):  
        fenetre.grid_rowconfigure(i, weight=0, minsize=0)
    
    for i in range(col_count):
        fenetre.grid_columnconfigure(i, weight=0, minsize=0)
    
    for widget in fenetre.winfo_children():
        widget.grid_forget() 
    
def login(password : str):
    req = requests.get("http://localhost:5000/get_vault")
    vault = req.json()
    passwords = aes.decrypt(bytes.fromhex(vault["vault"]),password,bytes.fromhex(vault["tag"]), bytes.fromhex(vault["nonce"]))
    if(passwords != "error"):
        afficher_page_accueil(passwords,password)
        
        
        
def save(entries_passwords,entries_usernames,_passwords, password):
    
    passwords = []
    
    for i in range(len(entries_passwords)):
        passwords.append({
            "id":i,
            "data":{
                "host":_passwords[i]["data"]["host"],
                "username":entries_usernames[i].get(),
                "password":entries_passwords[i].get(),
            }
        })
    
    encrypted_passwords, tag ,nonce = aes.encrypt(passwords,password)
    

    url = "http://localhost:5000/set_vault"


    data = {
        'vault': encrypted_passwords.hex(),
        'tag': tag.hex(),
        'nonce': nonce.hex()
    }

    response = requests.post(url, data=data)

    


def afficher_page_accueil(passwords,password):
    
    global row_count,col_count
    
    labels= []
    entries_passwords = []
    entries_usernames = []
    
    
    nb_passwords = len(passwords)
    
    clear()


    fenetre.geometry("300x300")  
    
    for i in range(nb_passwords):
        fenetre.grid_rowconfigure(i, weight=1)
        row_count +=1
        
    for j in range(3):
        fenetre.grid_columnconfigure(j, weight=1)
        col_count += 1  


    for i in range(nb_passwords):
        labels.append(tk.Label(fenetre, text=f"Mot de passe de {passwords[i]["data"]["host"]}"))
        entry = tk.Entry(fenetre, width=30)
        entry.insert(0,passwords[i]["data"]["password"])
        entries_passwords.append(entry)
        
        entry_u = tk.Entry(fenetre, width=30)
        entry_u.insert(0,passwords[i]["data"]["username"])
        entries_usernames.append(entry_u)
        
        
    for i in range(len(labels)):
        labels[i].grid(row=i, column=0)
        
    for i in range(len(entries_passwords)):
        entries_passwords[i].grid(row=i, column=1)
        entries_usernames[i].grid(row=i, column=2)
        
    frame = tk.Frame(fenetre)
    frame.grid(column=1,row=nb_passwords,sticky='n',pady=10)
    
    frame.grid_columnconfigure(0,weight=1)
    frame.grid_columnconfigure(1,weight=1)
    
    bouton_logout = tk.Button(frame, text="Déconnexion", command=afficher_login)
    bouton_logout.grid(column=0,row=0,sticky='n',pady=10)
    bouton_logout = tk.Button(frame, text="Save", command= lambda : save(entries_passwords,entries_usernames,passwords,password))
    bouton_logout.grid(column=1,row=0,sticky='n',pady=10)
    

    
def afficher_login():
    global row_count,col_count
    clear()
    
    

    
    fenetre.grid_rowconfigure(0, weight=1)
    fenetre.grid_rowconfigure(1, weight=1)
    fenetre.grid_columnconfigure(0, weight=1)
    
    col_count = 1
    row_count = 2
    
    entry = tk.Entry(fenetre, width=30)  # Crée un champ de texte
    entry.grid(column=0,row=0,sticky='s',pady=10)
    
    bouton_login = tk.Button(fenetre, text="Connexion", command=lambda: login(entry.get()) )
    bouton_login.grid(column=0,row=1,sticky='n',pady=10)


afficher_login()

# Boucle principale
fenetre.mainloop()