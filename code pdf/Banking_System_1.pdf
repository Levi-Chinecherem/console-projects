##############################################################################        
#-Universal-##################################################################
import time

balance = 0.0
account_number = None
security = None
runner = True
recievers = {}

username = input("Enter Username: ")
print("\n\nWelcome to D&C Banking System (Series One!)")
print(f"Username: {username} \nBalance: {balance}")
print("What would you like to do first?")

##############################################################################        
#-Commonness in Transactions-#################################################
class Transactions:
    def __init__(self, amount, acct_no, pin):
        
        self.acct_no = acct_no
        self.amount = amount
        self.pin = pin
    
##############################################################################        
#-Transactions-###################################################################
class Sub_Transactions(Transactions):
    
    def deposit(self):
        self.amount = int(input('Enter Amount: '))
        self.acct_no = input('Enter Account Number: ')
        self.pin = input('Enter 4 digit pin: ')
        depositors_name = input('Enter Depositors Name: ')
        balance =+ self.amount
        account_number = self.acct_no
        security = self.pin
        depo = [account_number, balance, security, depositors_name]
        recievers["Deposits"]=depo
        print("Money successfully deposited")
        time.sleep(2)
        home()
        
        
    def withdraw(self):
        self.amount = int(input('Enter Amount: '))
        self.acct_no = input('Enter Account Number: ')
        self.pin = input('Enter 4 digit pin: ')
        withdrawer_name = input('Enter Withdrawers Name: ')
        balance =+ self.amount
        account_number = self.acct_no
        security = self.pin
        witho = [account_number, balance, security, withdrawer_name]
        recievers["Withdraws"]=witho
        print('Successful Withdrawal!')
        time.sleep(2)
        home()
        
    def transfer(self):
        recievers_name = input('Enter Recievers Name: ')
        recievers_acct_no = input('Enter Recievers Account Number: ')
        senders_name = input('Enter Senders Name: ')
        balance =- self.amount
        account_number = self.acct_no
        security = self.pin
        transo = [account_number, balance, security, recievers_acct_no, recievers_name, senders_name]
        recievers["Transfers"]=transo
        print('You successfully transferred' + str(self.amount) +' to ' + recievers_acct_no +' '+ recievers_name + ' by name')
        time.sleep(2)
        home()
        
    def airtime(self):
        print('Airtime in Progress \n Choose who to recharge')
        who = int(input('1. Self \n2. Others'))
        
        if who == 1:
            balance =- self.amount
            account_number = self.acct_no
            security = self.pin
            selfo = [ account_number, balance, security ]
            recievers["Self Recharges"]=selfo
            print('Recharge Successful')
            time.sleep(2)
            home()
            
        elif who == 2:
            phone = input('Enter Recievers Number: ')
            network = input('Enter recievers network: ')
            balance =- self.amount
            account_number = self.acct_no
            security = self.pin
            otho = [ account_number, balance, security, phone, network ]
            recievers["Other Recharges"]=otho
            print('Recharge Successful!')
            time.sleep(2)
            home()
        else:
            again = input('Wrong input \nTry Again? (Y/N): ').lower()
            if again == 'y':
                Sub_Transactions.airtime()
            elif again == 'n':
                home()
            else:
                print('wrong again :( BYE!!!')
                
    def loan(self):
        name = input('Enter your name ')
        desc = input('Why do you need this loan? ')
        due_date = input('When can you pay back (Due Date)? ')
        repay_way = input('What means do you intend paying us back? ')
        balance =- self.amount
        account_number = self.acct_no
        security = self.pin
        loano = [ account_number, balance, security, name, desc, due_date, repay_way ]
        recievers["Loan"]=loano
        print('Loan Successful')
        time.sleep(2)
        home()
            
    
