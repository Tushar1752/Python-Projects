#Fake news headline generator
import random

subjects=[
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala sitharaman",
    "A mumbai cat",
    "A group of maonkeys",
    "Prime minister modi",
    "A auto rickshaw driver from delhi",

]

actions=[
    "caught",
    "seen",
    "arrested",
    "elected",
    "appointed",
    "spotted",  
    "donated",
]

places=[
    "in delhi",
    "at the taj hotel",
    "in mumbai",
    "at the red fort",
    "in the himalayas",
    "at the india gate",
    "at the ganges ghat",
]

#start the headline generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)
    headline=f"Breaking news :{subject} {action} {place}!"
    print("\n"+headline)
    user_input=input("\n Generate another headline ? (y/n) :").strip().lower()
    if user_input=="n":
        break 
        print("Thanks for using the fake news headline generator!") 
    elif user_input=="y":
        continue
    else:
        print("Invalid input. Exiting the program.")
        break 

#print a closing message
print("Thanks for using the fake news headline generator ")