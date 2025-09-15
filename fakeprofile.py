import random

# Sample data in tuples
first_names = ("Rani", "Aryan", "Saanvi", "Kartik")
last_names = ("Sharma", "Verma", "Singh", "Patel")
jobs = ("Teacher", "Developer", "Doctor", "Engineer")
cities = ("Mumbai", "Delhi", "Bangalore", "Chennai")
domains = ("example.com", "mail.com", "fakeemail.com")

# Generate fake profile
name = random.choice(first_names) + " " + random.choice(last_names)
age = random.randint(18, 60)
email = name.split()[0].lower() + "." + name.split()[1].lower() + "@" + random.choice(domains)
phone = "+91-" + str(random.randint(6000000000, 9999999999))
address = random.choice(cities) + ", India"
job = random.choice(jobs)

# Store in dictionary
profile = {
    "Name": name,
    "Age": age,
    "Email": email,
    "Phone": phone,
    "Address": address,
    "Job": job
}

# Print profile
for key, value in profile.items():
    print(f"{key}: {value}")
