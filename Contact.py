contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact {name} added successfully.")

def view_contact(name):
    if name in contacts:
        contact_info = contacts[name]
        print(f"Name: {name}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\n1. Add Contact\n2. View Contact\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name to view contact: ")
            view_contact(name)

        elif choice == '3':
            print("Exiting contact book.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
