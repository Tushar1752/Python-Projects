#creating  a program which is capable of displYING QUESTION LIKE KBC  


print("The name of prime minister of india is:")
A=("Narendra modi")
print("A",A)
B=("Rahul gandhi")
print("B",B)
C=("kejriwal")
print("C",C)
D=("akhilesh yadav")
print("D",D)
correct_option="A"
user_choice=input("Enter your option (A/B/C/D):").strip().upper()
print("Your  answer is:",user_choice)
if user_choice  == correct_option:
    print("7 crore")
else:
    print("chala ja bhutni ke")



# KBC Game using list

# Questions list
questions = [
    "1. Who is the Prime Minister of India?",
    "2. What is the capital of India?",
    "3. What is the national animal of India?"
]

# Options list
options = [
    ["A. Narendra Modi", "B. Rahul Gandhi", "C. Kejriwal", "D. Akhilesh Yadav"],
    ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
    ["A. Tiger", "B. Lion", "C. Elephant", "D. Cow"]
]

# Correct answers list (A/B/C/D)
correct_answers = ["A", "C", "A"]

# Prize for each question
prizes = [10000, 50000, 7000000]  # ₹10K, ₹50K, ₹70 lakh

# Total amount the player wins
total_amount = 0

# Starting the game
print("🎮 Welcome to Kaun Banega Crorepati (KBC) 🎮")
print("Let's begin the game!\n")

# Asking each question one by one
for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == correct_answers[i]:
        print("✅ Sahi Jawab!\n")
        total_amount += prizes[i]
    else:
        print("❌ Galat Jawab! Chala ja bhutni ke 😄")
        break  # Game ends on wrong answer

# Final result
print(f"\n🏁 Game Over! Aap ghar le ja rahe hain ₹{total_amount}")
print("🙏 Dhanyawaad KBC khelne ke liye!")
