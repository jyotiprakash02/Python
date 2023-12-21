'''
Inheritance

  => The process of transform and reflect the properties, characters of the parent class in child class is called
   inheritance
  =>In the inheritance parents class will execute first and then child class.

  => There is 5 types of inheritances
     1. single inheritance
     2. multi inheritance
     3. multi level inheritance
     4. Hierarchical inheritance
     5. Hybrid inheritance

    => single inheritance
       If one child class has one parent class then that type of inheritance is called single inheritance.
    => multi inheritance
       If one child class has more than one parent class then that type of inheritance is called multi inheritance.
    => multi level inheritance
       If there is an intermediate class is present in between child class and parent class then that type of
       inheritance is called as multi level inheritance.
    => Hierarchical inheritance
       If one parent class more than one child classes then that type of inheritance is called Hierarchical
       inheritance.
    => Hybrid inheritance
       It combines multiple inheritances with multilevel inheritance. one child class can have two or more parent
       classes, but only one of them can have derived classes.
'''

class Logger:

    def sample(self):
        print('python is a language')

    def greeet(self):
        print('C is the mother of all the language')


l1 = Logger()
l1.sample()


class Consolelogger(Logger):

    def sample(self):
        print('Selenium is a library')

    def track(self):
        print('webdriver is an interface')
        self.greeet()


C1 = Consolelogger()
C1.track()
C1.sample()


# Output
# python is a language
# webdriver is an interface
# C is the mother of all the language
# Selenium is a library



























