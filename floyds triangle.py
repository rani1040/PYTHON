# Write a program to demonstrate a Floyd triangle pattern?
num=1
rows=int(input("Enter how many rows do you want:"))
for row_number in range(1,rows+1):
    for column in range(1,row_number+1):
        print(num,end=" ")
        num=num+1
    print("")