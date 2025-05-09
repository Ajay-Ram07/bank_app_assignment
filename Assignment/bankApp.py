# Unicom Online Banking Application===============================================================================================
#Function - 01 
#[Function For Generating Account Numbers]

def generateAc_num():

    account_num = 10032
    count = 0

    try:

        with open("accountDetails.txt", "r") as file:
            for _ in file:
                count += 1

    except FileNotFoundError:
        pass

    return str(account_num + count)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 02
#[Function For Create Account ]


def createAccount():

    print("\n-*-*-*-*-*-Create [Unicom-Online-Banking] Account-*-*-*-*-*-*-")

    name = input("Enter Your username For Creating Account :").strip()
    password = input("Create a Password For your Account :").strip()

    while True:

        try:

            firstDep = float(input("Enter Your Account Opening Amount [Minimum 500.00] :"))

            if firstDep < 500:
                print("Please Deposit 500.00 or more than 500.00 for Creating Account !")

            else:
                break

        except ValueError:
            print("Please enter Valid Value For Deposit !!!")

    accountNumber = generateAc_num()

    with open("accountDetails.txt", "a") as file:
        file.write(f"{accountNumber},{name},{password},{firstDep}\n")

    print(f"\nHey {name}!, Your Account Created Successfully.! \nYour Account Number is {accountNumber}.")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 03
#[Function For Login Account ]

def login():

    print("\n-*-*-*-*-*-Login [Unicom-Online-Banking] Account-*-*-*-*-*-*-")

    accNo = input("Enter Your Account Number :").strip()
    inPassword = input("Enter Your Account Password For Login :").strip()

    with open("accountDetails.txt", "r") as file:

        for line in file:
            data = line.strip().split(",")

            if data[0] == accNo and data[2] == inPassword:
                print(f"\nLogin Successful!,\nWelcome {data[1]}")
                return accNo
            
    print("Login Inputs [Account Number / Password] incorrect.\nPlease Try Again..")
    return None

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 04
#[Function For Deposit ]


def deposit(account_num):
    
    print("\n-*-*-*-*-*-Deposit Page [Unicom-Online-Banking] -*-*-*-*-*-*-")
    try:
        depoAmo = float(input("\nEnter Your Deposit Amount Value Here [Minimum-100.00]:"))
        if depoAmo < 100:
            print("Please Enter Valid Amount Value For Deposit...")
            return
    except ValueError:
        print("\nPlease Enter Valid Inputs")
        return

    lines = []
    find = False

    with open("accountDetails.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == account_num:
                updateBal = float(data[3]) + depoAmo
                data[3] = str(updateBal)
                find = True
                print(f"Your Amount {depoAmo} is Deposited Successfully,\nYour Current Balance is {updateBal}.")
            lines.append(",".join(data))

    if find:
        with open("accountDetails.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")

        with open("transactionHistory.txt", "a") as file:
            file.write(f"{account_num},Deposit,{depoAmo}\n")
    else:
        print("Account Not Found!!!")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 05
#[Function For Withdrawal]



def withdrawal(account_num):
    print("\n-*-*-*-*-*-Withdrawal Page [Unicom-Online-Banking] -*-*-*-*-*-*-")
    try:
        withAmo = float(input("Enter Amount Value For Withdraw :"))
        if withAmo <= 0:
            print("\nPlease Enter Valid Value For Withdraw !")
            return
    except ValueError:
        print("Invalid Inputs, Please Try Again")
        return

    find = False
    lines = []

    with open("accountDetails.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == account_num:
                balance = float(data[3])
                if withAmo > balance:
                    print("Your Account Balance is Insufficient!!!")
                    return
                else:
                    balance -= withAmo
                    data[3] = str(balance)
                    find = True
                    print(f"Withdrawal Successful,\nYour Updated Balance is: {balance}")
            lines.append(",".join(data))

    if find:
        with open("accountDetails.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")
        with open("transactionHistory.txt", "a") as file:
            file.write(f"{account_num},Withdraw,{withAmo}\n")
    else:
        print("Account Not Found!!!")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 06
#[Function For Check Balance ]



def check_balance(account_num):
    print("\n-*-*-*-*-*-Check Balance Page [Unicom-Online-Banking] -*-*-*-*-*-*-")
    with open("accountDetails.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == account_num:
                print(f"Hi {data[1]}, Your Current Balance is: {data[3]}")
                return
    print("Account not Defined...!")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 07
#[Function For Transaction Activity ]



def transActivity(account_num):
    print("\n-*-*-*-*-*-View Transaction Activity [Unicom-Online-Banking] -*-*-*-*-*-*-")
    find = False
    try:
        with open("transactionHistory.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == account_num:
                    print(f"{data[1]} of Rs.{data[2]}")
                    find = True
        if not find:
            print("Transaction History not Available!")
    except FileNotFoundError:
        print("No Transaction History File Found!")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Function - 08
#[Function For UserMenu ]



def userMenu(account_num):
    while True:
        print("\n-*-*-*-*-*- [Unicom-Online-Banking] -*-*-*-*-*-*-")
        print("\n-*-*-*-*-*- [User-Menu] -*-*-*-*-*-*-")
        print("01. Deposit Money --- [Enter: 1]")
        print("02. Withdraw Money --- [Enter: 2]")
        print("03. Check Balance --- [Enter: 3]")
        print("04. View Transaction Activity --- [Enter: 4]")
        print("05. Log-out/Exit --- [Enter: 5]")

        try:
            choice = int(input("Enter Your Choice [1-5]: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            deposit(account_num)
        elif choice == 2:
            withdrawal(account_num)
        elif choice == 3:
            check_balance(account_num)
        elif choice == 4:
            transActivity(account_num)
        elif choice == 5:
            print("Logging Out. Thank You For Choosing [Unicom-Online-Banking]!")
            break
        else:
            print("Invalid Choice. Please Enter a number between [1-5].")


# ===================== Main Control ========================

print("\n-*-*-*-*-*- [Unicom-Online-Banking] -*-*-*-*-*-*-")
print("1. Create a New Account [A]")
print("2. Login to Existing Account [B]")

choice = input("Enter your Choice [A/B]: ").upper()

if choice == "A":
    createAccount()
elif choice == "B":
    acc = login()
    if acc:
        userMenu(acc)
else:
    print("Invalid Choice. Please Enter A or B.")
