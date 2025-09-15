# Simple Slam Book using dictionary

slam_book = {}

while True:
    print("\nSlam Book Menu:")
    print("1. Add Friend Entry")
    print("2. View Friend Entry")
    print("3. View All Entries")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter friend's name: ")
        hobby = input("Enter friend's hobby: ")
        favourite_food = input("Enter friend's favourite food: ")
        favourite_color = input("Enter friend's favourite color: ")

        # Store entry in dictionary
        slam_book[name] = {
            "Hobby": hobby,
            "Favourite Food": favourite_food,
            "Favourite Color": favourite_color
        }
        print(f"Entry for {name} added successfully!")

    elif choice == "2":
        name = input("Enter friend's name to view: ")
        if name in slam_book:
            print(f"\nDetails of {name}:")
            for key, value in slam_book[name].items():
                print(f"{key}: {value}")
        else:
            print("Entry not found.")

    elif choice == "3":
        print("\nAll Slam Book Entries:")
        for name, details in slam_book.items():
            print(f"\n{name}:")
            for key, value in details.items():
                print(f"{key}: {value}")

    elif choice == "4":
        print("Exiting Slam Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
