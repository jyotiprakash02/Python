'''1. Triangle patterns '''

'''
*
* *
* * *
* * * *
'''
# for ele in range(1, 5):
#     print(ele * '* ')

'''2.'''

'''
* * * *
* * *
* *
*
'''
# for i in range(4, 0, -1):
#     print(i * '* ')

# -----------------------------------------------------

'''3. Right justified triangle'''

'''
      *
    * *
  * * *
* * * *
'''

# for i in range(1, 5):
#     print(f'{"* " * i:>8}')


'''4.'''

'''
* * * *
  * * *
    * *
      *
'''
# for i in range(4, 0, -1):
#     print(f'{"* " * i:>8}')

'''5.'''

'''
   *
  * *
 * * *
* * * *
'''
# for i in range(1, 5):
#     print(f'{"* " * i:^8}')

'''6.'''

'''
* * * *
 * * *
  * *
   *
'''

# for i in range(4, 0, -1):
#     print(f'{"* " * i:^8}')

'''7.'''

'''

*
*
* *
*
* * *
*
* * * *
*
'''

# for ele in range(1, 5):
#     print(ele * '* ')
#     print('*')

'''8.'''

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# pat = ""
# for i in range(1, 6):
#     pat += str(i) + ' '      #pat = pat + str(i)
#     print(pat)

'''9.'''

'''
        1
      1 2
    1 2 3
  1 2 3 4 
1 2 3 4 5
'''

# pat = ''
# for i in range(1, 6):
#     pat += str(i) + ' '
#     print(f'{pat :>10}')

'''10.'''

'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''

# pat = ''
# for i in range(1, 6):
#     pat += str(i) +' '
#     print(f'{pat :^10}')

'''11.'''

'''
a 
a b 
a b c
a b c d
'''

# pat = ""
# for ele in range(ord('a'), ord('e')):  #for ele in range(97, 101)
#     pat += chr(ele) +' '
#     print(pat)

'''12. wap to get the below output using while loop'''

'''
1
1 2
1 2 3
1 2 3 4
'''
# pat = ''
# count = 1
# while count <=4:
#     pat += str(count) + ' '
#     print(pat)
#     count += 1
