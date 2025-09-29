#choose your own adventure game project

#in this we can ask so many question using the conditional statements as much as it possible


name=input("Enter your name:")
print("Welcome",name,"to this adventure!")
answer=input("You are on a dirt road and it has come to an end but you can go left or right . Now Which side you want to go?(Left/Right) :").lower()
if answer=="left":
    answer=input("you come to a river now here you walk or swim across the river? Type walk if you wanna walk or type swim if you wanna swim:")
    if answer=="swim":
        print("you swam across and were eaten by an aligator.")
    elif answer=="walk":
        print("You walk for so many miles and ran out of outer and you lost the game")
    else:
        print("Not a valid option . YOU loose")
elif answer=="right":
    answer=input("you come across ,it look woobly,do you want to cross it or head back (coss/back) ?:")
    if answer=="back":
        print("You go back to main road,YOU LOSE.")
    elif answer=="cross":
        print("YOu cross the bridge and meet a stranger .would you like to talk with that stranger or ignore them: (yes/no)")
        if answer=="yes":
            print("HE killed you . You lost")
        elif answer=="no":
            print("YOu survived . YOU won")
        else:
            print("Wrong input.YOU lost ")
else:
    print("Not a valid option you lost")