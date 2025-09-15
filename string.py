# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
l=["ABC","CFC","XYZ","ABBA","3333"]
print(len(l[0]))
for item in l:
    if len(item)>2 and item[0]==item[-1]:
        print(item)
        