from Account import * 

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Created an account for Joe')

oMarysAccout = Account('Mary', 12345, 'MarysPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccout.show()
print()

print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccout.withdraw(345, 'MarysPassword')
oMarysAccout.deposit(100, 'MarysPassword')

oJoesAccount.show()
oMarysAccout.show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", userBalance)

oNewAccount.show()


