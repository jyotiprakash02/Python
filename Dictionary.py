'''1. wap to reverse the values in a dict if the value is of type string
      output = {'a': 'olleh', 'b': 9.8, 'c': 'dlrow', 'd': 100} '''

# d = {'a': 'hello', 'b': 9.8, 'c': 'world', 'd': 100}

# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)


'''Using Comprehension'''

# d2 = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d2)

'''2. wap to replace the value present in nested dictionary'''

# d = {'a':100, 'b':{'m':'man', 'n':'nose', 'c':'cat'}}
# #Replace nose with net
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = 'net'
# print(d)    #{'a': 100, 'b': {'m': 'man', 'n': 'net', 'c': 'cat'}}

'''3. wap to find the most common words in given list'''
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
# 'eyes', "don't", 'look', 'around', 'the', 'eyes'
# ]
# d = {}
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
# print(d)

# res = sorted(d.items(), key=lambda some_tuple: some_tuple[-1])
# print(res[-1])

# from collections import Counter
# c = Counter(words)
# print(c)    # Counter({'eyes': 7, 'the': 5, 'look': 3, 'into': 2, 'my': 2, 'around': 2, 'not': 1, "don't": 1})
# print(c.most_common())  # [('eyes', 7), ('the', 5), ('look', 3), ('into', 2), ('my', 2), ('around', 2), ('not', 1), ("don't", 1)]
# print(c.most_common()[0])

'''4. wap to map a product to a company and build a dict with
      company and list of products pair'''

# all_products = ['iPhone', 'mac', 'gmail', 'maps', 'iWatch',
#                 'windows', 'google_drive', 'one drive']
#
# apple_products = ['iPhone', 'mac', 'iWatch']
# google_products = ['gmail', 'maps', 'google_drive']
# msft_products = ['windows', 'one drive']
#
# from collections import defaultdict
# def_dict = defaultdict(list)
#
# for ele in all_products:
#     if ele in apple_products:
#         def_dict['apple_products'] += [ele]
#     elif ele in google_products:
#         def_dict['google_products'] += [ele]
#     elif ele in msft_products:
#         def_dict['msft_products'] += [ele]
#
# print(def_dict)

'''5. make a dictionary of company name as key and products are the values'''

# company_name = ['apple', 'google', 'microsoft']
# all_products = ['iPhone', 'mac', 'gmail', 'maps', 'lumia', 'iWatch',
#                 'windows', 'google_drive', 'one drive']
#
# apple_products = ['iPhone', 'mac', 'iWatch']
# google_products = ['gmail', 'maps', 'google_drive']
# microsoft_products = ['windows', 'one drive', 'lumia']
#
# from collections import defaultdict
# def_dict = defaultdict(list)
# for ele1 in company_name:
#     for ele2 in all_products:
#         if ele1 == 'apple' and ele2 in apple_products:
#             def_dict[ele1] += [ele2]
#         elif ele1 == 'google' and ele2 in google_products:
#             def_dict[ele1] += [ele2]
#         elif ele1 == 'microsoft' and ele2 in microsoft_products:
#             def_dict[ele1] += [ele2]
#
# print(def_dict)

'''6. make a dictionary of ele of 'a' as key and ele of 'b' as value '''

# a = ['a', 'b', 'c']
# b = [10, 20, 30]
# d = {}
# for ele1, ele2 in zip(a, b):
#     d[ele1] = ele2
# print(d)

'''or'''

# a = ['a', 'b', 'c']
# b = [10, 20, 30]
# d = {}
# for ele1 in a:
#     for ele2 in b:
#         d[ele1] = ele2
# print(d)

'''7. wap to get the below output 
      ['a', 'b', 'c', 'd', 'e'] '''

# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# s =[]
# for item in d.items():
#     key, value = item
#     s.append(key)
# print(s)

''' 8.I want the output 
      {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}'''

# s = ['a', 'b', 'c', 'd', 'e']
# d = {}
# for ele in s:
#     d[ele] = s.index(ele)
# print(d)

'''9. how to shorted a dictionary'''

# R = 'Raghab'
# d = {}
# for ele in R:
#     d[ele] = R.count(ele)
# print(d)
# print(d.keys())
# print(d.items())

# def some(some_tuple):
#     return some_tuple[-1]
#
#
# c = sorted(d.items(), key=some)
# '''or'''
# t = sorted(d.items(), key=lambda some_tuple: some_tuple[-1])
# print(c[-1])
# print(t[-1])

























