# Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer
import random
while True:
    total_moves=["rock","paper","scissors"]
    computer_choice=random.choice(total_moves)
    user=input("rock,paper,scissors:")
    print(f"You choose {user}and computer chosses {computer_choice}")
    if user==computer_choice:
        print("Its a draw")
    elif user=="rock":
        if computer_choice=="scissors":
            print("Rock smashes the scissors YOU WIN!!!!!!!!!!!!!!!!!")
        else:
            print("You lose ):")
    elif user=="paper":
        if computer_choice=="scissors":
            print("you lose ):")
        else:
            print("Paper covers the rock YOU WIN!!!!!!!!!!!!!!!!!")
    elif user=="scissors":
        if computer_choice=="paper":
            print("scissors covers the paper YOU WIN!!!!!!!!!!!!!!!!!")
        else:
            print("You lose ):")
    play_again=input("Y or N")
    if play_again=="N":
        break