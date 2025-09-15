# Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
print("select your ride")
print("1. Bike 2. Car")
choice=int(input("enter the choice"))
if choice==1:
    print("what type of bike do you want")
    print("1. cycle")
    print("2. scooty")
    choice_2=int(input("enter the choice"))
    if choice_2==1:
        print("we have booked a cycle for you")
    else:
        print("we have booked a scooty for you")
elif choice==2:
    print("what type of car do you want")
    print("1. xuv")
    print("2. BMW")
    choice_2=int(input("enter the choice"))
    if choice_2==1:
        print("we have booked a xuv for you")
    else:
        print("we have booked a BMW for you")
else:
    print("wrong choice")