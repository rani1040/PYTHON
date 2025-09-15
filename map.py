# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
# take each item from as list change it and make a new list
l1=[1,2,3]
l2=[4,5,7]
l3=map(lambda x,y:x+y ,l1,l2)
print(list(l3))