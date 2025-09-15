# The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
mean=38
total=40
correct=56
wrong=36
sum=mean*total
correct_sum=sum-(wrong-correct)
correct_mean=correct_sum/total
print("correct mean is "+str(correct_mean))