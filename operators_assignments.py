'''# What will be the output of following statements
print({1, 2, 3, 5} - {3, 4, 7, 8})
#o/p is -{1, 2, 5}
print({1, 2, 3, 5} + {3, 4, 7, 8})
#o/p is -unsupported operand type(s) for +: 'set' and 'set'
# What will be the output of following programs'''
'''print('Hi ' + 'Anil')
#o/p is - Hi Anil
print([1, 2] + [3, 4])
#o/p is - [1, 2, 3, 4]
print('Hi' + [1, 2])
#o/p is -can only concatenate str (not "list") to str'''
# What will be the output of following programs
print((1, 2, 3) * 4)
#0p is - (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(8 // 3)
#op is 2

print(21 % 6)
#op is - 3

# What will be the output of following programs
a = 7
a /= 2
print(a)  # 3.5
#op is - 3.5
b = 5
print(b > 5 and b < 10)  # Also write the short form for this expression
#op is - false
print(5 < b < 10)
#op is - false

# Write the output of following programs
print(4 and 6)
#op is - 6
print(1 or 5)
#op is - 1
print(not 7)
#op is - false

# what is the output of following programs
print(2 not in [3, 4, 5, 2, 9])
#op is - false
print([1, 2, 5, (1, 2)] in ['hi', 3, 4, 5, 2, 9, [1, 2, 5, (1, 2)]])
#op is - true

# what is the output of following programs
a = 400.30123
b = 400.30123
print(a is b)
#op is - true

i = 23
j = 23
print(i is j)
#op is - true
print(i == j)
#op is - true

a1 = 999
b1 = 999
print(a1 is b1)
#op is - true
print(a1 == b1)
#op is - true

y = 4
z = -4
print(y == z)
#op is - false

s1 = 4096 * 'a'
s2 = 4096 * 'a'
print(s1 is s2)
#op is - true

# write the output of following programs
a = 2
b = 11
print(a & b)
#op is - 2
print(a | b)
#op is - 11
print(a ^ b)
#op is - 9
print(~b)
#op is - -12
print(a << 3)
#op is - 16
print(b >> 2)
#op is - 2

# write the output of following programs
print(+-4)
#op is - -4
print(--4)
#op is - 4
a = [1, 2, 3]
print(2 * a[1] << 2 > 8 and 9)
#op is - 9
print(2 * 3 - 3 ** 2 ** 1 & 5 // 2 + (4 + 2) or 5)
#op is - 8