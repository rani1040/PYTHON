# Write a program to print all the prime numbers which come in the range entered by the user?
isprime=True
num=int(input("enter a number:"))
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if isprime==True:
    print("it is a prime number")
else:
    print("it is not a prime number")
   