
# Number Guessing Game
import random

# Game Play Function
def number_guess():
    number = random.randint(1, 100)
    
    while True:
        try:
            user_guess = int(input("Enter Your Guess: "))
            if user_guess < number:
                print("Too low. Try Again.")
            elif user_guess > number:
                print("Too high. Try Again.")
            else:
                print("That is correct!")
                break
        except ValueError:
            print("Invalid input. Enter a valid numerical number.")
    
    play_again()

# lay again Function
def play_again():
    while True:
        again = input("Would you like to play again?: ").lower()
        if again == "yes":
            number_guess()
            break
        elif again == "no":
            print("Thank You for playing. Goodbye.")
            break
        else:
            print("Invalid entry! Enter (Yes or No).")

# Main Function
def main():
    pass

if __name__ == "__main__":
    main()