'''1. wap to merge two different lists'''''
# list_1 = [10, '30', 20, 4.0]
# list_2 = ['hello', 'python', 'selenium']

'1.1 Using *'
# list_3 = [*list_1, *list_2]
# print(list_3)       #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

'1.2 Using +'
# print(list_1 + list_2)      #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

'1.3 Using extend method'
# list_1.extend(list_2)
# print(list_1)   #10, '30', 20, 4.0, 'hello', 'python', 'selenium']

# from itertools import chain
# merged_list = chain(list_1, list_2)
# print(merged_list)  #<itertools.chain object at 0x0000024C8C6CD430>
# print(list(merged_list))    #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

'1.4 To merge dictionaries'

# d1 = {'one':1, 'two':2, 'three':3}
# d2 = {1:'one', 2:'two', 3:'three'}
#
# # print({**d1, **d2}) #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}
# from itertools import chain
# merged_dict = chain(d1, d2)
# # print(merged_dict)
# print(list(merged_dict))

'2. What is the output of the following'

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print([l1, l2])
# print((l1, l2))
#
# print([l1, l2])     #[[1, 2, 3], [4, 5, 6]]
# print((l1, l2))     #([1, 2, 3], [4, 5, 6])


'3. wap to remove the duplicates from the list without using inbuilt methods'

# items = [1, 2, 1, 3, 5, 4, 3, 6, 7, 4]  ##[1, 2, 3, 5, 4, 6, 7]
# result = set(items)
# print(result)   #{1, 2, 3, 4, 5, 6, 7}
# print(list(result))

'3.1 Alternate method'

# items = [1, 2, 1, 3, 5, 4, 3, 6, 7, 4]  ##[1, 2, 3, 5, 4, 6, 7]
# unique_list = []
# for ele in items:
#     if ele not in unique_list:
#         unique_list.append(ele)
# print(unique_list)

'3.2 Using comprehension'

# res = [ele for ele in items if ele not ,in unique_list]
# print(res)

'4. How to get the elements that are in list b, but not in list a'

# list_a = [1, 2, 3]
# list_b = [1, 2, 3, 4]
# set_a = set(list_a)
# set_b = set(list_b)
# print(set_b.difference(set_a))

'4.1 Alternate solution'

# list_a = [1, 2, 3]
# list_b = [1, 2, 3, 4]
#
# for ele in list_b:
#     if ele not in list_a:
#         print(ele)

'5. wap to reverse a iterable without using reversed func'

# l = [1, 2, 3, 4, 5]
# rev_l = []
# for ele in range(len(l)-1, -1, -1):
#     rev_l.append(ele)
# print(rev_l)

'5.1 Alternative'

# l = [1, 2, 3, 4, 5]
# d = []
# for ele in l:
#     d=[ele]+d
# print(d)


'6. wap to get the square of list of numbers'

# l = [1, 3, 34, 32, 7, 65, 43, 10]
# def square(iterable):
#     square_list = []
#     for num in iterable:
#         square_list.append(num ** 2)
#     return square_list
#
# print(square(l))

'6.1 Using Lambda'

# l = [1, 3, 34, 32, 7, 65, 43, 10]
# res = lambda num : num ** 2
# sq_list = [res(ele) for ele in l]
# print(sq_list)

''' 7. write a program to iterate through list and build a new list, 
       only if the items in the list has even number of characters.   '''

# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# even_list = []
# for ele in list_:
#     if len(ele)%2 == 0:
#         even_list.append(ele)
#
# print(even_list)


'''8. write a program to iterate through list and build a 
      dict of even length ele as key and its len as value'''

# list_ = ['mysore', True, 'bengaluru', 10, 'bijapura', 'hubli', 'dharwad', 'badami']
# dict_ = {}
# for ele in list_:
#     if isinstance(ele, str):
#         if len(ele)%2 == 0:
#             dict_[ele] = len(ele)
#
# print(dict_)


'9. wap which squares the numbers in a list using map object '

# l = [1, 2, 3, 4, 5]
# ## map = map(func, iterable)
# res = map(lambda num : num ** 2, l) #[1, 4, 9, 16, 25]
# print(res)  #<map object at 0x0000025A57CCD5B0>
# print(list(res))

'9.1 Using normal func'

# l = [1, 2, 3, 4, 5]
# def square(num):
#     return num ** 2
#
# res = map(square, l)
# print(res)
# print(list(res))


# ele = 'bengaluru'
# res = lambda element : len(element) % 2 == 0
# print(res(ele))

# ele = 'bengaluru'
# res = lambda element : 'even length' if len(element) % 2 == 0 else 'odd length'
# print(res(ele))

# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# res = map(lambda element : len(element) % 2 == 0, list_)
# print(res)
# print(list(res))    #[True, False, True, False, False, True]


# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# res = filter(lambda element : len(element) % 2 == 0, list_)
# print(res)
# print(list(res))

'''49. wap to print the sum of entire list and sum of internal list'''
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [6, 15, 24]
# 45
# sum_list = []
# for ele in l:
#     sum_list.append(sum(ele))
# print(sum_list)     # [6, 15, 24]
# print(sum(sum_list)) # 45
#
#
# l1 = []
# total = 0
# for ele in l:
#     for item in ele:
#         total += item
#
# print(total) #45

'''50. wap to reverse the list as below'''
# words = ['hi', 'hello', 'python']
#op --> ['nohtyp', 'olleh', 'ih']
# rev_list = []
# for ele in words[::-1]:
#     rev_list.append(ele[::-1])
# print(rev_list[::-1])

'''61. write a program to find the duplicate elements in the list
without using inbuilt functions'''

# list_ = ['apple', 'google', 'apple', 'gmail', 'google', 'kia']
# for item in s1:
#     count = 0
#     for ele in list_:
#         if item == ele:
#             count += 1
#     if count > 1:
#         print(item)

# ''Alternet solution''
#
# list = []
# for ele in list_:
#     if list_.count(ele)>1 and ele not in list:
#         list+=[ele]
# print(list)

'''62. wap to count the number of occurances of each item in the
list without using inbuilt functions
'''
# list1 = ['duster', 'seltos', 'kiger', 'ritz', 'kiger', 'duster']
# d = {}
# for ele in list1:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
#
# print(d)
'''65. wap to find the largest number in the list without using
any inbuilt func'''

# l = [1, 4, 10, 32, 8, 4, 2]
# large = l[0]
# for i in l:
#     if i> large:
#         large = i
# print(large)

'''70. wap to get all the duplicate items and the number of times
 the item is repeated in the list'''
#
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook',
#           'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d = {}
# for ele in names:
#     if names.count(ele) > 1 and ele not in d:
#         d[ele] = names.count(ele)
#
# print(d)
'''35. Print the numbers in the below list'''
l = ['abcd', '123', 'xyz', '456']
# for ele in l:
#     if ele.isnumeric():
#         print(ele)

'''73. wap to print all numeric values in a list'''
l = ['apple', 1.2, 'google', '26', 100, 78]
# for ele in l:
#     if isinstance(ele,(int,float)):
#         print(ele)

'''77. wap to rotate the items of the list'''
names = ['apple', 'google', 'gmail', 'yahoo', 'microsoft']
# def _rotate(iterable, n):
#     for i in range(0, n):
#         res = iterable.pop()
#         iterable.insert(0, res)
#     print(iterable)
#
# _rotate(names, 2)
# _rotate(names, 3)

'''89. wap to get the below output'''
# a = [1, 2 ,3, 4, 5, 6, 7, 8, 9]
'''op ---> [1, 2], [3, 4], [5, 6], [7, 8], [9]'''
# for i in range(0, len(a), 2):
#     print(a[i:i+2])

'''90. wap to check if the elements in the second list
is series of continuation of the items in the first list'''
# l1 = [2, 4, 6, 8, 10]
# l2 = [12, 14, 16, 18, 20]
#
# diff = l1[1] - l1[0]
# l = [*l1, *l2]  #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# def continuation():
#     for ele in range(0, len(l)):
#         if l[ele + 1] == l[ele] + diff:
#             return True
#         else:
#             return False
#
# print(continuation())

'''95. wap to sort a list which has a mix of even and odd numbers
, the sorted list should contain odd numbers first and then even 
numbers in a sorted order'''

# num_list = [2, 17, 31, 32, 47, 97, 98, 60, 55, 46, 49]
# even_=[]
# odd_ = []
#
# for ele in num_list:
#     if ele%2==0:
#         even_.append(ele)
#     else:
#         odd_.append(ele)
# b=(sorted(even_))
# c=(sorted(odd_))
# print([*c,*b])
#
# even_.sort()
# odd_.sort()
# print(*odd_, *even_)

'''98. Grouping files with same extensions'''

# items = ['lotus-flower', 'lilly-flower', 'dog-animal',
#           'cat-animal', 'sunflower-flower']

'''99. Grouping files with same extensions'''
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt',
#          'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

'''102. Grouping even and odd numbers'''
 # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ## o/p ---> {1:[1, 3, 5, 7, 9], 0:[2, 4, 6, 8, 10]}
