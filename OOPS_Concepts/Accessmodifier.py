'''
There is three types of access modifiers
 1. Public
 2. Protected _     Ex _variable
 3. private   __    EX __variable

Public:    we can access this type of variable anywhere, means inside any classes
protected: we can also access it anywhere, means inside any classes but we should not do it
private:   we cannot access it any other classes but it can only accessible in it's own class inside any method. 
           Also we can access it in other class, by passing that private variable inside it's own class anyone method
           and call that method inside the inherit class. Then we can access that variable.
'''


class Bankaccount:  
    
    __total_amount = 50000

    def __init__(self, deposit, account_number, amount, withdraw):
        self.deposit = deposit
        self._account_number = account_number
        self.__amount = amount
        self.withdraw = withdraw

    def add_money(self):
        if self.deposit == 0:
            print(f'unable to deposit')
        else:
            self.__amount = self.__amount + self.deposit
            print(f'the recent amount is {self.__amount}')

    def withdraw_money(self):
        if self.__amount <= 0:
            print('insufficient balance')
        else:
            self.__amount = self.__amount - self.withdraw
            print(f'the withdraw amount is {self.__amount}')
            print(f'{self.__total_amount}')


B1 = Bankaccount(1000, 12354, 10000, 500)
B1.add_money()
B1.withdraw_money()


class Saving_bankaccount(Bankaccount):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(1000, 2000, 3000, 4000)

    def lone_deposit(self):
        print(f'the lone account number is {self._account_number}')
        super().add_money()
        # print(self._total_amount)


B2 = Saving_bankaccount(100,200)
B2.lone_deposit()
B2.add_money()


