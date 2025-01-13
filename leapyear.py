#Leap year checker
#Name

#Init

#Functions

#If a year is divisible by 4, it is a leap year
#However if that year is also divisible by 100, it is not
#If it is divisible by 400 it is a leap year

def is_leap_year(year):
    if year % 400==0 and year % 4==0:
        print("true")
    elif year % 100==0:
        print("false")
    elif year % 4==0:
        print("true")
#main
is_leap_year(2024) #True
is_leap_year(1900) #False
is_leap_year(1600) #True
