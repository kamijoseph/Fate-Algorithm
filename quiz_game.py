
# Simple Quiz Game just for logic

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

def play_again():
    pass
    

def main():
    pass