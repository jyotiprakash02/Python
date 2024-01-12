'''1. Write a program to find the length of iterable.'''

'using len() inbuilt fun'

# print(len('hello universe'))

'without using inbuilt func'

# def length(iterable):
#     count = 0
#     for ele in iterable:
#         count += 1
#     return count
#
# print(length('python is a programming language'))

'Alternative method'

# def func():
#     return 'a', 'b', 10, True, 2.3, False, 'python'
#
# print(func())   #('a', 'b', 10, True, 2.3, False, 'python')

'''2. write a program to reverse a string without any inbuilt methods'''

'Using slicing'
# a = 'python'
# print(a[::-1])

'Using reversed'

# a = 'python'
# print(reversed(a))            #<reversed object at 0x0000029B61446670>
# rev_ele = list(reversed(a))
# print(rev_ele)                #['n', 'o', 'h', 't', 'y', 'p']
# print(''.join(rev_ele))       #nohtyp

'Alternate method'

# a = 'python'
# for ele in range(len(a)-1, -1, -1):
#     print(a[ele], end='')             #nohtyp

'Alternate method'

# a = 'python'
# b = []
# for ele in range(len(a)-1, -1, -1):
#     b.append(a[ele])
# print(b)
# print(''.join(b))

# def reverse(string):
#     b = ''
#     for ele in string:
#         b = ele +b
#     print(b)
# reverse('spiderman')

# def reverse(list_):
#     b = []
#     for ele in list_:
#         b = [ele] + b
#     print(b)
# reverse(['apple', 'google', 'Ajio', 'Myntra', 'amazon', 'flipkart'])

'''3. wap to replace one string with another str_='hello world', replace world with universe.'''

# replace()method
# str_ = 'hello world'
# print(str_.replace('world', 'universe'))        #hello universe
# str_ = 'hello world'
# import re
# print(re.sub('world', 'universe', str_))

'''4. wap to replace all the vowels in the string with * '''

# str_ = 'python is a programming language'
# result_str = ''
# for ele in str_:
#     if ele in 'aeiouAEIOU':
#         result_str += '*'
#     else:
#         result_str += ele
# print(result_str)
''' 5. How to convert a string to a list and vice-versa '''
# a = 'hello world'
# b = list(a)
# print(b)                #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# print(a.split())        #['hello', 'world']

'''5. convert the string, 'Hello Welcome to Python' to a comma separated string '''

# str_ = 'Hello Welcome to Python'    #'Hello,Welcome,to,Python'
# print(str_.replace(' ', ','))       #Hello,Welcome,to,Python

'Alternate method'

# a=''
# for ele in str_:
#     if ele==' ':
#         a+=','
#     else:
#         a+=ele
# print(a)

'Alternate method'

# str_ = 'Hello Welcome to Python'
# res = str_.split()
# print(','.join(res))               # Hello,Welcome,to,Python

''' 6. wap to print the ASCII values of all the characters in the string. '''

# str_ = 'hello world'
# for ele in str_:
#     print(f'The ASCII value of {ele} is {ord(ele)}')

''' 7. wap to convert the uppercase alphabets to lowercase and vice-versa '''

'swapcase()'

# str_ = 'HeLlO WeLcOmE To BEnGALuRu'
# print(str_.swapcase())      #hElLo wElCoMe tO beNgalUrU

'Alternate Solution'

# str_ = 'HeLlO WeLcOmE To BEnGALuRu'
# res = ''
# for ele in str_:
#     if ele.isupper():
#         res += ele.lower()
#     elif ele.islower():
#         res += ele.upper()
#     else:
#         res += ele
# print(res)      #hElLo wElCoMe tO beNgalUrU

'Alternate method'

# str_ = 'HeLlO WeLcOmE To BEnGALuRu'
# res = ''
# for ele in str_:
#     if ord('a') <= ord(ele) <= ord('z'):
#         res += chr(ord(ele) - 32)
#     elif ord('A') <= ord(ele) <= ord('Z'):
#         res += chr(ord(ele) + 32)
#     else:
#         res += ele
# print(res)

