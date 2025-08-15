import json
import os

if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
else:
    contacts = []


def add_contact():

    """
    Demande prénom, nom et numéro à l'utilisateur.
    Vérifie que le numéro est numérique.
    Ajoute le contact à la liste et sauvegarde dans contacts.json.
    """

    fname = input("Enter contact first name : ")
    name = input("Enter contact name : ")
    number = input("Enter contact number : ")
    if number.isnumeric() :
        contacts.append({'name': name, 'fname': fname, 'number': number})
        print("Contact has been successfully saved !")
        # Immediat backup
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
    else :
        print("You need to save a number.")


def display_contacts():

    """
    Affiche tous les contacts de la liste.
    Si la liste est vide, affiche un message.
    Chaque contact est affiché avec prénom, nom et numéro.
    """

    if not contacts :
        print("You have no friends.")
    else :
        print("\nContact list")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['fname']} {contact['name']} - {contact['number']}")
            print("-" * 30)


choice = ""

# Boucle principale du programme
# Affiche le menu, exécute l'action choisie et demande si l'utilisateur veut revenir au menu
while True:
    print("\nWelcome to your personal contact assistant ! What can I do for you today ?")
    print("1: Add a contact")
    print("2: Display my contact list")
    print("3: Leave my personal contact assistant")

    choice = input("\nChoose your option : ")

    if choice == '1' :
        add_contact()
    elif choice == '2' :
        display_contacts()
    elif choice == '3':
        print("\nGoodbye !")
        # Save to a json file
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        break
    else:
        print("You are asked to choose a number between 1 and 3.")
        continue
    retour = input("Do you want to return to the main menu ? (Yes/No) : ").lower()
    if retour not in ['yes', 'y']:
        # Save to a json file
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Goodbye !")
        break

