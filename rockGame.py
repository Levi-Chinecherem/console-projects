import random


def choicez():
    
    activity = ("rock", "paper", "scissors")
    computer = random.choice(activity)
    player = None

    while player not in activity:
        player = input("rock paper scissors?").lower()
    
    print()
    print("Computer: "+ computer)
    print("Player: "+ player)



    if player == computer:
        print("Tie!")
        
    elif player == "rock":
        if computer == "paper":
            print("Player Lose, Computer Wins!")
        if computer == "scissors":
            print("Computer Lose, Player Wins!")
                 
    elif player == "paper":
        if computer == "scissors":
            print("Player Lose, Computer Wins!")
        if computer == "rock":
            print("Computer Lose, Player Wins!")
                       
    elif player == "scissors":
        if computer == "rock":
            print("Player Lose, Computer Wins!")
        if computer == "paper":
            print("Computer Lose, Player Wins!")
        
            
def main_Game():
    
    while True:
        
        choicez()
        play_again = input("Wanna Play Again? (Y/N): ").lower()
    
        if play_again != "y":
            print("Thanks for Checking In. Bye!")
            break   
        else: choicez()

    
main_Game()
        

