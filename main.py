import pickle
import os
import pathlib


class Account:
    account_number = 0
    name = ''
    deposit = 0

    def create_account(self):
        self.account_number = int(input("Enter the account number : "))
        self.name = input("Enter the account holder name : ")
        self.deposit = float(input("Enter the initial amount :"))
        print("\n\n\nAccount Created")

    def show_account(self):
        print("Account number : ", self.account_number)
        print("Account holder name : ", self.name)
        print("Balance : ", self.deposit)

    def modify_account(self):
        print("Account number : ", self.account_number)
        self.name = input("Modify account holder name :")
        self.deposit = float(input("Modify balance :"))

    def deposit_amount(self, amount):
        self.deposit += amount

    def withdraw_amount(self, amount):
        self.deposit -= amount

    def transfer_amount(self, amount):
        self.deposit -= amount
        self.deposit += amount

    def report(self):
        print(self.account_number, " ", self.name, " ", self.deposit)

    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.name

    def get_deposit(self):
        return self.deposit


def intro():
    print("\n\t\t\t\t*** BANK REPORT SYSTEM ***")

    print("\nPress enter and make your choice ")

    input()


def write_account():
    account = Account()
    account.create_account()
    write_accounts_file(account)


def display_all():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.account_number, " ", item.name, " ", item.deposit)
        infile.close()
    else:
        print("No records to display!")


def show_account_balance(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        for item in mylist:
            if item.account_number == num:
                print("Your account balance is = ", item.deposit)
                # found = True
    else:
        print("No records to Search!")



def deposit_and_withdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.account_number == num1:
                if num2 == 1:
                    amount = float(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updated!")
                elif num2 == 2:
                    amount = float(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw larger amount!")


        outfile = open('new_accounts.data', 'wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('new_accounts.data', 'accounts.data')


def transfer_money():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            account_number1 = int(input("Enter account number to transfer from :"))
            if item.account_number == account_number1:
                amount = float(input("Enter the amount to transfer :"))
                if amount <= item.deposit:
                    item.deposit -= amount
                    print("Withdraw account is updated!")
                    for item1 in mylist:
                        account_number2 = int(input("Enter account number to transfer to :"))
                        if item1.account_number == account_number2:
                            item1.deposit += amount
                            print("Deposit account is updated!")

                else:
                    print("You cannot withdraw larger amount!")


        outfile = open('new_accounts.data', 'wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('new_accounts.data', 'accounts.data')


def delete_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_list = pickle.load(infile)
        infile.close()
        new_list = []
        for item in old_list:
            if item.account_number != num:
                new_list.append(item)
        os.remove('accounts.data')
        outfile = open('new_accounts.data', 'wb')
        pickle.dump(new_list, outfile)
        outfile.close()
        os.rename('new_accounts.data', 'accounts.data')


def modify_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_list = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in old_list:
            if item.account_number == num:
                item.name = input("Enter the account holder name : ")
                item.deposit = float(input("Enter the amount : "))

        outfile = open('new_accounts.data', 'wb')
        pickle.dump(old_list, outfile)
        outfile.close()
        os.rename('new_accounts.data', 'accounts.data')


def write_accounts_file(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        old_list = pickle.load(infile)
        old_list.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        old_list = [account]
    outfile = open('new_accounts.data', 'wb')
    pickle.dump(old_list, outfile)
    outfile.close()
    os.rename('new_accounts.data', 'accounts.data')


choice = ''
num = 0
intro()

while choice != 9:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. TRANSFER MONEY")
    print("\t5. SHOW ACCOUNT BALANCE")
    print("\t6. DISPLAY ALL ACCOUNTS")
    print("\t7. DELETE ACCOUNT")
    print("\t8. MODIFY AN ACCOUNT")
    print("\t9. EXIT")
    print("\tSelect Your Option (1-9) ")
    choice = input()


    if choice == '1':
        write_account()
    elif choice == '2':
        num = int(input("\tEnter the account number to deposit to : "))
        deposit_and_withdraw(num, 1)
    elif choice == '3':
        num = int(input("\tEnter the account number to withdraw from : "))
        deposit_and_withdraw(num, 2)
    elif choice == '4':
        transfer_money()
    elif choice == '5':
        num = int(input("\tEnter the account number to show the balance : "))
        show_account_balance(num)
    elif choice == '6':
        display_all()
    elif choice == '7':
        num = int(input("\tEnter the account number to delete : "))
        delete_account(num)
    elif choice == '8':
        num = int(input("\tEnter the account number to modify : "))
        modify_account(num)
    elif choice == '9':
        print("\tThanks for using bank report system")
        break
    else:
        print("Invalid choice")

    choice = input("Press enter and make your choice ")
