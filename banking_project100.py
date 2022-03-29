class ATM(object):
    def __init__(self, balance):
        self.balance = balance

    def checkBalance(self):
        print("Current balance is " + str(self.balance))
    
    def withdrawMoney(self, amountToWithdraw):
        if(amountToWithdraw <= self.balance):
            self.balance = self.balance - amountToWithdraw
            print("Current balance is " + str(self.balance))
        else:
            print("Insufficient funds")
    
    def depositMoney(self, amountToDeposit):
        self.balance = self.balance + amountToDeposit
        print("Current balance is " + str(self.balance))

account = ATM(100)
print("Press 1 for checking balance")
print("Press 2 to withdraw money")
print("Press 3 to deposit money")

service = int(input("Enter service to be availed "))

if (service == 1):
    account.checkBalance()
elif (service == 2):
    withdrawAmount = int(input("Enter amount to withdraw"))
    account.withdrawMoney(withdrawAmount)
elif (service == 3):
    depositAmount = int(input("Enter amount to deposit"))
    account.depositMoney(depositAmount)
else:
    print("Invalid input")
