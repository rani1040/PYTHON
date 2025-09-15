# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(number):
    return number*number*number
def divisiblle_3(number):
    if number%3==0:
        print("It is divisible by 3")
        print(cube(number))
    else:
        print("It is not divisible by three")
number=int(input("Enter a number:"))
divisiblle_3(number)