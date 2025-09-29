#random number guessing game

import random
top_of_range=input("Enter the range of the number you wanna guess:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
      
    if top_of_range <=0:
        print("Please Enter a digit greater than zero")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number=random.randrange(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guesses=input("Make a guess:")
    if user_guesses.isdigit():
        user_guesses=int(user_guesses)
    else:
        print("Please type a number next time")
        continue
    if user_guesses==random_number:
        print("Correct answer buddy")
        break
    elif user_guesses > random_number:
            print("You were above the random_number")
    else:
            print("you are below the number")
print("Your correct guesses in:" ,guesses ,"attempts")