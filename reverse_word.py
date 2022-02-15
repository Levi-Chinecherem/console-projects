print("\nWelcome to D&C word Reversing System\n")
while True:
  print("Mirror Your Words with D&C")
  word = input("Enter word to mirror/reverse: \n")

  print("Your Mirror Says: ", end="")
  for i in reversed(word):
    print(i, end="")

  Again = input("\n\nMirror Another Word? (Y/N): ").lower()
  if Again != "y":
    break