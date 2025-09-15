# Write a program to calculate the product of the middle digits of a number?
num=int(input("Enter a number"))
temp=num
num_leghnth=0
while temp>0:
    num_leghnth=num_leghnth+1
    temp=temp//10
print(num_leghnth)
if num_leghnth>=4:
    num_leghnth=num_leghnth//2
    c=0
    while num>0:
        rem=num%10
        if num_leghnth==c:
            first=rem
        elif c==(num_leghnth-1):
            second=rem
        num=num//10
        c=c+1
    print(first*second)