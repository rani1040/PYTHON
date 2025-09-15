# Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”
name=input("Enter your name:")
for char in name:
    if char=="A" or char=="a":
        print("You have A in your name")
        break