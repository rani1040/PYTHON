# Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?
marks1=int(input("enter the marks of 1 subject"))
marks2=int(input("enter the marks of 2 subject"))
marks3=int(input("enter the marks of 3 subject"))
marks4=int(input("enter the marks of 4 subject"))
marks5=int(input("enter the marks of 5 subject"))
total=marks1+marks2+marks3+marks4+marks5
avg=total/5
if avg>=91 and avg<=100:
    print("grade A")
elif avg>=81 and avg<=90:
    print("grade A2")
elif avg>=71 and avg<=80:
    print("grade B1")
elif avg>=61 and avg<=70:
    print("grade B2")
elif avg>=51 and avg<=60:
    print("grade C1")
elif avg>=41 and avg<=50:
    print("grade C2")
elif avg>=31 and avg<=40:
    print("grade D1")
elif avg>=21 and avg<=30:
    print("grade D2")
elif avg>=11 and avg<=20:
    print("grade E1")
else:
    print("grade E2")