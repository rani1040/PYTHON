# Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allow
attendance=int(input("enter your attendance percentage = "))
Medical_cause=input("If you medical cause then type ‘Y’ for yes and ‘N’ for no = ")
if Medical_cause=="Y":
    print("You are allowed")
else:
    if attendance>75:
        print("You are allowed")
    else:
        print("You are not allowed")