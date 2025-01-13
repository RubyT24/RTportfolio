#Generates the animal breed the viewer will be based on how they answer each question
#They first have to chose between dog and cat
#then big or small
#then color

print("Welcome to: What animal breed are you?")
print("Answer the questions to find out your animal breed")
ans = input("dog or cat?")
if ans == "dog":
    ans = input("Big or small?")
    if ans == "small":
        ans = input("beige or white?")
        if ans == "beige":
            print("Chihuahua")
        else: print("Frenchie")
    elif ans == "big":
        ans = input("black or brown")
        if ans == "black":
            print("Shepherd")
        else: print("pitbull")


if ans == "cat":
    ans = input("shorttail or longtail?")
    if ans == "shorttail":
        ans = input("orange or white?")
        if ans == "orange":
            print("shorthair")
        else: print("persian")
    elif ans == "longtail":
        ans = input("grey or black")
        if ans == "grey":
            print("Tabby")
        else:
            print("Manx")
