# This program demonstrates functions in Python

# Function definition
def greet(name):
    print("Hello, " + name + "!")

# Function call
greet("Alice")

# Function with return value
def add(num1, num2):
    return num1 + num2

result = add(2, 3)
print("2 + 3 = " + str(result))

# Function with default parameter
def power(base, exp=2):
    return base ** exp

print("2 ^ 3 = " + str(power(2, 3)))
print("2 ^ 2 = " + str(power(2)))

# Function with variable number of arguments
def sum_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print("1 + 2 + 3 + 4 = " + str(sum_all(1, 2, 3, 4)))
