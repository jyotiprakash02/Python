''' 1. difference between default dict and normal dict '''

'default dict'

# 1. When each key is encountered for the first time, it will not
#    be there  in the mapping
# 2. So an entry is automatically created with default value
# 3. When keys are encountered again, the look-up proceeds normally
#    like a normal dictionary
# 4. So, in default dict, creation of the key, initialisation will
#    happen simultaneously

'Normal dict :'

# 1. In case of normal dict, if the key does not exist,
#    'KEY ERROR' is raised.
# 2.   So, we first create the keys and initialise the values

'''2. Property decorator'''

'''3. Mutable and immutable datatypes'''

'''Mutable datatype '''

#  It is datatype where we can modify the value in the original memory location.
#  ex. list, set, dictionary

'''immutable datatype'''

#  immutable datatype are datatype where we cannot modify the original value if we modify the value we have to
#  take the copy of that and modify it and store in the different memory location.
#  ex.string, tuple

'''4. Explain get() method in dict.'''

# 1. In case of normal dictionary if the key is not present in the dictionary key error will come.
# 2. but in case of get method if the key is not present inside the dictionary it does not show key error instate of it
#    none will come.
# 3. It does not modify the original dictionary.

'''5.set-default'''

# set-default is similar to the get method but
# 1. It modified the original dictionary.
# 2. It does not show key error if key is not present in the dictionary.
# 3. It shows none.
# 4. Instate of none we can write our own statement inside it and that statement displayed in the output.

'''6. what is the difference between list and tuple'''

# As List is mutable datatype when we create a list it occopies some block of memory. As the list support append
# operation we can add element inside the list. So the list is flexible and dynamic in nature. But in case of tuple
# as it is immutable datatype so append is not possible inside the tuple. So tuple is not flexible and it shows the
# static nature. That's why tuple is more memory efficient than list.

'''7. difference between xrange and range'''

# python2 - xrange
# python3 - range

# 1. xrange does not have start, stop and step attributes
#     But range object has start, stop and step attributes

# 2. range object supports slicing whereas xrange does not support
#     slicing

# 3. range object has __contains__, so it supports membership
#     operator
#     But xrange does not implement __contains__ method


'''8. what is the difference between append method and extend method in list'''

# append method adds one item at the end of the list
# extend method adda all the items of the iterable at the end of the list
# Both append and extend will add the elements to the end of the list
# l = [1, 2, 3]
# l.append('hai')
# print(l)
# l.extend('100')
# print(l)

'''9. Why python is object oriented
      Because in Python, everything is an object(defined as class)'''

# a = 10
# '10' is a value which is stored in a memory and 'a' is a variable which is indicating that memory location. Now I
# change the value a = 'hello'. Right now 'a' is pointing to a string due to this dynamic nature so python is called as
# Object oriented.

'''10. what are .pyc files '''

# When we compile .py file we get bite code that is nothing but the .pyc file also called pythonic class file

'''11. Difference between while and for loop'''


'''12. What are magic methods'''

# magic method is called as __ method or dunder method which is going behind the function
# ex in case of len function __len__ method is going and in case of in __contains__ is going and also in case of ()
# __call__ method is going


'''13. What is pylint'''

'''14. what is the difference between is and == operator '''

# a = [1, 2, 3, 4]
# b = a[:]
# print(b)
# print(a == b)
# print(a is b)

'''15. What is self in the class'''
# Self is the first argument inside a class by which we pass the memory address of object instance of a class.
# it is mandatory argument and instate of self we can write anything but according to the industrial standred we write self.

'''141. What is assert statement. what is the difference between assert and if/else statement'''

# assert 3==3
# print('hello world')

'''142. What is the difference between a module, a package and a library'''

