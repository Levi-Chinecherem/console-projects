import random
from itertools import cycle

choices = ["baby", "rose", "benjamin", "japan"]
game_checker = list()
comp_score = None
play_score = None

while True:
  print("Baby Rose Benjamin Japan!")

  computer_choice = random.choice(choices)
  player_choice = input('Enter Choice: ("baby", "rose", "benjamin", "japan") ').lower()

  comp_game = random.randint(1, 10)
  play_game = int(input("\nEnter Number To Play "))
  gamer = comp_game + play_game

  print(f"Computer Number: {comp_game}")
  print(f"Player Number: {play_game}")
  print(f"Total Number: {gamer}")
  print("")
  print(f"Computer Choice: {computer_choice}")
  print(f"Player Choice: {player_choice}")

  for choice in cycle(choices):
    game_checker.append(choice)
    gamer = gamer - 1
    if gamer == 0:
      break
  game = game_checker[-1]
  print(f"Game Count: {game_checker}")
  print(f"Game Count: {comp_game + play_game} is {game} so:")

  if (computer_choice == player_choice) == game:
    print(f"Tie!")
    comp_score =+ 1
    play_score =+ 1
  if computer_choice == game:
    print(f"Computer Wins!")
    comp_score =+ 1
  if player_choice == game:
    print(f"Player Wins!")
    play_score =+ 1
  if computer_choice != game and player_choice != game:
    print(f"None Win!")
    play_score = play_score
    comp_score = comp_score
    
  print(f"Computer Score: {comp_score}")
  print(f"Player Score: {play_score}")
  Again = input("\nPlay Again? (Y/N): ").lower()
  if Again != "y":
    break
