'''
 => It is the ability to transform multiple forms then it is called as polymorphism.

  EX:
    => print(5+5)               here + operator is doing addition operation between two integer.
    => print('see' + 'facing')  here the + operator is doing concatenation operation between two strings.

=> In the polymorphism there is two process.
    1. overloading
    2. overriding

 => overloading:
      When the class contain more than one method with same name and different types of parameters then
      that is called as overloading.

class Greet:

    def sample(self):
       print('hello world')

    def sample(self):
       print('hii there')

g = Greet()
g.sample()
output = hii there ( because it takes the latest one)

=> overriding:
   when we are writing the method name with same signature in parent and child class then
   that is called overriding.

class Greet:

    def sample(self):
       print('hello world')

class Okgreet(Greet):

     def sample(self):
        super().sample()
        print('go there')

s = Okgreet()
s.sample()

=> here, when we call the sample method which is present in parent class by child class object
   instance then the child class sample method wil execute not parent class sample method.
   here the method overriding is happening.

'''


class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()