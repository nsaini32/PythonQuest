# This program demonstrates Lists and Dictionaries in Python

# Lists
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)
print("The third fruit is: " + fruits[2])
fruits.append("kiwi")
print("The last fruit is: " + fruits[-1])
fruits.remove("cherry")
print("The remaining fruits are: " + str(fruits))

# Dictionaries
person = {"name": "Alice", "age": 20, "is_student": True}
print(person)
print("Name: " + person["name"])
print("Age: " + str(person["age"]))
person["is_student"] = False
print(person)
