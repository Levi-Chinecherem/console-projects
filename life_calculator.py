
###########################################################################
#-Centuries and Years (High Order)-########################################
class HighOrder:
  def __init__(self, birth_year, current_year):
    self.birth_year = birth_year
    self.current_year = current_year

  def century(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    cent = abs(age/10.0)
    print(f"Congrats you have lived for {cent} centuries \nEqually you have live for {age} years.")

  def years(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    print(f"Congrats you have live for {age} years.")

###########################################################################
#-Low Order-###############################################################
class LowOrder(HighOrder):

  def months(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    month = age * 12
    print(f"You have lived for {month} months")

  def weeks(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    week = age * 12 * 52
    print(f"You have lived for {week} weeks")

  def days(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    day = age * 12 * 52 * 365
    print(f"You have lived for {day} days")

  def hours(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    hour = age * 12 * 52 * 365 * 24
    print(f"You have lived for {hour} hours")

  def seconds(self):
    self.birth_year = int(input("Year of Birth: "))
    self.current_year = int(input("Current Year: "))
    age = abs(self.birth_year - self.current_year)
    second = age * 12 * 52 * 365 * 24 * 60 * 60
    print(f"You have lived for {second} seconds")

###########################################################################
#-Choices-#################################################################
def choices():
  choice = int(input('''
  What do you wanna do first
    1. Number of Years
    2. Number of Months
    3. Number of Weeks
    4. Number of Days
    5. Number of Hours
    6. Number of Seconds
    7. Number of Centuries
    8. Exit
    '''))

  birth_year = current_year = 0
  high = HighOrder(birth_year, current_year)
  low = LowOrder(birth_year, current_year)

  if choice == 1:
    high.years()
  elif choice == 2:
    low.months()
  elif choice == 3:
    low.weeks()
  elif choice == 4:
    low.days()
  elif choice == 5:
    low.hours()
  elif choice == 6:
    low.seconds()
  elif choice == 7:
    high.century()
  elif choice == 8:
    while True:
      break
  else:
    again = input("Wrong Choice Try Again? (Y/N) ").lower()
    if again != 'y':
      while True:
        break

  again = input("Have more fun? (Y/N)").lower()
  while again != 'y':
    break
  else:
    choices()

###########################################################################
#-Control-#################################################################

print("Welcome to D&C live calculator")
play = input("Wanna have fun finding out stuffs about you? (Y/N): ").lower()
while play != 'y':
  break
else:
  choices()