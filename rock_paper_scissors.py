
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
        
        # Outcome
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
             print("You win this round!")
             player_score += 1
        else:
            print("You Lose this round!")
            comp_score += 1
            
        print(f"Current score - Player: {player_score}, Computer: {comp_score}\n")
        
    # Winner
    if player_score > comp_score:
        print("You Win!")
    elif player_score < comp_score:
        print("You Lose!")
    else:
        print("It's a Tie!")
        

# Man Function
def main():
    pass

if __name__ == "__main__":
    main()