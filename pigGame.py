
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
            print(f"\nPlayer {player + 1}, its tour turn.")
            currentScore = 0
            
            
if __name__ == "__main__":
    main()