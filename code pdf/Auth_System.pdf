#########################################################################
###########################-Universal-###################################
# Building a Authentication System WITHOUT Database (Series 1)
import time

runner = True
usernames = []
passwords = []
emails = []

#########################################################################
###########################-Login-#######################################
def login():
    user1 = input("Username: ")
    pass1 = input("Password: ")
    
    if  user1 in usernames and pass1 in passwords:
        print("Checking Logging...")
        time.sleep(2)
        print("Logged in Successfully\n")
        final()
    else:
        print("\nUsername or Password not found!")
        ask = input("Try Again (Y/N)").lower()
        if ask == 'y':
            login()
        if ask == 'n':
            control()
            
#########################################################################
###########################-Registeration-###############################
def register():
    user1 = input("Username: ")
    pass1 = input("Password: ")
    mail = input("Email: ")
    
    if user1 in usernames:
        print("Username Taken!")
        new_user1 = input("New Username: ")
        if new_user1 in usernames:
            print("Username Taken!")
            register()
        else:
            usernames.append(new_user1)
            passwords.append(pass1)
            emails.append(mail)
            time.sleep(2)
            print("Done!!!")
            print("Proseed to login")
            time.sleep(2)
            login()
    else:
        usernames.append(user1)
        passwords.append(pass1)
        emails.append(mail)
        time.sleep(2)
        print("\nUsername, Password, and Email Successful")
        print("Proceed to login")
        time.sleep(2)
        login()

#########################################################################
###########################-Exit-########################################

def exit():
    Universalrunner = False

#########################################################################
###########################-Exit-########################################
def final():
    print("Thanks alot for checking in \nWe at D&C are grateful having you here!")
    print("Bye!!")
    time.sleep(6)


#########################################################################
###########################-Control-#####################################
def control():
    print(" \nWelcome to D&C Authentication System\n Hope you enjoy your stay here!\n")
    print("What would you like to do first?")
    response = int(input(" 1. Login\n 2. Register\n 3. Exit: \n"))
    if response == 1:
        login()
    elif response == 2:
        register()
    elif response == 3:
        exit()
    else:
        print("Wrong Input, Use only numbers")
        tryAgain = input("Try Again? Y/N: ").lower()
        if tryAgain == 'y':
            control()
        elif tryAgain == 'n':
            print("Thanks For Checking Out The System \nBye!")
        else:
            print("Wrong Again :( BYE!!!")
            Universalrunner = False

#########################################################################
###########################-Main-########################################

while not runner:
    break
else:
    control()
