# Write a program to calculate the BMI of a person?
h=float(input("enter your height in cm= "))
w=float(input("enter your weight in kg= "))
bmi=w/(h/100)**2
print("your bmi= ",bmi)
if bmi<18.5:
    print("you are underweight")
elif bmi>=18.5 and bmi<25:
    print("you are healthy")
elif bmi>=25 and bmi<30:
    print("you are overweight")
else:
    print("you are obese")