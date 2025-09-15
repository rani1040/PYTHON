# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
d={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
country=input("Enter your country:")
print("Your country code is ",d.get(country,"ERROR Country not found!!!!!!!!!!!!!!!!!"))