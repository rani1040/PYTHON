# Write a program to generate a random integer and match it with the input given by the user?
import random
computer_choice=random.randint(10,20)
playing=True
while playing:
    number=int(input("Enter a number:"))
    if number==computer_choice:
        print("WELL DONE YOU GUESSED IT CORRECT!!!!!!!!!!")
        break
    elif number<computer_choice:
        print("Enter a number greater than ",number)
    elif number>computer_choice:
        print("Enter a number smaller than ",number)