
# Simple Quiz Game just for logic
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
    

def check_answer():
    pass

def display_score(correct_guesses, guesses):
    pass

def play_again():
    pass

def main():
    pass