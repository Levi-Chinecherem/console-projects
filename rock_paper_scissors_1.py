import random

def choices():
  while True:
    choices = ['ROCK', 'PAPER', 'SCISSORS']
    computer = random.choice(choices)
    player = input('Rock, Paper, or Scissors? ').upper()
    while player not in choices:
      player = input('Rock, Paper, or Scissors? ').upper()

    print('Computer:', computer)
    print('Player:', player)

    #############################################################
    #-Logic-#####################################################
    if player == computer or computer == player: 
      print('Tie!')

    if computer == 'ROCK' and player == 'PAPER':
      print('Player Wins!')
      if player == 'SCISSORS':
        print('Computer Wins!')

    if computer == 'PAPER' and player == 'SCISSORS':
      print('Player Wins!')
      if player == 'ROCK':
        print('Computer Wins!')

    if computer == 'SCISSORS' and player == 'ROCK':
      print('Player Wins!')
      if player == 'PAPER':
        print('Computer Wins!')

    play = input('Play? (Yes/No) ').upper()
    if play != 'YES':
      break
      
###############################################################
#-Call or Game Loop-###########################################
choices()