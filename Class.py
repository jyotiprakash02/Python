'''1. wap to get the count of number of instances of a class that is being created'''

# class Sample:
#     count = 0
#
#     def __init__(self):
#         Sample.count += 1
#
# s1 = Sample()
# s2 = Sample()
# s3 = Sample()
# print(Sample.count)

'''2. write a cuatom class which can access the values of dictionaries using d['a'] and d.a  '''

# class MyDict:
#
#     def __init__(self, dict_):
#         self.dict_ = dict_
#
#     def __getitem__(self, item):
#         return self.dict_[item]
#
#     # def __getattr__(self, item):
#     #     return self.dict_[item]
#
# d = MyDict({'a':1, 'b':2})
# print(d['a'])
# print(d['b'])

'''3. write a class named Sample and it should have iteration capability'''

# class Sample:
#     def __init__(self, list_):
#         self.list_ = list_
#
#     def __iter__(self):
#         return iter(self.list_)
#
# s1 = Sample([1, 2, 3])
# for ele in s1:
#     print(ele)
#
# print(dir(Sample))

'''4. Can we override static method in Python'''
# class greet:
#
#     @staticmethod
#     def spam():
#         print('hello world')
#
#
# g = greet()
# g.spam()

'''5. what is the output'''

# class Demo:
#     def greet(self):
#         print('hello world')
#
#     def greet(self):
#         print('hello universe')
#
# d = Demo()
# d.greet()       #hello universe

'6. Can we have multiple init methods in a class'

# class Sample:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# sample_obj = Sample(1, 2, 3)
# print(sample_obj.a)     #1
# print(sample_obj.b)     #2
# print(sample_obj.c)     #3
#
# sample_obj_2 = Sample(1, 2)     #TypeError: __init__() missing 1 required positional argument: 'c'
