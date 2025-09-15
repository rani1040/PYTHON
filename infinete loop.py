# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
valid=False
while not False:
    try:
        user_input=int(input("Enter a number"))
        while user_input%2==0:
            print("BYE BYE")
        valid=True
    except:
        print("Invalid")