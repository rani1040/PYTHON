# Write a program to calculate the number of notes in the given amount?
amount=int(input("enter the amount"))
notes_of_hundred=amount//100
print("notes_of_100=",notes_of_hundred)
notes_of_fifty=(amount%100)//50
print("notes_of_50=",notes_of_fifty)
notes_of_twenty=((amount%100)%50)//20
print("notes_of_20=",notes_of_twenty)
