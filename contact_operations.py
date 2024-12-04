from file_operations import load_from_file, save_to_file, overwrite_contacts

def is_duplicate_number(phone, contacts):
    return any(contact['phone'] == phone for contact in contacts)

def add_contact():
    name = input("Enter Name: ")
    while True:
        email = input("Enter Email: ")
        if "@" in email:
            break
        else:
            print("Invalid email address. Please include '@'.")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")

    contacts = load_from_file()
    if is_duplicate_number(phone, contacts):
        print("Error: This phone number already exists.")
        return

    contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
    save_to_file(contact)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_from_file()
    if contacts:
        for contact in contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

def remove_contact():
    phone = input("Enter the phone number of the contact to remove: ")
    contacts = load_from_file()
    updated_contacts = [contact for contact in contacts if contact['phone'] != phone]

    if len(updated_contacts) < len(contacts):
        overwrite_contacts(updated_contacts)
        print("Contact removed successfully.")
    else:
        print("Contact not found.")

def update_contact():
    phone_to_update = input("Enter the phone number of the contact to update: ")
    contacts = load_from_file()
    contact_found = False

    for contact in contacts:
        if contact['phone'] == phone_to_update:
            contact_found = True
            print(f"Found contact: {contact}")
            contact['name'] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
            while True:
                new_email = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ")
                if not new_email or "@" in new_email:
                    contact['email'] = new_email or contact['email']
                    break
                else:
                    print("Invalid email address.")
            contact['phone'] = input(f"Enter new phone (or press Enter to keep '{contact['phone']}'): ") or contact['phone']
            contact['address'] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
            overwrite_contacts(contacts)
            print("Contact updated successfully.")
            break

    if not contact_found:
        print("Contact not found.")

def search_contact():
    search_term = input("Enter name, email, or phone to search: ").lower()
    contacts = load_from_file()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['email'].lower() or search_term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
