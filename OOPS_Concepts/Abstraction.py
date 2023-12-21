'''There is two methods by which we can achieve abstractions
 1. Abstract class
 2. Interface

*Abstract class:
    => In a class if any one method decorated with @abstractmethod then that entire class is called as abstract class.
    => We cannot create the object instance or cannot perform execution inside the abstract class but the execution 
       and object creation can possible outside the abstract class means through any other class.
    => Abstract class can carry one or more then one, both normal method as well as abstract method.
    => To create abstract class we have to import the abstract module as 
       from abc import ABC, abstractmethod

* Interface:
    => It is similar to the Abstract class but the main difference is, in the interface have only 
       Abstract method no other normal methods.
'''

'''Abstract Class'''

from abc import ABC, abstractmethod

class Logger:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class Textfilelogger(Logger):

    def __int__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def mul(self):
        return self.a * self.c

    def greet(self):
        print('All students are good in python')


L1 = Logger(1, 2)
print(L1.add())
print(L1.sub())
L2 = Textfilelogger(1, 2)
L2.greet()

'Output'
# 3
# -1
# All students are good in python'


'''Interface'''

from abc import ABC, abstractmethod

class Logger:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def add(self):
        return self.a + self.b

    @abstractmethod
    def sub(self):
        return self.a - self.b


class Textfilelogger(Logger):

    def __int__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def mul(self):
        return self.a * self.c

    def greet(self):
        print('All students are good in python')


L1 = Logger(1, 2)
print(L1.add())
print(L1.sub())
L2 = Textfilelogger(1, 2)
L2.greet()

'Output'
# 3
# -1
# All students are good in python'









