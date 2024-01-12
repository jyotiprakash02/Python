'''1. write a func which takes a list of strings and numbers.
      If the item is a string, print it as it is, if it is int or
      float, reverse it'''

# res_list = []
# def func(list_):
#     for ele in list_:
#         if isinstance(ele, str):
#             res_list.append(ele)
#         else:
#             # res = str(ele)
#             res_list.append(str(ele)[::-1])
#
# func(['python', 24, 8.6, 'hello', 78, 9.8, 'welcome'])
# print(res_list)

'''2.'''

# l = ['apple', 'ajio']
# # d = {apple:elppa, ajio:ajio}
# d = {}
# for ele in l:
#     if len(ele)%2 == 0:
#         d[ele] = ele
#     else:
#         d[ele] = ele[::-1]
# print(d)

'''3. Write a lambda func to add two numbers'''

# res = lambda a, b : a + b
# print(res(6, 7))

'''4. A function takes variable number of positional arguments
      as input. How to check if the arguments that are passed are more than 5 '''

# def func(*args):
#     if len(args) > 5:
#         print('The arguments are greater than 5')
#     else:
#         print('The arguments are lesser than 5')
#
# func('a', 'b', 10, 2, 3, 4, 'python', 'hai')
# func(1, 2)

'''5. write a func to print the below output

func('TRACXN', 0)   ---->Should print RCN
func('TRACXN', 1)   ---->Should print TAX
'''
# def func(string, num):
#     if num == 0:
#         print(string[1::2])
#     elif num == 1:
#         print(string[::2])
#     else:
#         print('Invalid Input')
#
# func('TRACXN', 0)       #RCN
# func('TRACXN', 1)       #TAX
# func('TRACXN', 8)

'''6. write a func that accepts two strings and returns True 
      if the two strings are anagrams of each other '''

# def anagram(str1, str2):
#     if str1 == str2:
#         return False
#     a = sorted(str1)
#     b = sorted(str2)
#     if a == b:
#         return True
#     else:
#         return False
#
# print(anagram('silent', 'listen'))
# print(anagram('racecar', 'racecar'))

'''7. write a func that returns the last digit of an integer For Eg. 
      if user input is 3716, output should be 6. '''

# def is_last_digit(num):
#     if num %10 !=0:
#         temp = num % 10
#         print(temp)
#
# is_last_digit(4568709)

'''8. Make a func named tail that takes the sequence like (list, str, tuple) and a number, 
      and returns the last n elements from the given sequence as a list '''

# def tail(iterable, n):
#     if not isinstance(n, int):
#         return 'Only integers'
#     if n < 0:
#         return []
#     return list(iterable[-n:])
#
# print(tail('programming', -4))

'''9. write a func that accepts a number and returns True if its a perfect square, else False'''

# from math import sqrt
# def is_perfect_square(num):
#     return num == sqrt(num)**2
#
# print(is_perfect_square(8))     #False
# print(is_perfect_square(9))     #True

'''10. write a func which returns the sum of lengths of all the iterables'''

# def total_length(*iterables):
#     total = 0
#     for iterable in iterables:
#         total += len(iterable)
#     return total
#
# print(total_length('hai', [1, 2, 3, 4], (2, 3, 4), {1:1, 2:2}))