'''8. wap to search for a particular character in a given string
      and return the corresponding index '''

# def str_index(str_, element):
#     for index, item in enumerate(str_):
#         if element == item:
#             print(f'The index of {item} is {index}')
#
# str_index('welcome to python', 'e')

'Alternate'

# def str_index(str_, n):
#     for ele in str_:
#         if str_.find(n) > -1:
#             return str_.find(n)
#
# print(str_index('python', 'p'))

'Alternate'

# def string(str_, ele):
#     try:
#         print(str_.index(ele))
#     except ValueError:
#         print('element not found')
#
# string('python', 'l')

''' 9. wap to get the below output
       str_ = 'python is a programming language and programs are fun'
       o/p --> {p:[python, programming, programs], i:[is], a:[a, and, are],
       l:[language], f:[fun]} '''

# str_ = 'python is a programming language and programs are fun'
# dict_ = {}
# split_str = str_.split()
# print(split_str)
# ['python', 'is', 'a', 'programming', 'language', 'and', 'programs', 'are', 'fun']

# for ele in split_str:
#     if ele[0] not in dict_:
#         dict_[ele[0]] = [ele]
#     else:
#         dict_[ele[0]] += [ele]
#
# print(dict_)

'Alternate Solution Using default dict'

# str_ = 'python is a programming language and programs are fun'

# from collections import defaultdict
# def_dict = defaultdict(list)
# split_str = str_.split()
# for ele in split_str:
#     def_dict[ele[0]] += [ele]
#
# print(def_dict)

'''10.'''

# a = 'she sells seashells on the seashore'
# d = {}  #{s:8, h:4, e:7, ' ':5,....}
# for ele in a:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
# print(d)

'Alternative solution'

# from collections import defaultdict
# def_dict = defaultdict(int)
# for ele in a:
#     def_dict[ele] += 1
# print(def_dict)


'''11. wap to replace all the characters with * if the character
       occurs more than once in a string'''

# str_ = 'hello welcome to Bengaluru'
# h*****w**c*m**t**B*nga**r*

# res = ''
# for ele in str_:
#     if str_.count(ele) > 1:
#         res += '*'
#     else:
#         res += ele
# print(res)

'Alternate solution using comprehension'

# str_ = 'hello welcome to Bengaluru'
# result = ''.join(['*' if str_.count(ele)>1 else ele for ele in str_])
# print(result)

'''12. wap to get the below output'''

# s = 'hi how are you'        # ih woh era uoy
# s = 'hi how are you'          # ih woh era uoy

# words = s.split()
# print(words)        #['hi', 'how', 'are', 'you']
# res_str = ''
# for ele in words:
#     res_str += ele[::-1] + ' '
#
# print(res_str)

'alternate method'

# s = 'hi how are you'        # ih woh era uoy
# words = s.split()
# a =[]
# for ele in words:
#     a.append(ele[::-1])
# print(' '.join(a))


'''13. wap to get the below output'''

# s1 = 'hi how are you'         # ouy era woh ih
# s1 = 'hi how are you'       # ouy era woh ih

# res = ''
# for ele in s1:
#     res = ele + res
# print(res)

'''14. Find the longest word in the sentence'''

# s = 'python is a programming language'
# s_split = s.split()
# # print(s_split)  #['python', 'is', 'a', 'programming', 'language']
#
# longest_word = s_split[0]
# for ele in s_split:
#     if len(ele) > len(longest_word):
#         longest_word = ele
#
# print(longest_word)

'Alternate method'

# s = 'python is a programming language'
# longest = max(s.split(), key=len)
# print(longest)

'''15. Program to find the shortest element'''

# s = 'python is a programming language'
# shortest = min(s.split(), key=len)
# print(shortest)

'Alternate method.'

# s = 'python is a programming language'
# s_split = s.split()
# print(s_split)  #['python', 'is', 'a', 'programming', 'language']
# shortest_word = s_split[0]
# for ele in s_split:
#     if len(ele) < len(shortest_word):
#         shortest_word = ele
# print(shortest_word)

