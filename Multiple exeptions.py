# Write a program to check how the exceptions and finally statement works.
try:
    number1=int(input("Enter a number:"))
    number2=int(input("Enter a number:"))
    result=number1/number2
except ValueError:
    print("ONLY ENTER NUMBERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
except ZeroDivisionError:
    print("DIVISION BY ZERO IS EROOR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("wrong input")
finally:
    print("IT WILL WRIGHT NO MATTER WHAT")