# This program demonstrates control structures in Python

# if-else statement
num = 10
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

# while loop
i = 0
while i < 5:
    print("Counting: " + str(i))
    i += 1

# for loop
for j in range(3):
    print("Hello!")

# nested loop
for row in range(3):
    for col in range(3):
        print("(" + str(row) + ", " + str(col) + ")")

# break and continue statements
for k in range(10):
    if k == 5:
        break  # exit the loop when k equals 5
    if k % 2 == 0:
        continue  # skip even numbers
    print(k)
