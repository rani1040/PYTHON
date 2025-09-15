# Write a program to find the sum of natural numbers.
num=int(input("Enter a number:"))
sum=0
while num>0:
    print(str(num)+" + "+str(sum) +" = ")
    sum=sum+num
    print(str(sum))
    num=num-1