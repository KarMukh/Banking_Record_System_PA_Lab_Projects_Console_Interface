# Աշխատանքային ֆայլ
# Այս ֆայլի վրա ուղղակի ընթացքում փուձում էի տարբեր ձևեր, հետո վերջնականը մեյնում գրում


import pickle
import os
import pathlib


class Account:
    account_number = 0
    name = ''
    deposit = 0
    type = ''

    def create_account(self):
        self.account_number = int(input("Enter the account number : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = float(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")

    def show_account(self):
        print("Account Number : ", self.account_number)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modify_account(self):
        print("Account Number : ", self.account_number)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = float(input("Modify Balance :"))

    def deposit_amount(self, amount):
        self.deposit += amount

    def withdraw_amount(self, amount):
        self.deposit -= amount

    def transfer_amount(self, amount):
        self.deposit -= amount
        self.deposit += amount

    def report(self):
        print(self.account_number, " ", self.name, " ", self.type, " ", self.deposit)

    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.name

    def get_account_type(self):
        return self.type

    def get_deposit(self):
        return self.deposit


def intro():
    print("\t\t\t\tBANK REPORT SYSTEM")

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
            print(item.account_number, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def display_sp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.account_number == num:
                print("Your account Balance is = ", item.deposit)
                found = True
    else:
        print("No records to Search")
    # if not found:
    #     print("No existing record with this number")


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
                    print("Your account is updated")
                elif num2 == 2:
                    amount = float(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw larger amount")

    # else:
    #     print("No records to Search")
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
            account_number1 = int(input("Enter account number to withdraw from "))
            if item.account_number == account_number1:
                # if num2 == 1:
                amount = float(input("Enter the amount to transfer : "))
                if amount <= item.deposit:
                    item.deposit -= amount
                    print("Your account is updated")
                    for item1 in mylist:
                        account_number2 = int(input("Enter account number to transfer to "))
                        if item1.account_number == account_number2:
                            item1.deposit += amount
                            print("Your account is updated")

                else:
                    print("You cannot withdraw larger amount")

    # else:
    #     print("No records to Search")
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
                item.type = input("Enter the account Type : ")
                item.deposit = float(input("Enter the Amount : "))

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
    # system("cls");
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
    # system("cls");

    if choice == '1':
        write_account()
    elif choice == '2':
        num = int(input("\tEnter the account number. : "))
        deposit_and_withdraw(num, 1)
    elif choice == '3':
        num = int(input("\tEnter the account number. : "))
        deposit_and_withdraw(num, 2)
    elif choice == '4':
        transfer_money()
    elif choice == '5':
        num = int(input("\tEnter the account number. : "))
        display_sp(num)
    elif choice == '6':
        display_all()
    elif choice == '7':
        num = int(input("\tEnter the account number. : "))
        delete_account(num)
    elif choice == '8':
        num = int(input("\tEnter the account number. : "))
        modify_account(num)
    elif choice == '9':
        print("\tThanks for using bank report system")
        break
    else:
        print("Invalid choice")

    choice = input("Enter your choice : ")
