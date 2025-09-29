accounts={}
def create_account():
    name=input("Enter the name:")
    if name in accounts:
        print("your name is already exist")
        return
    pin=input("Enter the pin")
    accounts[name]={'pin':pin,'balance':0.0}
    print("your account sucessfully open")
def show_balance():
    name=input("Enter the name:")
    pin=input("Enter the pin:")
    if name in accounts and accounts[name]['pin']==pin:
        print("your account balance:",accounts[name]['balance'])
    else:
        print("you entered invalid pin and name")
def deposite_ammount():
    name=input("Enter the name:")
    pin=input("Enter the pin:")
    if(name in accounts and accounts[name]['pin']==pin):
        ammount=float(input("Enter the ammount:"))
        if(ammount<0):
            print("please enter valid ammount")
        else:
            accounts[name]['balance']=accounts[name]['balance']+ammount
            print("your deposite ammount:",ammount)
    else:
        print("plese entered valid pin and name")        
def withdraw_ammount():
    name=input("Enter the name:")
    pin=input("Enter the pin:")
    if(name in accounts and accounts[name]['pin']==pin):
        ammount=float(input("Enter the withdraw ammount"))
        if (ammount<=accounts[name]['balance']):
            accounts[name]['balance']=accounts[name]['balance']-ammount
            print("you withdraw ammount is:",ammount)
        else:
            print("your accounts balances is less",accounts['balance'])
    else:
        print("plese enter valid name and pin")
def change_pin():
    name=input("Enter the name:")
    pin=input("Enter the pin:")
    if(name in accounts and accounts[name]['pin']==pin):
        key=input("enter the 4 digit new pin")
        if(len(key)==4):
            print("your new  pin succesfully exsist:",key)
            accounts[name]['pin']=key
        else:
            print("please enter only 4 digit pin")
    else:
        print("plese entered valid pin and name")
def delete_account():
    name=input("Enter the name")
    pin=input("Enter the pin")
    if(name in accounts and accounts[name]['pin']==pin):
        del accounts[name]
        print("your account is sucessfuly delete")
def menu():
    print("------------ATM MACHINE----------")
    while True:
        print("********Menu*********\n")
        print("1.Create account")
        print("2.Show balance")
        print("3.Deposite ammount")
        print("4.withdraw ammount")
        print("5.Change pin")
        print("6.Delete account")
        print("7.Exit")
        x=int(input("Enter the no."))
        if(x==1):
            create_account()
        elif(x==2):
            show_balance()
        elif(x==3):
            deposite_ammount()
        elif(x==4):
            withdraw_ammount()
        elif(x==5):
            change_pin()
        elif(x==6):
            delete_account()
        elif(x==7):
            print("Thankyou for using the Atm")
        else:
            print("please chose valid no.")
menu()
    
