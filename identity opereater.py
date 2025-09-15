# Write a program to illustrate the use of 'is' identity operator
age=10
if type(age) is int:
    print("age is integer")
else:
    print("age is not integer")
a=[20]
b=[20]
if (a is b):
    print("they have same identity")
else:
    print("they have different identity")