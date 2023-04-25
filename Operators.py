# This program demonstrates operators in Python

# Arithmetic operators
num1 = 10
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)

# Comparison operators
print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

# Logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# Bitwise operators
a = 60  # 0011 1100
b = 13  # 0000 1101
print(a & b)   # 0000 1100
print(a | b)   # 0011 1101
print(a ^ b)   # 0011 0001
print(~a)      # 1100 0011
print(a << 2)  # 1111 0000
print(a >> 2)  # 0000 1111

# Assignment operators
num3 = 5
num3 += 2  # equivalent to num3 = num3 + 2
print(num3)
num3 *= 3  # equivalent to num3 = num3 * 3
print(num3)
