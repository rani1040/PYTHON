# Write a program to generate a random date and time from the given start and end d
import random
from datetime import date
import time
t=(2025,8,20,16,21,10,0,0,-1)
t=time.mktime(t)
print(t)
def getrandom (start,end):
    randomgenerater=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(start,dateformat))
    endtime=time.mktime(time.strptime(end,dateformat))
    print(starttime,endtime)
    randomtime=starttime+randomgenerater*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    print(randomdate)
    print(time.localtime(randomtime))
getrandom("08/21/2025","08/26/2025")