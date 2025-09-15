# Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def add (num1,num2):
    return num1 + num2
def subtract (num1,num2):
    return num1-num2
def multiply (num1,num2):
    return num1*num2
def divide (num1,num2):
    return num1/num2
print("please select the operation")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. division")
choice=input("enter your choice ")
n1=int(input("enter first num "))
n2=int(input("enter second num "))
if choice=="a":
    print(n1," + ",n2," = ",add(n1,n2))
elif choice=="b":
    print(n1," - ",n2," = ",subtract(n1,n2))
elif choice=="c":
    print(n1," x ",n2," = ",multiply(n1,n2))
elif choice=="d":
    print(n1," / ",n2," = ",divide(n1,n2))
else:
    print("invalid input")
