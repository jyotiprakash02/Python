'''
Encapsulation

=> The process of wrapping the data and methods inside single unit and restrict the data and variables
   outside the class is called Encapsulation.
=> By following the encapsulation we can prevent the accidental modification of data.

=> By using Getter and setter we can achieve encapsulation as well as by Access modifier
=> In the getter and setter we set the value by setter and display it by getter.
=> In the getter and setter we set the value in the a, b but when we execute the by the object instance
   then we can see that the value of a and b have sited in __a, __b.

'''


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise Exception('Only integer are allowed')
        else:
            self.__a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise Exception('only int are allowed')
        else:
            self._b = value


c = Calculator(3, 2)
c.a = 5
print(c.__dict__)


class Telephone:

    def __init__(self, consumer_name, billing_account_number, telephone_number):
        self.consumer_name = consumer_name
        self.__billing_account_number = billing_account_number
        self.telephone_number = telephone_number

    def telephone_number(self):
        print(f'the telephone number of the {self.consumer_name} is {self.telephone_number}')

    def account_number(self):
        print(f'the billing account number is {self.__billing_account_number}')
        print(self.__billing_account_number)


class Telephone_bill_payment(Telephone):

    def current_month_bill(self):
        print(f'the current month bill is 1000')
        super().account_number()

    def customer_name(self):
        print(f'alok is our 1st customer')


t = Telephone_bill_payment('alok', 15968, '06788-242013')
t.current_month_bill()
t.account_number()




