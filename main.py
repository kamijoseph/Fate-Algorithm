# Main to run the several modules of the project
# The Modules are:
import Arithmetic_calc as Ac
import binomial_distribution as Bd
import compound_interest as Cd
import countdown as Cdn
import fibbonacci as Fib
import math_challenge as MathC
import mean_median_mode as MMM
import measurement_calc as Mc
import number_guess as Ng
import password_gen as Pg
import pigGame as Pge
import quiz_game as Qg
import rock_paper_scissors as Rps
import stocksPrice as SnP
import YouTube as DD                                                                                  

# Mathematical Computations function
def mathComputations():
    print("Good choice. Here are the mathematics computation modules:")
    print("     1. Arithmetic Calculator")
    print("     2. Binomal distribution Calculator")
    print("     3. Compound Interest Calculator")
    print("     4. Fibonacci Numbers Generator")
    print("     5. Mean, Median and Mode Module")
    print("     6. Measurement Conversions Calculator")
    # Aritmetic calculator
    # Binomial distribution
    # Compound Interest
    # Fib Generator
    # Mean median and Mode
    # Measurement Calculator
    pass

def games():
    # Modules
    # Math Challenge
    # Number guessing game
    # pig game
    # quiz game
    # rock papers scissors game
    pass

def scripts():
    # Modules
    # stocks price
    # Youtube downloader
    # countodown
    # password generators
    pass



def main():
    print("Welcome to the Fate Algorithm System\nMy name is Fate, and I will help you with different tasks and terminal gameplays\n")
    name = input("What is your name? ")
    print(f"Nice to meet you {name}!\n")
    print("I have a collection Calculations modules, Terminal games modules, and random Scripts modules")
    while True:
        userInput = input("What would you like today? \nFor Math Computations type 1\nFor Games type 2\nFor scripts type 3\nType 4 to exit: ")
        if userInput == "1":
            return mathComputations()
        elif userInput == "2":
            return games()
        elif userInput == "3":
            return scripts()
        elif userInput == "4":
            print(f"Thank You for visiting {name}. See you again soon fren.")
            break
        else:
            print("Invalid entry! Try again.")

if __name__ == "__main__":
    main()