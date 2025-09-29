#Rock Papper Scissor game

import random

user_wins=0
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock=0,paper=1,scissor=2
    computer_guess= options[random_number]
    print("Computer Picked",computer_guess)
    if user_input=="rock" and computer_guess=="scissor":
        print("You Won ")
        user_wins+=1
        continue
    
    elif user_input=="paper" and computer_guess=="rock":
        print("You Won ")
        user_wins+=1
        continue
    elif user_input=="scissor" and computer_guess=="paper":
        print("You Won ")
        user_wins+=1
        continue
    else:
        print("You lost")
        computer_wins+=1
print("You won:" , user_wins ,"times")
print("Computer wins:",computer_wins,"times")
if user_wins> computer_wins:
    print("Congrats you are the champion ")
else:
    print("Sorry buddy you lost but the computer wons more than you")
print("Good Bye ")