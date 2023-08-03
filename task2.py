#This program determines if a year is a leap year.  In order to test if the year is a multiple of 4 I consulted this page:
#https://www.geeksforgeeks.org/efficiently-check-whether-n-multiple-4-not/
#and used their suggested method in my code, in order to check whether the last two bits are unset or not
#in the binary representation of the year.  As they say in the page, it is the more efficient way of doing it

#Getting input from the user
original_year = int(input("What year do you want to start with? "))
number_years = int(input("How many years do you want to check? "))

#Setting the values for the counter and end of range
n = original_year
last_year = original_year + number_years

#Determining if a year in the range (including the original year given by the user) is a leap year
#and displaying the correspondent messages
print(" ")
for n in range(original_year, last_year):
   if (n & (3) == 0):
      print(f"{n} is a leap year")
   else:
      print(f"{n} isn’t  a leap year")