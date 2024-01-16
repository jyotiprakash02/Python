''' 1. write a decorator which will convert negative numbers to positive number'''

# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @positive       # add = positive(add)
# def add(a, b):
#     return a + b
#
# print(add(-12,-10))

'2. write a decorator to print prefix +91 to the original phone num'

# numbers = 7978425565

# def prefix_code(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return "+91"+str(result)
#     return wrapper
#
# @prefix_code        #ph_num = prefix_code(ph_num)
# def ph_num(num):
#     return num
#
# print(ph_num(numbers))

'''3.write a decorator to reverse the string'''

# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
# @outer      #string_ = outer(string_)
# def string_(str_):
#     return str_
#
# print(string_('python'))
# print(string_('selenium'))

'4.write a decorator print the total length of the positional and keyword arguments'

# def outer(func):
#     def wrapper(*args, **kwargs):
#         total = len(args) + len(kwargs)
#         print(total)
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #spam = outer(spam)
# def spam(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# spam(1, 2, 3, 4, 5, a=10, b=20, c=30, d=100, z=10000, m='hai')

# Alternative method
# def outer(func):
#     def wrapper(*args, **kwargs):
#         total = 0
#         for _ in args:
#             total += 1
#         for _ in kwargs:
#             total += 1
#         print(total)
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #spam = outer(spam)
# def spam(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# spam(1, 2, 3, 4, 5, a=10, b=20, c=30, d=100, z=10000, m='hai')

'5.write a decorator to find total number of positional arguments and keyword arguments separately'

# def outer(func):
#     def wrapper(*args, **kwargs):
#         total_args = 0
#         total_kwargs = 0
#         for _ in args:
#             total_args += 1
#         for _ in kwargs:
#             total_kwargs += 1
#         print(f'The total number of positional args are {total_args}')
#         print(f'The total number of keyword args are {total_kwargs}')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #spam = outer(spam)
# def spam(*args, **kwargs):
#     pass
#
# spam(1, 2, 3, 4, 5, a=10, b=20, c=30, d=100, z=10000, m='hai')

'6. write a program to print the name of the main function'

# def outer(func):
#     def wrapper(*args,**kwargs):
#         print(f"the name of the function is {func.__name__}")
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
#
# @outer
# def add(a,b):
#     c = a+b
#     return c
# print(add(1,2))

'7. write a decorator function to know how many functions are decorated'
# count=0
# def outer(func):
#     def wrapper(*args,**kwargs):
#         global count
#         count+=1
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
#
# @outer
# def add(a,b):
#     c = a+b
#     return c
# print(add(1,2))
#
# @outer
# def spam():
#     print('in spam')
# spam()
#
# print(f'total decorated functions are {count}')


'8. write a decorator to calculate the execution time'

# import time
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         starting_time=time.time()
#         time.sleep(2)
#         result=func(*args,**kwargs)
#         ending_time=time.time()
#         total_time=ending_time-starting_time
#         print(f'the total time taken by {func.__name__} function is {total_time}')
#         return result
#     return wrapper
#
# @outer
# def add(a,b):
#     c=a+b
#     return c
# print(add(1,2))


'9. Write a decorator to execute the main function for 3 times'

# def outer(func):
#     def wrapper(*args,**kwargs):
#         for _ in range(1,4):
#             func(*args,**kwargs)
#     return wrapper
#
# @outer
# def add(a,b):
#     c = a+b
#     print(c)
# add(1,2)
#
# @outer
# def spam():
#     print('i spam')
# spam()

'parameterized Decorator'

'''10. if you want to execute one main function 5 times and another main function 3 times then we are using 
       parameterized decorator'''

# def execute_n_time(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return outer
#
# @execute_n_time(3)
# def spam():
#     print('i have')
# spam()
#
# @execute_n_time(5)
# def display():
#     print('in display')
# display()

'11.wap to which takes current time and add 10 minutes'

# import datetime
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         current_time=datetime.datetime.now()
#         new_time=current_time+datetime.timedelta(minutes=10)
#         print(f'current_time={current_time}')
#         print(f'new_time={new_time}')
#         func(*args,**kwargs)
#     return wrapper
# @outer
# def add_time(time):
#     print(time)
# add_time(10.22)