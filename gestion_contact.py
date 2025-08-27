import json
import os
import time

# Load contacts from JSON file if it exists
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
else:
    contacts = []


def add_contact():

    """
    Prompt the user to enter a first name, last name, and phone number.
    Check that the phone number is numeric.
    Add the contact to the contacts list and save it to contacts.json.
    """

    fname = input("Enter contact first name : ")
    name = input("Enter contact name : ")
    number = input("Enter contact phone number : ")
    if number.isnumeric() :
        contacts.append({'name': name, 'fname': fname, 'number': number})
        print("Contact registration...")
        time.sleep(1)
        print("Contact has been successfully saved !")
        time.sleep(1)
        print("Returning to main menu...")
        time.sleep(1.5)
        # Immediat backup
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
    else :
        print("You need to save a phone number.")


def display_contacts():

    """
    Display all contacts in the contacts list.
    If the list is empty, display an informative message.
    Each contact is shown with first name, last name, and phone number.
    """

    if not contacts :
        print("You have no friends.")
    else :
         while True:
            print("\nContact list")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['fname']} {contact['name']} - {contact['number']}")
                print("-" * 30)

            delete = input("Do you want to delete a contact from the list ? (Yes/No) : ").lower()
            if delete in ['y', 'yes']:
                delete_contact()
            else:
                print("Returning to main menu...")
                time.sleep(1)
                break


def delete_contact():

    """
    Delete the selected contact from the contact list.
    Delete the selected contact from the JSON File. 
    """

    num = input("What is the number of the contact you want to delete ? ")
    if num.isnumeric() :
        index = int(num)-1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            confirm = input(f"Are you sure you want to delete {contact['fname']} {contact['name']}? I'll really miss them! (Yes/No) : ").lower()
            if confirm in ['y', 'yes']:
                print("Okay... let me grab my hammer of forgetfulness... ")
                time.sleep(1.2)
                deleted = contacts.pop(index)

                # Immediat backup
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f)

                print(f"Contact {deleted['fname']} {deleted['name']} has been deleted.")
                time.sleep(1.5)
            else:
                print("Deletion cancelled.")
                time.sleep(1.5)
        else:
            print("This contact does not exist, idiot.")
            time.sleep(1.5)
    else :
        print("Please choose a number among the contact list. That should not be that hard...")
        time.sleep(1.5)


choice = ""

# Main program loop
# Displays the menu, executes the chosen action, and asks if the user wants to return to the menu
while True:
    print("\nWelcome to your personal contact assistant ! What can I do for you today ?")
    print("1: Add a contact")
    print("2: Display my contact list")
    print("3: Leave my personal contact assistant")

    choice = input("\nChoose your option : ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        print("Hmm... where did I put that list again... ")
        time.sleep(1.2)
        print("There it is !")
        time.sleep(0.8)

        display_contacts()
    elif choice == '3':
        print("Already leaving me?")
        time.sleep(1)
        print("Promise me you’ll come back soon, okay?")
        time.sleep(1)
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        break
    else:
        print("You are asked to choose a number between 1 and 3.")

