import time
import random as r 
print ("Welcome to the Speed Typing Test!")
Name = input("Enter your name: ")
print(f"Hello , {Name}! Get ready to test your typing speed.")
time.sleep(2)
texts=["The evening sky was painted in shades of orange and pink as the cool breeze touched the quiet streets.",
" Birds were returning to their nests, and the faint sound of children laughing filled the air. ",
"A tea seller stood by his cart, pouring steaming cups for tired workers, while the smell of freshly fried snacks spread around.",
" Everything seemed ordinary, yet there was something peaceful about that moment — a kind of calm that made time slow down, reminding everyone to pause and breathe.",]
while True:
    test1=r.choice(texts)
    print("Type the following text as quickly and accurately as you can:")
    print("\n" + test1 + "\n")
    input("Press Enter when you are ready to start.....")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    words = len(test1.split())
    words_per_minute = (words / time_taken)*60
    correct_chars = sum(1 for a, b in zip(test1, user_input) if a ==b)
    accuracy = (correct_chars / len(test1))*100
    print(f"\n Time taken : {time_taken:.2f} seconds")
    print(f" Words per minute: {words_per_minute:.2f} WPM")
    print( "Accuracy: {accuracy:.2f}%".format(accuracy=accuracy)) 
    import time 
    time.sleep(2)
    print("Thank you so much for playing the speed typing test game. Have a great day ahead!")
    import time
    time.sleep(2)

    if words_per_minute>40 and accuracy>80:
        print("Congratulations! You have a good typing speed and accuracy.")
    elif words_per_minute>20 and accuracy>50:
        print("Not bad! But you can improve your typing speed and accuracy with practice.")
    else:
        print("Keep practicing! Your typing speed and accuracy need improvement.")
    time.sleep(2)
    print("Exiting...")

    
    time.sleep(1)
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\nThanks for playing! Exiting the game...")
        time.sleep(2)
        break
