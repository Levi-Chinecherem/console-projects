import time

while True:
  print("Welcome to make a new word with D&C")
  mainPhrase = input("Enter the Sentence to derive your new word from: ")
  choices = [1, 2, 3, 4, 5]

  def beginning():
    length = int(input("Enter length of word from beginning: "))
    output = mainPhrase[ : length + 1]
    print("Processing...")
    time.sleep(2)
    print(f"Your new word is: { output }")
    print(f"Having length of: { int(len(output) - 1) }")
    play_again = input("\nWanna Try Another Word? (Y/N): ").upper()

  def in_between():
    length_start = int(input("Enter length from where to start: "))
    length_stop = int(input("Enter length of where to stop: "))
    output = mainPhrase[length_start : length_stop + 1]
    print("Processing...")
    time.sleep(2)
    print(f"Your new word is: { output }")
    print(f"Having length of: { int(len(output) - 1) }")

  def ending():
    length = int(input("Enter length of word counting from right to left: "))
    output = mainPhrase[length : ]
    print("Processing...")
    time.sleep(2)
    print(f"Your new word is: { output }")
    print(f"Having length of: { int(len(output) - 1) }")

  def all():
    print("Processing...")
    time.sleep(2)
    print(f"Your word is: { mainPhrase }")
    print(f"Having length of: { len(mainPhrase) }")

  player = None
  while player not in choices:
    player = int(input("Make new word from? \n1. beginning \n2. in-between \n3. ending \n4. All \n5. Exit: "))

  if player == 1:
    beginning()
  elif player == 2:
    in_between()
  elif player == 3:
    ending()
  elif player == 4:
    all()
  elif player == 5:
      break

