# Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
# average=sum/total numbers
l=[1,2,3,4,5,6,7,8]
sum=0
for i in l:
    sum=i+sum
print(sum)
total=len(l)
a=sum/total
print("average is ",a)
print(min(l))
print(max(l))
