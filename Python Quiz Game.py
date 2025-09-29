#Python Quiz Game

questions=("How many elements are in the periodic table?:",
          "Country who won odi worldcup 2023:",
          "Prime minister name of the india?:",
          "CM of the UP?:",)

options=(("A.114","B.333","C.118","D.119"),
         ("A.India","B.Japan","C.Australia","D.England"),
         ("A.Rahul Gandhi","B.Narendra Modi","C.Kajriwal","D.Akhilesh"),
         ("A.Yogi adityanath","B.Akhilesh","C.Mayawati","D.Chandrashekhar"))


Answers=("C","C","B","A")

guesses=[]
score=0
question_num=0


for question in questions:
   print("-------------------------")
   print(question)
   for option in options[question_num]:
      print(option)
   guess=input("Enter the correct option A , B, C, D").upper()
   guesses.append(guess)
   if guess == Answers[question_num]:
       score+=1
       print("Correct")
   else:
      print("Incorrect")
      print(f"{Answers[question_num]} is the correct")
   question_num+=1

print("-------------------------")
print(f"Your total score is: {score} / {len(questions)}")