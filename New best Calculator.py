#calulator that gives result and also the hsitory of operations

History_file = "/Users/tusharchaudhary/Documents/minor python projects/history.txt"

def show_history():
    file = open(History_file, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(History_file, "w")
    file.close()
    print("History Cleared")

def add_to_history(equation, result):
    file = open(History_file, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculator(user_input):
    print("Welcome to the Calculator by Tushar")
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input Format. Please use: number 1 and number 2 with an operator in between")
        return
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed/possible")
            return
        result = num1 / num2
    else:
        print("Invalid Operator. Please use one of +, -, *, /")
        return

    print(f"The result of {num1} {operator} {num2} is: {result}")

    if int(result) == result:
        result = int(result)

    print("Result:", result)
    add_to_history(user_input, result)

def main():
    print("Welcome to the Calculator Program!")
    while True:
        user_input = input("Enter your calculation (or type 'history', 'clear history' or 'exit'): ").strip().lower()
        if user_input == "exit":
            print("Exiting the Calculator. Good bye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear history":
            clear_history()
        else:
            calculator(user_input)

print("----------------------------------")
main()