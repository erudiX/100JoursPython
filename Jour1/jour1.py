contacts = {}

def show_menu():
    print ("\n=========== MENU DU GESTIONNAIRE DE CONTACT =================")
    print("1. Creer un nouveau contact")
    print("2. Affichier les contacts")
    print("3. Chercher Un contact ")
    print("4. Modifier un Contact")
    print("5. Supprimer un contact")
    print("6. Quitter le menu ...")
    
def add_contact():
    name = input("Vauillez saisir le nom du Conctact : ")
    phone = input ("Entrer le numero de Telephone : ")
    email = input ("Adresse mail du Contact : ")
    adresse = input ("Ajouter l'addresse de votre contact :")
    contacts[name] = {"phone" : phone, "email": email}
    print(f"Contact {name} a ete ajoute a votre Repertoire avec success !")

def view_contacts():
    if contacts:
        print("\n===== LIST DES CONTACTS =======")
        for name, details in contacts.items():
            print(f"Nom : {name}")
            print(f"phone : {details['phone']}")
            print(f"email : {details['email']}")
            print(f"adresse : {details['adresse']}")

def search_contact(): 
    name = input (" Veuillez introduire le nom du contact que vous cherchez : ")
    if name in contacts:
        print (f"\n+++++Les informations relatives a {name} sont les suivants +++++")
        print(f"Nom : {name}")
        print(f"phone : {contacts['phone']}")
        print(f"email : {contacts['email']}")
        print(f"adresse : {contacts['adresse']}")
    else:
        print (f"Le Nom {name} N'est pas present dans votre repertoire de contact")

def edit_contact():
    name = input(" Veuillez saisir le nom du contact que vous voullez modifier ")
    if name in contacts:
        phone = input ("Entrez le nouveau numero de telephone")
        email = input ("Veuillez nous fournir la nouvelle adresse mail")
        adresse = input ("Veuillez nous fournir la nouvelle adresse")
        contacts[name] = {"phone" : phone  , "email" : email  , "adresse" : adresse}
    else:
        print(f"Le contact {name} N'existe pas dans ce repertoire...")

def delete_contact():
    name = input("Entrer le nom du contact que vous souhaitez supprimer de votre Repertoire : ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} supprimer avec succeess")
    else:
        print(f"Contact {name} ne figure pas dnas vos contacts...")

while True:
    show_menu()
    choice = input("Entrer votre choix (1-6) : ")

    if choice == "1" :
        add_contact()
    elif choice == "2" :
        view_contacts()
    elif choice == "3" :
        search_contact()
    elif choice == "4" :
        edit_contact()
    elif choice == "5" :
        delete_contact()
    elif choice == "6" :
        print("Merci D'utiliser notre aplication")
    else:
        print("Entrer Invalide. Selectionnez une option entre 1 et 6... Merci...")
    