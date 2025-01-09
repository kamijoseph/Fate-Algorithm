
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
    pass

# Main Function
def main():
    pass

if __name__ == "__main__":
    main()