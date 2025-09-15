# Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
s1={1,2,3,4,5,6,7,8,9}
print(s1)
s2={(1,2,3,4),"dictionary"}
print(s2)
s3={1, 2, 3, 4, 3, 2 , 4}
print(s3)
s4=set([1, 2, 3, 2])
print(s4)
s5={ 0,1, 3, 4, 5}
print("orignal set=",s5)
s5.pop()
print("set after removel is=",s5)