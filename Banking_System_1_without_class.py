##############################################################################        
#-Universal-##################################################################
import time

balance = 0.0
account_number = None
security = None
runner = True
recievers = []
amount = int(input('Enter Amount: '))
acct_no = input('Enter Account Number: ')
pin = input('Enter 4 digit pin: ')

##############################################################################        

def deposit():
    depositors_name = input('Enter Depositors Name: ')
    print("Money successfully deposited")
    balance =+ amount
    account_number = acct_no
    security = pin
    depo = [account_number, balance, security, depositors_name]
    recievers.append(depo) 
    
    
def withdraw():
    withdrawer_name = input('Enter Withdrawer Name: ')
    print('Successful Withdrawal!')
    balance =- amount
    account_number = acct_no
    security = pin
    witho = [account_number, balance, security, withdrawer_name]
    return witho
    
def transfer():
    recievers_name = input('Enter Recievers Name: ')
    recievers_acct_no = input('Enter Recievers Account Number: ')
    senders_name = input('Enter Senders Name: ')
    print('You successfully transferred' + str(amount) +' to ' + recievers_acct_no +' '+ recievers_name + ' by name')
    balance =- amount
    account_number = acct_no
    security = pin
    transo = [account_number, balance, security, recievers_acct_no, recievers_name, senders_name]
    return transo

def airtime():
    print('Airtime in Progress \n Choose who to recharge')
    who = int(input('1. Self \n2. Others'))
    
    if who == 1:
        print('Recharge Successful')
        balance =- amount
        account_number = acct_no
        security = pin
        selfo = [ account_number, balance, security ]
        return selfo
    elif who == 2:
        phone = input('Enter Recievers Number: ')
        network = input('Enter recievers network: ')
        print('Recharge Successful!')
        balance =- amount
        account_number = acct_no
        security = pin
        otho = [ account_number, balance, security, phone, network ]
        return otho
    else:
        again = input('Wrong input \nTry Again? (Y/N): ').lower()
        if again == 'y':
            airtime()
        elif again == 'n':
            home()
        else:
            print('wrong again :( BYE!!!')
            
def loan():
    name = input('Enter your name ')
    desc = input('Why do you need this loan? ')
    due_date = input('When can you pay back (Due Date)? ')
    repay_way = input('What means do you intend paying us back? ')
    print('Loan Successful')
    balance =- amount
    account_number = acct_no
    security = pin
    loano = [ account_number, balance, security, name, desc, due_date, repay_way ]
    return loano
        
    
##############################################################################        
#-Records-####################################################################

def depo_record():
    print('Deposition Record!')
    out = deposit()
    for value in out:
        print(out)
    print('Done')
    return_home = input('Return Home? (Y/N): ').lower()
    if return_home == 'y':
            home()
    elif return_home == 'n':
        print(':) BYE!!!')
        time.sleep(3)
        runner = False

def witho_record():
    print('Withdrawal Record!')
    out = withdraw()
    for value in out:
        print(out)
    print('Done')
    return_home = input('Return Home? (Y/N): ').lower()
    if return_home == 'y':
            home()
    elif return_home == 'n':
        print(':) BYE!!!')
        time.sleep(3)
        runner = False
            
def transo_record():
    print('Deposition Record!')
    out = transfer()
    for value in out:
        print(out)
    print('Done')
    return_home = input('Return Home? (Y/N): ').lower()
    if return_home == 'y':
            home()
    elif return_home == 'n':
        print(':) BYE!!!')
        time.sleep(3)
        runner = False

def selfo_record():
    print('Deposition Record!')
    out = airtime.selfo
    for value in out:
        print(out)
    print('Done')
    return_home = input('Return Home? (Y/N): ').lower()
    if return_home == 'y':
            home()
    elif return_home == 'n':
        print(':) BYE!!!')
        time.sleep(3)
        runner = False
    
def otho_record():
   print('Deposition Record!')
   out = airtime()
   for value in out:
       print(out)
   print('Done')
   return_home = input('Return Home? (Y/N): ').lower()
   if return_home == 'y':
           home()
   elif return_home == 'n':
       print(':) BYE!!!')
       time.sleep(3)
       runner = False  
    
def all_record():
    print('Record of all transactions!\n')
   
    print('Deposits')
    print(deposit())
    print('Withdraws')
    print(withdraw())
    print('Transfers')
    print(transfer())
    print('Self Recharges')
    print(airtime())
    print('Others Recharges')
    print(airtime())
    print('Done')
    
    return_home = input('Return Home? (Y/N): ').lower()
    if return_home == 'y':
            home()
    elif return_home == 'n':
        print(':) BYE!!!')
        time.sleep(3)
        runner = False
     
        
##############################################################################        
#-Home-#######################################################################
def home():
    username = input("Enter Username: ")
    print("\n\nWelcome to D&C Banking System (Series One!)")
    print(f"Username: {username} \nBalance: {balance}")
    print("What would you like to do first?")
    action = int(input('''
                    1. Deposit \n
                    2. Withdraw \n
                    3. Transfer \n
                    4. Airtime \n
                    5. Loan \n
                    6. Records \n
                    7. Back \n
                    8. Exit
                       '''))
    if action == 1:
        deposit()
    elif action == 2:
        withdraw()
    elif action == 3:
        transfer()
    elif action == 4:
        airtime()
    elif action == 5:
        loan()
        
    elif action == 6:
        check_records = int(input('''1. Deposit Record \n
                       2. Withdraw Record \n
                       3. Transfer Record \n
                       4. Airtime Record \n
                       5. All Records
                       '''))
        if check_records == 1:
            depo_record()
        elif check_records == 2:
            witho_record()
        elif check_records == 3:
            transo_record()
            
        elif check_records == 4:
            check_airtime = int(input('''1. Self Recharged Record \n
                       2. Others Recharged Record
                       '''))
            if check_airtime == 1:
                selfo_record()
            elif check_airtime == 2:
                otho_record()
            else:
                print("Wrong Input Bye!!")
                Universalrunner = False
            
        elif check_records == 5:
            all_record()
        else:
            print("Wrong Input Bye!!")
            Universalrunner = False
        
    elif action == 7:
        Universalrunner = False
    elif action == 8:
        home = False
    else:
        again = input('Wrong input \nTry Again? (Y/N): ').lower()
        if again == 'y':
            home()
        elif again == 'n':
            Universalrunner = False
        else:
            print('wrong again :( BYE!!!')
            runner = False
    print(recievers)
            
##############################################################################        
#-Executor-###################################################################
while runner:
    home()
else:
    while not runner:
        break

    


        