'''1. wap to swap two numbers without using 3rd variable'''''
import time

# num1 = 100
# num2 = 200
# num2, num1 = num1, num2
# print(num1)
# print(num2)

'''2.wap to check if the string is palindrome or not'''

# def palindrome(str_):
#     if str_ == str_[::-1]:
#         return f'{str_} is a palindrome'
#     else:
#         return f'{str_} is not a palindrome'
# print(palindrome('racecar'))

'Alternative solution'

# def palindrome(str_):
#     rev_str = ''
#     for ele in str_:
#         rev_str = ele + rev_str
#
#     if str_ == rev_str:
#         return f'{str_} is a palindrome'
#     else:
#         return f'{str_} is not a palindrome'
#
# print(palindrome('malayalam'))
# print(palindrome('python'))

'''3. write a func to print all the prime number from 0 to the given range'''

# def is_prime(num):
#     for i in range(2, num):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# is_prime(10)

# def is_prime(num):
#     return not any(num % ele == 0 for ele in range(2, num))
#
# print(is_prime(9))
# print(is_prime(7))
# print(is_prime(17))

'''4. wap to check if the year is leap year or not'''
# def Loop_year(year):
#     if year%4==0:
#          print('loop year')
#     else:
#         print('it is not a loop year')
# Loop_year(2021)

'Alternative solution'

import calendar
# print(calendar.isleap(2020))
# print(calendar.isleap(2023))

'''5.write a func to check if the numb is prime or not'''
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print(f'{n} is not prime')
#             break
#     else:
#         print(f'{n} is a prime number')
# prime(6)

'''6. Swap two variables without using 3rd variable'''
# a = 10
# b = 20
# b, a = a, b
# print(a)
# print(b)

'''7. write a fibonacci series'''
# def fibo(num):
#     n1 = 0
#     n2 = 1
#
#     for i in range(0,num):
#         yield n1
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#
#
# res = fibo(10)
# for j in res:
#     print(j)

'''8. wap to print "Bengaluru" for 10 times without using loops '''

# print('bengaluru\n'*10)

'''9. match the pattern of the string and count will be 2'''

# s = 'cdcdc'
# pattern = 'cdc'
# count = 0
# for ele in range(len(s)):
#     if s[ele:ele+3] == pattern:
#         count += 1
#
# print(count)

'''10. wap to print random number in each execution'''

# import random
# def random_number(N):
#     minimum = pow(10,N-1)
#     maximum =  pow(10,N)-1
#     return random.randint(minimum, maximum)
# print(random_number(5))















































