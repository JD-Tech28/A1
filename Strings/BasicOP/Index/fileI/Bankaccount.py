class bank():
    def __init__(self,Bank_acc_no,Bank_balance):
        self.acc=Bank_acc_no
        self.bal=Bank_balance

    def credit(self,amount):
        self.bal+=amount
        print(amount,"is credited\ncurrent bal:",self.bal)
        return

    def debit(self,amount):
        if amount>self.bal:
            print("Insufficient balance:",self.bal)
        else:
            self.bal-=amount
            print(amount,"is debited\ncurrrent bal:",self.bal)
            return
            
c1=bank(1234,5000)
c1.credit(2000)
c1.debit(3000)
c1.debit(4000)