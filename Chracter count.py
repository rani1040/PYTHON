# Write a program to check how many times a character is repeated in a word?
word=input("Enter a word:")
count=0
character=input("Enter a character:")
for char in word:
    if char==character:
        count=count+1
print(character+" is repeating "+ str(count)+" times")