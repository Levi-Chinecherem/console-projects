import random

###########################################################################
#-Control-#################################################################
def checker():
  comp_score = play_score = 0
  choices = [0,1,2,3,4,5,6,7,8,9,10]
  computer = random.choice(choices)

  print("\nEarly In The Morning Pepper Soup!")
  player = int(input("Enter a Number to Play: "))
  print("\nComputer:", computer)
  print("Player:", player)

  if computer == (computer + player):
    print("\nTotal:", computer + player)
    print("Computer Wins!\n")
    comp_score =+ 1
    play_score = play_score
    print("Computer Score:", comp_score)
    print("Player Score:", play_score)

  if player == (computer + player):
    print("\nTotal:", computer + player)
    print("Player Wins!\n")
    comp_score = comp_score
    play_score =+ 1
    print("Computer Score:", comp_score)
    print("Player Score:", play_score)

  if computer != (computer + player) or player != (computer + player):
    print("\nTotal:", computer + player)
    print("None Wins!\n")
    comp_score = comp_score
    play_score = play_score
    print("Computer Score:", comp_score)
    print("Player Score:", play_score)

  again = input("Play Again? (Y/N)").lower()
  while again != 'y':
    break
  else:
    checker()

###########################################################################
#-Game Loop-###############################################################
print("Welcome to D&C 'Early in The Morning Pepper Soup' Game")
play = input("Wanna Play? (Y/N): ").lower()
while play != 'y':
  break
else:
  checker()