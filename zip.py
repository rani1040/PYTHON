# Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
names=["Rani","Mahd","Rohan"]
marks=[50,90,80]
info=zip(names,marks)
print(list(info))
new_dictionary={names:marks for names,marks in zip(names,marks)}
print(new_dictionary)
print("hello world")
exit()
print("Hello Mahd")