# Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75
tax=0
amount=0
unit=int(input("enter the units = "))
if unit<50:
    tax=25
    amount=unit*2.60
elif unit<100:
    tax=35
    amount=130+(unit-50)*3.25
elif unit<200:
    tax=45
    amount=162.50+130+(unit-100)*5.26
else:
    tax=75
    amount=162.50+130+526+(unit-200)*8.45
bill=amount+tax
print("electricity bill is ",bill)