from contact_operations import add_contact, view_contacts, remove_contact, update_contact, search_contact

def menu():
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Update Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            remove_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
