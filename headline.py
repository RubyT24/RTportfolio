#clickbait headline generator

#Init
#functions
def believe_headline():
    noun = input("Please enter a noun: ")
    ppronoun = input("Please enter a possesive pronoun")
    place =input("Please enter a place")
    print("you wont believe what this " + noun + " found in " + ppronoun + " " + place)

def believe_headline2():
    noun = input("Please enter a noun: ")
    place =input("Please enter a place")
    ppronoun = input("Please enter a possesive pronoun")

    print(noun + " travels to " + place + " with " + ppronoun + " family")

def believe_headline3():
    noun = input("Please enter a noun: ")
    ppronoun = input("Please enter a possesive pronoun")
    place =input("Please enter a place")
    print("a " + noun + " was found in " + ppronoun +" " + place)
#main
believe_headline()
believe_headline2()
believe_headline3()
