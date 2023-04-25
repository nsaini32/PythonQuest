# This program introduces basic Python syntax and data types

# Let's start with variables
name = "Alice"   # A string data type
age = 10         # An integer data type
is_student = True # A boolean data type

# Print some messages using these variables
print("Hello, my name is " + name)
print("I am " + str(age) + " years old")
print("I am a student: " + str(is_student))

# Now let's do some arithmetic
num1 = 5
num2 = 2
result = num1 + num2
print(str(num1) + " + " + str(num2) + " = " + str(result))

# Let's also use some conditional statements
if age < 18:
    print("You are not an adult yet")
else:
    print("You are an adult")

# And a loop
for i in range(5):
    print("Counting: " + str(i))
