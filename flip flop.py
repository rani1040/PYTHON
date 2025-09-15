# Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
t=(1,2,3,3,2,1,5,6)
start_index=0
end_index=len(t)-1
while start_index<=end_index:
    if t[start_index]==t[end_index]:
        start_index=start_index+1
        end_index=end_index-1
    else:
        print("Not palindrome")
        break
print("palindrome")