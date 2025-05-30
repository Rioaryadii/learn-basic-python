#Rio Fandia Aryadi
#241011400059
#02TPLE001

#12 - Contact Management System

def show_menu():
    print("\n=== Contact Management System ===")
    print("1. Show all Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def show_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n=== Contacts ===")
        for name, info in contacts.items():
            print(f"- {name}: {info['phone']} | {info['email']}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found contact: {name} - Phone: {info['phone']} | Email: {info['email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()