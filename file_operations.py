import os

contacts_file = "contacts.txt"

def load_from_file():
    contacts = []
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split(",")
                contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    return contacts

def save_to_file(contact):
    with open(contacts_file, "a") as file:
        file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")

def overwrite_contacts(contacts):
    with open(contacts_file, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")
