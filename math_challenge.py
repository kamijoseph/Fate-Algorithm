
# Timed Simple Math Challege
import random
import time

# Constant Variables for the Operations and Expression Generation
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10

# Function to Generate the Problems
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expression = f"{left} {operator} {right}"
    answer = eval(expression)
    return expression, answer

# Function tha runs the timed Math Challenge.
def main():
    print("Welcome, this is the Timed Math Challenge!")
    input("Press Enter to start.................. ")
    print("------------------------------------------\n")
    
    start_time = time.time()
    wrong_attempts = 0
    
    for problem_number in range(1, TOTAL_PROBLEMS + 1):
        expr, correct_answer = generate_problem()
        
        while True:
            try:
                user_guess = int(input(f"Problem #{problem_number}: {expr} = "))
                if user_guess == correct_answer:
                    break
                else:
                    print("Incorrect answer.Try again")
                    wrong_attempts += 1
            except ValueError:
                print("Invalid Input! Pleae Enter A valid nmerical value.")
    
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print("------------------------------------------")
    print(f"Great job! You completed {TOTAL_PROBLEMS} problems in {total_time} seconds.")
    if wrong_attempts > 1:
        print(f"You had {wrong_attempts} incorrect attempts.")
    else:
        print(f"You had only {wrong_attempts} incorect attempt.")
        

if __name__ == "__main__":
    main()