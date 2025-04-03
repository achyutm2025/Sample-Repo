#ATM MENU PROGRAMME

#Initial Balance in Bank
current=10000

#Function to Check Balance
def Check_Balance(current):
    money=current
    print(f"Rs.{current} is your current balance\n")

#Function To Deposit Amount    
def Deposit_Amt(amount):
    amt=current+amount
    print(f"The Rs.{amount} is Deposited Sucessfully\n")

#Function to Withdraw Amount    
def Withdraw_Amt(amount):
    amt=current-amount
    print(f"Rs.{amount} Withdrawl Sucessfully\n")

#First Loop For Pin Input
while(True):
    pin=int(input("Enter Your Pin : "))
    #Checking Pin Match
    if(pin==1234):
        #Second Loop For Genral Oprations
        while(True):
            print("Welcome to SBI\n")
            print("Select Option What You Want to do")
            print("1) Check Balance : ")
            print("2) Deposit Amount : ")
            print("3) Withdraw Amount : ")
            print("4) EXIT")

            option=int(input(("Select Option What You Want to do : ")))

            if option==1:
                Check_Balance(current)

            elif option==2:
                amount=int(input("Enter the amount you want to deposit : "))
                Deposit_Amt(amount)
                current=amount+current

            elif option==3:
                amount=int(input("Enter the amount you want to Withdraw : "))
                if(amount<current):
                    Withdraw_Amt(amount)
                    current=current-amount
                else:
                    print("Not Enough Balance")

            elif option==4:
                break
        
            else:
                print("Wrong Option Try Again")

            # import time
        break
         # time.sleep(2)
    else:
        print("Wrong Pin Try Again")