start=int(input("enter the starting number:"))
end=int(input("Enter the ending number:"))
l1=[]
for i in range(start,end):
    l1.append(i**2)
    print(l1)
for item in l1:
    if item%2==0:
        print(item," is even")
    else:
        print(item," is odd")