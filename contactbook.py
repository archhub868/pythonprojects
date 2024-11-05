def display_menu():
    print("\nContact Management System")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Delete a contact")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Create a dictionary to store the contact details
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    # Add the contact to the list
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    
    # Find the contact by name
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print(f"\nContact '{name_to_delete}' deleted successfully!")
            return
    
    print(f"\nContact '{name_to_delete}' not found.")

def main():
    contacts = []

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
