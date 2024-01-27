from Account import * 
class Bank():
    
    def __init__(self):
        self.accountDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountDict[newAccountNumber] = oAccount

        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account?')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for this account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()
    
    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you.')
            del self.accountDict[userAccountNumber]
            print('Your Account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)
    
    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountDict:
            oAccount = self.accountDict[userAccountNumber]
            print('     Account:', userAccountNumber)
            oAccount.show()
    
    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None: 
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

        





    


    