'''16. Sum of all the numbers in the below string'''
# import re

# s = 'Sony12India567Pvt2ltd'
# total = 0
# res = re.findall(r'\d', s)
# print(res)  #['1', '2', '5', '6', '7', '2']
# for num in res:
#     total += int(num)
# print(total)

# s = 'Sony12India567Pvt2ltd'
# total = 0
# for ele in s:
#     if '0' <= ele <= '9':
#         total += int(ele)
# print(total)


'''17. wap to print sum of all numbers in below string'''

# s = 'Sony12India567Pvt25ltd'     # 12 + 567 + 25

# total = 0
# res = re.findall(r'[\d]+', s)
# print(res)      #['12', '567', '25']
# for num in res:
#     total += int(num)
# print(total)


'''18. wap to print the number of occurrence of characters in 
       a string without using inbuilt methods'''

# s = 'hello world'
# d = {}
# for ele in s:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
# print(d)

'alternative method'

# d = {}
# for ele in s:
#     d[ele]=s.count(ele)
# print(d)

'Using defaultdict'

# from collections import defaultdict
# s = 'hello world'
# def_dict = defaultdict(int)
# for ele in s:
#     def_dict[ele] += 1
# print(def_dict)


''' 19. wap to print only the repeated characters and the count
    of the repeated characters'''

# s = 'hello world'
# from collections import defaultdict
#
# def_dict = defaultdict(int)
# for ele in s:
#     def_dict[ele] += 1
# # print(def_dict)
#
# for key, value in def_dict.items():
#     if value > 1:
#         print(key, value)

'Alternative method'

# s = 'hello world'
# d = {}
# for ele in s:
#     if s.count(ele)>1:
#         d[ele]=s.count(ele)
# print(d)


'''20. wap to get alternate characters of a str in list format '''

# s = 'hello universe'
# res = s[::2]
# print(list(res))              #['h', 'l', 'o', 'u', 'i', 'e', 's']

'Using Comprehension'

# s = 'hello universe'
# l = [ele for ele in s[::2]]
# print(l)                      #['h', 'l', 'o', 'u', 'i', 'e', 's']

'''21. wap to print alternate characters in a string'''

# str_ = 'Hello Welcome to Python'
# Slicing
# print(str_[::2])        #HloWloet yhn

'Alternate method'

# for ele in range(0, len(str_), 2):
#     print(str_[ele], end='')        #HloWloet yhn

'''22. Find the longest non-repeated substring in the below string'''

# s = 'python is a programming language and programming is very easy'
# words = s.split()
# ele = words[0]
# for word in words:
#     if words.count(word)==1 and len(word)>len(ele):
#             ele = word
# print(ele, len(ele))

'''23. wap to rotate characters in a string from r to o'''

# s = 'hello world'
# print(s[-3:] + s[:-3])

'''24. wap to count the number of white spaces in a given string'''

# s = 'hello world welcome to python'
# import re
# print(len(re.findall(r'\s', s)))

'''25. wap to print only non repeated characters in a string'''

# s = 'hello world'
# p = ''
# for ele in s:
#     if s.count(ele) == 1:
#         p += ele
# print(p)

'''26. wap to print all the consonants in a given string'''

# s = 'hello world'
# f = ''
# for ele in s:
#     if ele not in 'AEIOUaeiou':
#         f+=ele
# print(f)

'''27. wap to count no of capital letters in the string'''

# str_ = 'PyThoN 123 IS @ PrOgRAmmING 567 LAnGuagE !'

# from re import findall
# d = findall(r'[A-Z]',str_)
# print(len(d))

'alternative method'

# f ={}
# for ele in str_:
#     if ele.isupper():
#         f[ele]=str_.count(ele)
# print(f)

'alternative method'

# total = 0
# for ele in str_:
#     if ele.isupper():
#         total+=1
# print(total)

'''28. wap to find the first repeating character in a string'''

# s = 'hai hello universe how are you'
# for ele in s:
#     if s.count(ele)>1:
#         print(ele)
#         break

'''29. wap to find the index of nth occurrence of a substring in a string'''

