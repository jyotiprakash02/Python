'''1. wap to read a random line in a file'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(num):
#     with open(path) as file:
#         for line_no, line in enumerate(file, start=1):
#             if num == line_no:
#                 print(f'{line_no} = {line}')
#
# random_line(9)

'Alternate solution'

# from itertools import islice
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(num):
#     with open(path) as file:
#         ## res = islice(file, line_num, line_num+1)
#         res = islice(file, num, num+1)
#         print(res)  #<itertools.islice object at 0x000001E254E56090>
#         for ele in res:
#             print(ele)
#
# random_line(3)


'''2. wap to read a random lines in a file'''

# from itertools import islice

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(start_val, end_val):
#     with open(path) as file:
#         ## res = islice(file, start, end)
#         res = islice(file, start_val-1, end_val)
#         print(res)  #<itertools.islice object at 0x000001E254E56090>
#         for ele in res:
#             print(ele)
#
# random_line(3, 8)


'''3.wap to print last N lines of a file'''

# from itertools import islice
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def last_n_lines(num):
#     with open(path) as file:
#         line_count = 0
#         for line in file:
#             line_count += 1
#         print(line_count)
#
#         file.seek(0)
#
#         res = islice(file, line_count-num, line_count)
#         # print(res)
#         print(list(res))
#
# last_n_lines(4)

'Alternate method'

# from collections import deque
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def last_n_lines(num):
#     with open(path) as file:
#         res = deque(file, num)
#         print(res)
#
# last_n_lines(3)

'''4. Count the number of occurrences of 'CRITICAL', "INFO", "ERROR" lines in a log file'''

# lines = '''CRITICAL:Hello world
# INFO: This is an info
# ERROR: this is an error
# CRITICAL: This is critical
# CRITICAL: hello
# INFO: hello info
# ERROR: This is error
# CRITICAl: This is critical
# CRITICAL: Critical issue
# INFO: hello
# ERROR: hello
# '''
# d = {}
# for line in lines.split('\n'):
#     split = line.split(':')
#     for ele in split:
#         if ele not in d:
#             d[ele] = 1
#         else:
#             d[ele] += 1
#
# print(d)

'''5. wap to count the number of lines  in a file without loading the file to the memory'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# with open(path) as file:
#     line_count = 0
#     for line in file:
#         line_count += 1
#     print(line_count)


'''6. Printing line and line numbers'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, '-', line)


'''7. wap to count number of white spaces in a file'''

# import re
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# count = 0
# with open(path) as file:
#     for line in file:
#         match = re.findall(r'\s', line)
#         if match:
#             count += len(match)
#
# print(count)

''' 8. wap to count the number of occurrences of each word in file'''

from collections import defaultdict

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         if line.strip():
#             res = line.split()
#             for ele in res:
#                 d[ele] += 1
#
#             print(d)

'''9. wap to count the number of vowels'''

path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             vowel_count = 0
#             for ele in line:
#                 if ele in 'aeiouAEIOU':
#                     vowel_count += 1
#             print(f'{line.strip()} has {vowel_count} vowels')

'''10. wap that counts the occurrences of a particular word in file'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# def _count(word):
#     with open(path) as f1:
#         count = 0
#         for line in f1:
#             words = line.split()
#             for i in words:
#                 if i == word:
#                     count += 1
#         print(count)
#
# _count('hello')

''' 11. wap to count the number of commented lines in the file'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\wednesday_apr_19.py'
# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             if line.startswith('#'):
#                 count += 1
#     print(count)

'''12. Replace all the occurrences of Java with Python in a file'''

# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# with open(path) as file:
#     for line in file:
#         res = re.sub(r'java', 'python', line)
#         print(res)

