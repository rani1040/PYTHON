# Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip
def planecost (city):
    if city=="Karachi":
        return 150
    elif city=="Islamabad":
        return 500
    elif city=="Delhi":
        return 1000
    elif city=="Quetta":
        return 200
    elif city=="los angles":
        return 10000
    





def carcost (days): 
    if days>7:
        return 100*days-50
    elif days>3:
        return 100*days-20
    else:
        return 100*days





def hotelcost (night):
    return 1000*night





city=input("Enter your city:")
day=int(input("Enter how many days you want to rent a car:"))
nights=int(input("Enter how many nights you want to spent:"))

print(planecost(city))
print(carcost(day))
print(hotelcost(nights))