import re
# s = 'she sells seashells on the seashore'
# def n_occurance(iterable, pat, n):
#     count = 0
#     res = re.finditer(pat, iterable)
#     for ele in res:
#         count += 1
#         if count == n:
#             print(ele)
#
# n_occurrence(s, 'e', 7)

'''30. wap to count the number of occurrences of special characters in the given string'''

# s = '123hello @ world ! % ha! Un!verse4567 *()'
# from re import findall
# _s = findall(r'[^\s\w]',s)
# print(_s)
# d ={}
# for ele in _s:
#     if ele in d:
#         d[ele]+=1
#     else:
#         d[ele]=1
# print(d)
#
#  #total ele
# total =0
# for ele in _s:
#     total+=1
# print(total)

'''31. Filter only those characters except digits'''

# s = '123@hello4567 world 789 universe !!'
# from re import findall
# d = findall(r'[^\d]',s)
# print(d)

'Alternative solution'

#  _s =''
# for ele in s:
#     if not ele.isdigit():
#         _s+=ele
# print(_s)

'''31. Find all max length words from the below sentence '''

# sentence = 'hello world hi apple hai yahoo'
# res = sentence.split()
# # print(res)      #['hello', 'world', 'hi', 'apple', 'hai', 'yahoo']
#
# max_len = max(res,key=len)
# print(max_len)
# for ele in res:
#     if len(ele) == len(max_len):
#         print(ele)

'''32. Find the range from the following string'''

# s = '0-0,4-8,20-20,43-45'
# [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
# res = s.split(',')
# print(res)               #['0-0', '4-8', '20-20', '43-45']
#
# range_list = []
# for ele in res:
#     start, end = ele.split('-')
#     for num in range(int(start), int(end)+1):
#         range_list.append(num)
#
# print(range_list)

'''33. Replace whitespaces with newline character in the below string'''

# sentence = 'Hello world welcome to python'
# print(sentence.replace(' ','\n'))
#
# import re
# res = re.sub(' ','\n',sentence)
# print(res)


'''34. Replace all the vowels with "*" '''

# sentence = 'Hello world welcome to python'
# s=''
# for ele in sentence:
#     if ele in 'AEIOUaeiou':
#         s+='*'
#     else:
#         s+=ele
# print(s)

'''35. wap to get the below output
input --> 'python@#$%pool'
output --> ['PYTHON', 'POOL']
'''
# input ='python@#$%pool'
# from re import findall
# f = findall(r'[\w]+',input)
# print(f)
# r =[]
# for ele in f:
#     r.append(ele.upper())
# print(r)

'Alternative solution'

# u= 'python@#$%pool'
# from re import findall
# res =findall(r'[a-z]+',u)
# d =[]
# for ele in res:
#     d.append(ele.upper())
# print(d)

'''36. wap to print all the words which starts with letter 'h' in the given string '''

# s='hello world hi universe how are you happy birthday'
# r=s.split()
# for ele in r:
#     if ele[0].startswith('h'):
#         print(ele)

''''37. wap to find the sum of all even numbers in the given string'''

# s= "hello 123 world 567 welcome to 9724 python"
# from re import findall
# e = findall(r'[\d]',s)
# print(e)
# total = 0
# for ele in e:
#     if int(ele)%2==0:
#         total+=int(ele)
# print(total)

'''38. wap to add each num in word1 to number in word2 '''

# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# # ## output --> 1+5, 2+6, 3 +7, 4+8, 5+9
# from re import findall
# w1 = findall(r'[\d]',word1)
# w2 = findall(r'[\d]',word2)
# for i,j in zip(w1,w2):
#     print(f'{i}+{j}')

'''39. wap to filter out even and odd numbers in the given str'''

# s = 'hello 123 world 567 welcome to 9724'
# # from re import findallpython685645'
# d = findall(r'[\d]',s)
# print(d)
#
# _even=[]
# _odd = []
# for ele in d:
#     if int(ele)%2 ==0:
#         _even.append(ele)
#     else:
#         _odd.append(ele)
# print(_odd)
# print(_even)