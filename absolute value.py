# Using abs() function
num1 = -25
num2 = 42

print("Absolute value of", num1, "is:", abs(num1))
print("Absolute value of", num2, "is:", abs(num2))


# Using custom function (without abs)
def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n

print("Custom absolute value of -10 is:", absolute_value(-10))
print("Custom absolute value of 15 is:", absolute_value(15))