##############################################################################        
#-Records-####################################################################
class Record:
    
    def depo_record():
        print('Deposits')
        print(recievers["Deposits"])
        print('Done')
        return_home = input('Return Home? (Y/N): ').lower()
        if return_home == 'y':
                home()
        else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 

    def witho_record():
        print('Withdraws')
        print(recievers["Withdraws"])
        print('Done')
        return_home = input('Return Home? (Y/N): ').lower()
        if return_home == 'y':
                home()
        else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 
                
    def transo_record():
        print('Transfers')
        print(recievers["Transfers"])
        print('Done')
        return_home = input('Return Home? (Y/N): ').lower()
        if return_home == 'y':
                home()
        else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 
    
    def selfo_record():
        print('Self Recharges Records')
        print(recievers["Self Recharges"])
        print('Done')
        return_home = input('Return Home? (Y/N): ').lower()
        if return_home == 'y':
                home()
        else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 
        
    def otho_record():
       print('Others Recharges Record')
       print(recievers["Other Recharges"])
       print('Done')
       return_home = input('Return Home? (Y/N): ').lower()
       if return_home == 'y':
               home()
       else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 
           
    def loano_record():
       print('Loan Record')
       print(recievers["Loan"])
       print('Done')
       return_home = input('Return Home? (Y/N): ').lower()
       if return_home == 'y':
               home()
       else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False 
        
    def all_record():
        print('Record of all transactions!\n')
        print('Deposits')
        print(recievers["Deposits"])
        print('Withdraws')
        print(recievers["Withdraws"])
        print('Transfers')
        print(recievers["Transfers"])
        print('Self Recharges Records')
        print(recievers["Self Recharges"])
        print('Others Recharges Records')
        print(recievers["Other Rec5harges"])
        print('Done')
        
        return_home = input('Return Home? (Y/N): ').lower()
        if return_home == 'y':
                home()
        else:
            print(':) BYE!!!')
            time.sleep(3)
            runner = False
     
        
##############################################################################        
#-Home-#######################################################################
def home():
    dep = Sub_Transactions(balance, account_number, security)
    print("NOTE: \n\tOnly use 6 when you have performed every other Transactions \n\tAgain never use any Record if you have not performed any transaction")
    action = int(input('''
                    1. Deposit \n
                    2. Withdraw \n
                    3. Transfer \n
                    4. Airtime \n
                    5. Loan \n
                    6. Records \n
                    7. Exit
                       '''))
    if action == 1:
        dep.deposit()
    elif action == 2:
        dep.withdraw()
    elif action == 3:
        dep.transfer()
    elif action == 4:
        dep.airtime()
    elif action == 5:
        dep.loan()
        
    elif action == 6:
        check_records = int(input('''
                       1. Deposit Record \n
                       2. Withdraw Record \n
                       3. Transfer Record \n
                       4. Airtime Record \n
                       5. Loan Records \n
                       6. All Records
                       '''))
        if check_records == 1:
            Record.depo_record()
        elif check_records == 2:
            Record.witho_record()
        elif check_records == 3:
            Record.transfo_record()
            
        elif check_records == 4:
            check_airtime = int(input('''
                       1. Self Recharged Record \n
                       2. Others Recharged Record
                       '''))
            if check_airtime == 1:
                Record.selfo_record()
            elif check_airtime == 2:
                Record.otho_record()
            else:
                tryAgain = input('Wrong Response Try Again? (Y/N): ').lower()
                if tryAgain == 'y':
                        home()
                else:
                    print(':) BYE!!!')
                    time.sleep(3)
                    runner = False 
        elif check_records == 5:
            Record.loano_record()    
        elif check_records == 6:
            Record.all_record()
        else:
            tryAgain = input('Wrong Response Try Again? (Y/N): ').lower()
            if tryAgain == 'y':
                    home()
            else:
                print(':) BYE!!!')
                time.sleep(3)
                runner = False
        
    elif action == 7:
        runner = False
    else:
        again = input('Wrong input \nTry Again? (Y/N): ').lower()
        if again == 'y':
            home()
        elif again == 'n':
            runner = False
        else:
            print('wrong again :( BYE!!!')
            runner = False
            
##############################################################################        
#-Executor-###################################################################
while not runner:
    break
else:
    home()
