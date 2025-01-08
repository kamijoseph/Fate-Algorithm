
# Rock, Paper, Scissors Game
import random

# Rock, Paper, Scissors Game Function
def rps_game():
    max_games = 3
    comp_score =0
    player_score = 0
    
    for _ in range(max_games):
        choices = ["rock", "paper", "scissors"]
        player = None
        computer = random.choice(choices)
        while player not in choices:
            player = input("Rock, Paper, or Scissors?: ").lower()
        print(f"Player: {player}\nComputer: {computer}")

# Man Function
def main():
    pass

if __name__ == "__main__":
    main()