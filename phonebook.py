# Simple Phonebook using dictionary

phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. View All Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"Contact {name} added successfully!")
    
    elif choice == "2":
        name = input("Enter contact name to view: ")
        if name in phonebook:
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print("Contact not found.")
    
    elif choice == "3":
        print("\nAll Contacts:")
        for name, phone in phonebook.items():
            print(f"{name} : {phone}")
    
    elif choice == "4":
        print("Exiting Phonebook. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
