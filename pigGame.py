
# Simple Pig Game
import random

def getPlayers():
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Players must be between two and four")
        else:
            print("Invalid entry! Try again")

def main():
    players = getPlayers()
    maxScore = 50
    playerScore = [0 for _ in range(players)]
    
    # ZeGame looooooooop
    while max(playerScore) < maxScore:
        for player in range(players):
            print(f"\nPlayer {player + 1}, its your turn.")
            currentScore = 0
            
            while True:
                roll = input("Would you like to roll? (Yes/No): ").strip().lower()
                if roll == "yes":
                    value = random.randint(1, 6)
                    print(f"You rolled a {value}")
                    if value == 1:
                        print("You rolled a 1. Turn over.")
                        currentScore = 0
                        break
                    else:
                        currentScore += value
                        print(f"Your current score this turn is: {currentScore}")
                elif roll == "no":
                    break
                else:
                    print("Invalid input. Enter Yes to roll or No to hold.")
            
            playerScore[player] += value
            print(f"Player {player + 1}'s total score: {playerScore[player]}")
            
            if playerScore[player] >= maxScore:
                print(f"\nPlayer {player + 1} wins with a score of {playerScore[player]}!")
                return
            
if __name__ == "__main__":
    main()