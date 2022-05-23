Accounts={
    0 :{
        'Name' :'System',
    'AccNo' : 0,
    'Mobile' : 00000,
    'Money' : 0,
    'AccType': 'c',
    'Password': '0000'
    }
}
Acno=[0]
def createacc(name):
    Acno.append(Acno[-1]+1)
    n=Acno[-1]
    Accounts[n]={}
    Accounts[n]['Name']=name
    pas=int(input("Enter a numeric Password for Your Account: "))
    Accounts[n]['PassWord']=pas
    Accounts[n]['AccNo']=n
    mob=int(input("Enter the mobile number to get a unique identity: "))
    Accounts[n]['Mobile']=mob
    mon=int(input("Enter the amount deposit in acc: "))
    Accounts[n]['Money']=mon
    typ=input("Enter the Account Type c/s: ")
    Accounts[n]['AccType']=typ
    print("You have been assigned a Account Number: "+ str(Accounts[n]['AccNo']) + " Remember this or Future")

def withdraw(n):
    print("========== Name: {} ==========\n==========Account Number {} ==========\n========== Money Available: {} ==========".format(Accounts[acno]['Name'],Accounts[acno]['AccNo'],Accounts[acno]['Money']))
    money=int(input("Enter the Ammount You want to Withdraw < {}: ".format(Accounts[acno]['Money'])))
    Accounts[acno]['Money']-=money
    print("Money Deducted successfully")
def deposit(n):
    money=int(input("Enter the Ammount You want to Deposit: "))
    Accounts[acno]['Money']+=money
    print("Money Deposited successfully")
    print("========== Name: {} ==========\n==========Account Number {} ==========\n========== Money Available: {} ==========".format(Accounts[acno]['Name'],Accounts[acno]['AccNo'],Accounts[acno]['Money']))
def display():
    for i in Accounts.keys():
        print("Account Number: {}\nHolder Name: {}\nAmmount: {}".format(Accounts[i]['AccNo'],Accounts[i]['Name'],Accounts[i]['Money']))
while True:
    print("************************************************************")
    print("========== WELCOME TO BANKING SYSTEM ==========")
    print("************************************************************")
    print("==========     (a). Open New Client Account     ============")
    print("==========     (b). The Client Withdraw a Money ============")
    print("==========     (c). The Client Deposit a Money  ============")
    print("==========     (d). Check Clients & Balance     ============")
    print("==========     (e). Quit                        ============")
    print("************************************************************")

    ch=input("Enter the Desired Option: ")
    if ch=='a':
        name=input("Enter the name of Client: ")
        createacc(name)

    elif ch=='b':
        acno=int(input("Enter the Account Number: "))
        if acno in Acno:
            while True:
                pasword=int(input("Enter the PassWord for your Account: "))
                if Accounts[acno]['PassWord']==pasword:
                    withdraw(acno)
                    break
                else:
                    print("Enter a correct password")
    elif ch=='c':
        acno=int(input("Enter the Account Number: "))
        if acno in Acno:
            while True:
                pasword=int(input("Enter the PassWord for your Account: "))
                if Accounts[acno]['PassWord']==pasword:
                    deposit(acno)
                    break
                else:
                    print("Enter a correct password")
    elif ch=='d':
        display()
    elif ch == "e":
        print("letter e is selected by the client")
        print("Thank you for using our banking system!")
        print("\n")
        print("Thank You and Come again")
        print("God Bless")
        break
    else:
        print("Invalid option selected by the Client")
        print("Please Try again!")

        #mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
