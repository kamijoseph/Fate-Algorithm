# Main to run the several modules of the project
# The Modules are:
import Arithmetic_calc as Ac
import binomial_distribution as Bd
import compound_interest as Ci
import countdown as Cd
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
    while True:
        print("Good choice. Here are the mathematics computation modules:")
        print("     1. Arithmetic Calculator")
        print("     2. Binomal distribution Calculator")
        print("     3. Compound Interest Calculator")
        print("     4. Fibonacci Numbers Generator")
        print("     5. Mean, Median and Mode Module")
        print("     6. Measurement Conversions Calculator")
        
        while True:
            mathChoice = input("Enter your choice of Math computation (1/2/3/4/5/6): ")
            if mathChoice == "1":
                Ac.main()
                break
            elif mathChoice == "2":
                Bd.main()
                break
            elif mathChoice == "3":
                Ci.main()
                break
            elif mathChoice == "4":
                Fib.main
                break
            elif mathChoice == "5":
                MMM.main()
                break
            elif mathChoice == "6":
                Mc.main()
                break
            else:
                print("Invalid choice. Choices available (1/2/3/4/5/6).\n")
        computeAgain = input("\nWould you like to continue with calculations? (Yes?No): ").strip().lower()
        if computeAgain != "yes":
            print("See you next time, Bye!")
            break

# Games Function
def games():
    while True:
        print("Perfect! Here are the Games Modules:")
        print("     1. Timed Math Challenge Game")
        print("     2. Number Guessing Game")
        print("     3. P-I-G Game")
        print("     4. Simple Quiz Game")
        print("     5. Rock Paper Scissors Game")
        
        while True:
            gameChoice = input("Enter the game module of your choice(1/2/3/4/5): ")
            if gameChoice == "1":
                MathC.main()
                break
            elif gameChoice == "2":
                Ng.main()
                break
            elif gameChoice == "3":
                Pge.main()
                break
            elif gameChoice == "4":
                Qg.main()
                break
            elif gameChoice == "5":
                Rps.main()
                break
            else:
                print("Invalid choice. Choices available (1/2/3/4/5).\n")
        replay = input("Would you lke to play more games or that one again? (Yes/No): ").strip().lower()
        if replay != "yes":
            print("Thank you for playing.\nHope you enjoyed.\nSee you later, Bye!")
            break

# Scripts Function
def scripts():
    print("Excellent! Here are some cool Scripts:")
    print("     1. Stocks Price Fetcher")
    print("     2. YouTube Videos Downloader")
    print("     3. CountDown Script")
    print("     4. Passwords Generators")

# Main Function to ..... Ugh you can see what it does, right?
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