# Write a program to demonstrate a right angle triangle pattern?
rows=int(input("Enter how many rows you want:"))
for row_number in range(1,rows+1):
    for column in range(1,row_number+1):
        print("*",end="")
    print("")