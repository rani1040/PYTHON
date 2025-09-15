# Write a program to check if the number entered by the user is an Armstrong number or not?
num=int(input("Enter a number:"))
temp=num
sum=0
while num>0:
    rem=num%10
    num=num//10
    EX=rem**3
    sum=sum+EX
if temp==sum:
    print("Well done it is an armstrong number")
else:
    print("it is not an armstrong number")