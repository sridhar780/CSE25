contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append((name, phone))
        print(f"Contact '{name}' added!")
    
    elif choice == '2':
        name = input("Name: ")
        found = False
        for contact in contacts:
            if contact[0].lower() == name.lower():
                print(f"Name: {contact[0]}, Phone: {contact[1]}")
                found = True
                break
        if not found:
            print("No contact found.")
    
    elif choice == '3':
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts:
                print(f"Name: {name}, Phone: {phone}")
    
    elif choice == '4':
        break
    
    else:
        print("Invalid choice.")
