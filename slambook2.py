# Create Your Own Slam Book

slam_book = {}

print("Welcome to Your Slam Book! 📝")

# Get your details
name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")
favourite_food = input("Enter your favourite food: ")
favourite_color = input("Enter your favourite color: ")

# Store in dictionary
slam_book[name] = {
    "Age": age,
    "Hobby": hobby,
    "Favourite Food": favourite_food,
    "Favourite Color": favourite_color
}

print("\n🎉 Slam Book Entry Created!\n")

# View your slam book entry
print(f"Here is your Slam Book entry, {name}:")
for key, value in slam_book[name].items():
    print(f"{key}: {value}")
