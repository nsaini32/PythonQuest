# This program demonstrates input/output (I/O) in Python

# Input
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello, " + name + "! You are " + age + " years old.")

# Output to file
file = open("output.txt", "w")
file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.close()
print("Output written to file: output.txt")

# Input from file
file = open("input.txt", "r")
lines = file.readlines()
file.close()
print("Contents of input.txt:")
for line in lines:
    print(line.strip())
