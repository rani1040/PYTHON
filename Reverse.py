# Write a program to reverse the string entered by the user.
word=input("Enter your name:")
s=""
for letter in word:
    s=letter+s
print(s)
print(word[::-1])