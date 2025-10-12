#madlib generator is a fun program that takes user input and generates a silly story based on that input.
with open("/Users/tusharchaudhary/Documents/minor python projects/story.txt", "r") as file:
    story=file.read()
words=set()
start_of_word=-1
target_start="("
target_end=")"
for i, char in enumerate(story):
    if char==target_start:
        start_of_word=i
    elif char==target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
answer_dict={"(animal)":"Lion"}
print("Welcome to the madlib generator!")
for word in words:
    user_input=input(f"Please enter a word for {word}:")
    answer_dict[word]=user_input

for word in words:
    story=story.replace(word,answer_dict[word])
print(story)