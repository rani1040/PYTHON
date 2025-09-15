# Write a program to demonstrate the numbers in a diamond pattern?
rows=int(input("Enter how many rows you want:"))
if rows%2==0:
    half_diomand_row=rows//2
else:
    half_diomand_row=(rows//2)+1
spaces=half_diomand_row-1
for i in range(1,half_diomand_row+1):
    for j in range(1,spaces+1):
        print(end=" ")
    spaces=spaces-1
    for k in range(0,2*i-1):
        print("*",end="")
    print("")
spaces=1
for i in range(1,half_diomand_row):
    for j in range(1,spaces+1):
        print(end=" ")
    spaces=spaces+1
    for k in range(1,2*(half_diomand_row-i)):
        print("*",end="")
    print("")