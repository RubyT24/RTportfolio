#Conditonals

#Init

#Functions

#Challenge 1
#18 years of age or older
#US citizen
def vote_check():
    #collect input
    #process the data using conditonals
    age = int(input("Please enter your age: "))
    citizen = input("Are you a US citizen?(yes, no): ")
    if age > 17 and citizen == "yes":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

#Challenge 2
#a = int b=int c=int
#Function print the largest number out of a,b,c
def max_num(a,b,c):
    #no input needed
    #Figure out which is the largest, conditonal statements
    if a > b and a > c:
        print("A is the largest number, the value of A is: " +str(a))
    if b > a and b > c:
        print("B is the largest number, the value of B is: " +str(b))
    if c > b and c > a:
        print("C is the largest number, the value of C is: " +str(c))

#Challenge 3
#This function takes in a score and prints out the letter grade

def score_to_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score <= 59 and score >= 0:
        print("F")
    elif score < 0:
        print("invalid")

#main
vote_check()
max_num(10,5,2)
score_to_grade(81)