#
# from collections import defaultdict
# def_dict = defaultdict(list)
# for num in numbers:
#     if num % 2 == 0:
#         def_dict[0] += [num]
#     else:
#         def_dict[1] += [num]
#
# print(def_dict)

'''103. Find all the max numbers from the below list'''
# l = [1, 2, 2, 5, 6, 7, 8, 9, 4, 9, 9, 8, 9]
# max_ = max(l)
# print(max_)
# print(l.count(max_))

## Alternate
# l = [1, 2, 2, 5, 6, 7, 8, 9, 4, 9, 9, 8, 9]
# max_ = max(l)
# max_list = []
# for ele in l:
#     if ele == max_:
#         max_list.append(ele)
#
# print(max_list)     #[9, 9, 9, 9]
'''111. wap to find sum of max 3 numbers and min 3 numbers'''
# l = [9, 1, 4, 2, 3, 8, 6, 7, 5]
# l.sort()
# total1=0
# total2=0
# print(l)
# for ele in l[:3]:
#     total1+=ele
# for ele in l[-3:]:
#     total2+=ele
# print(total1)
# print(total2)


'''113. wap to print all the numbers which are ending with 5'''
# numbers = ['1', '12', '123', '12345', '125', '155', '555', '666']
# for ele in numbers:
#     if ele.endswith('5'):
#         print(ele)

'''114. wap to get the indexes of each item in the below list'''

# names = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'gmail',
#          'microsoft', 'yahoo', 'flipkart']
# for item in enumerate(names):
#     index,value=item
#     print(f'the item is {value} and its index is {index}')


'''120. wap to print all the numbers starting with 8'''
# numbers = ['8', '87', '67', '890', '45', '888', '108', '828']
# for ele in numbers:
#     if ele.startswith('8'):
#         print(ele)
'''121. wap to remove duplicates from the list without using
empty list or converting to set'''
# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4, 4, 3]
# c =l1[:]
# print(c)
# for ele in c:
#     if l1.count(ele)>1:
#         l1.remove(ele)
# print(l1)

'''122. Print all the missing numbers from 1-10 in the below list'''

# l = [1, 3, 6, 8, 10]
# _L =[]
# for ele in range(1,11):
#     if ele not in l:
#         _L.append(ele)
# print(_L)

'''123. wap to get the below output'''
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# l = []
# for item in l1:
#     for ele in l2:
#         l.append(str(item)+ele)
# print(','.join(l))    #1a,1b,1c,2a,2b,2c,3a,3b,3c

'''124. wap to get the below output
## o/p ---> [Y3, c2, a2, A4]'''
# words = 'AAAAaaccYYY'
# unique_words= set(words)
# print(unique_words)
#
# list_ = []
# for ele in unique_words:
#     temp = words.count(ele)
#     list_.append(ele+str(temp))
# print(list_)
'''126. In the list below, find all the number pairs which results in 10 either
when added or subtracted'''
# l = [3, 5, -4, 8, 11, 1, -1, 6, 14]
# for ele1 in l:
#     for ele2 in l:
#         if ele1+ele2==10:
#             print(f'the addision of {ele1}+{ele2}=10')
#         elif ele1-ele2==10:
#             print(f'the substraction of {ele1}-{ele2}=10')

'''132. reverse a list without using any inbuilt funcs and slicing'''

# a = [1, 2, 3, 4, 5]
# _a = []
# for ele in a:
#     _a = [ele]+_a
# print(_a)
#
# res=[a[ele] for ele in range(len(a)-1,-1,-1)]
# print(res)

'''138. What is the output of the following'''
# print([1, 2, 3, 4] * 2)     #[1, 2, 3, 4, 1, 2, 3, 4]

''''139.wap to get the element whose first letter and last letter is vowel'''

# names = ['apple', 'google', 'gmail', 'flipkart', 'yahoo']
# for ele in names:
#     if ele[0] in 'aeiouAEIOU' or ele[-1] in 'aeiouAEIOU':
#         print(ele)

'144. wap to get the below output'

# items = ['$123.45', '$434.23', '$567.89']
# from re import findall
# f = []
# for ele in items:
#     res=findall(r'[\d.\d]+',ele)
#     s = ''.join(res)
#     f.append(float(s))
# print(f)

'''145. function should accept a list and if any number is divisible by 3 then
modify that number to 33, else keep it as it is'''

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# d =[]
# for ele in l:
#     if ele %3==0:
#         d+=[33]
#     else:
#         d+=[ele]
# print(d)
#
# res =[33 if ele%3==0 else ele for ele in l]
# print(res)