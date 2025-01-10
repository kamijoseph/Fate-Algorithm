
# Simple Quiz Game just for logic

questions = {
            "Who created Python?: ": "A",
            "What year was Python created?: ": "B",
            "Python is tributed to which comedy group?: ": "C",
            "Is the Earth Round?: ": "A"
        }

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bills Gate", "D. Mark Zuckerberg"],
        ["A. 1989", "B. 1991", "C. 1974", "D. 1980"],
        ["A. Lonely Island", "B. NL", "C. Monty Pyton", "D. Mark Zuckerberg"],
        ["A. True", "B. False", "C. Debatable", "D. What is Earth"]]

# New Game Initialiation
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("-------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)
    
# Checking the Answer
def check_answer(answer, guess):
    if answer == guess:
        print("Correct Answer.")
        return 1
    else:
        print("Incorrect Answer.")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print(f"Your Score is {str(score)}%")

# Function to Prompt Play Again 
def play_again():
    rensponse = input("Would you like to play again? (Yes/No): ").lower()
    if rensponse == "yes":
        return True
    return False

def main():
    while True:
        main_cont = input("Welcome, this is the Quiz Game. Do you wish to continue? (Yes/No): ").lower()
        if main_cont == "yes":
            new_game()
            break
        elif main_cont == "no":
            print("Thank You for Visiting, See you next time.")
            break
        else:
            print("Invalid Input! Enter Yes or No")
    
    while play_again:
        new_game()
    