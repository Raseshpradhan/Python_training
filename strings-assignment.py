"""
Write a Program to retrieve character 'X' using positive indexing
from "Semantic segmentation of Lung Cancer from Chest X-Ray" string
"""
x='"Semantic segmentation of Lung Cancer from Chest X-Ray"'
print(x[49])
'''
Write a Program to retrieve the 'L' character from "I have to Love Python Programming" string
using negative/reverse indexing
'''
x="I have to Love Python Programming"
print(x[10])

'''
Can prove that python string is immutable with the program
'''
x="rasesh"
print(x[2])
#if we modify
x[2]=y
print(x)#output showing y not define hence proved that python string is immutable