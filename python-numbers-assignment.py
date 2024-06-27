"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
a=75
PI=3.14
print(a,PI)
print(type(a),type(PI))

'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
a=3+7j
b=8-5J
print(a,b)
print(type(a),type(b))

'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
import sys
x=111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999000000000
print(x)
print(sys.getsizeof(x))
print(type(x))
