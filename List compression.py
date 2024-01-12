''' 1. write a list comprehension to get list of even numbers from 1-50 '''
print([ele for ele in range(1, 51) if ele % 2 == 0])

'2.write a program to print the number from -1 to -10 using list compression'
# print([ele for ele in range(-1,-11,-1)])

'3.write a program to print the number from 10 to 1 using list compression'
# print([ele for ele in range(10,0,-1)])

'4. write a list compression print the word whose first letter starts with vowel'

# names=['alum','smith','john','oms','elipsha']
# print([name for name in names if name[0] in 'AEIOUaeiou'])

'5. write a list compression to separate the words which first letter starts with "p"'

# words =['python','pytest','pycharm','java','.net','c++']
# print([word for word in words if word[0].startswith('p')])

# Alternative method
# f = []
# f=([word for word in words if word[0]=='p'])
# print(f)

'6.I want to print those name whose whose length les tha 6 by list compression'

# names=['apple','google','yahoo','facebook']
# print([name for name in names if len(name)<6])

'7. I want the below output'
'input->[1,2,3,4,5]'
'output->[0,2,9,64,625]'

# nums=[1,2,3,4,5]
# print([value**index for index,value in enumerate(nums)])

'8.print the factorial of the number'
# from math import factorial
# number =[1,2,3,4]
# print([factorial(num)for num in number])

'9.I want to build a list of name and its length pair'

# names=['apple','google','yahoo','facebook']
# output=[('apple',5),('google',6)]

# print([(name,len(name))for name in names])

'10.even length of number name by list compression'

# names=['apple','google','yahoo','facebook']
# print([name for name in names if len(name)%2==0])

'11.I want to make a list, if the length of the element is even then live as it is, otherwise reverse it'

# names=['apple','google','yahoo','facebook']
# print([name if len(name)%2==0 else name[::-1] for name in names])

'12. I want to print below output'
# a=[1,2,3,4]
# b=[5,6,7,8]
# output=[6,8,10,12]

# a=[1,2,3,4]
# b=[5,6,7,8]
# print([ele1+ele2 for ele1,ele2 in zip(a,b)])

'13. I want to print below output'

# a=[[1,2,3],[4,5,6],[7,8,9]]
# print([_ele for ele in a for _ele in ele])

'14. I want to print below output'

# letter='ABCDEF'
# number=[0,1,2,3,4,5]
# output=['A0','B1','C2','D3','E4','F5']

# print([f'{ele1}{ele2}' for ele1,ele2 in zip(letter,number)])

'15.I want to make a list compression if the ele is list then reverse it otherwise live as it is'

# _list=['hello','hi',12.6,'world',14.2,True,'python']
# print([ele[::-1] if isinstance(ele,str) else ele for ele in _list])

'16.print the number from 1 to 10 using list compression'
# print([ele for ele in range(1,11)])








