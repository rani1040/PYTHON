# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def fictorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fictorial(number-1)
print(fictorial(3))
