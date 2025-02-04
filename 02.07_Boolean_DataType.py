# Boolean
# In Python, the Boolean data type is used to represent the truth values of logic and can have two values: True or False.

# Creating a boolean variable
is_python = True
print(is_python) # True

# Example
# Boolean values are returned when you compare two values
x = 10
y = 20
print(x > y) # False
print(x < y) # True
print(x == y) # False
print(x != y) # True
print(x >= y) # False
print(x <= y) # True
print(x is y) # False
print(x is not y) # True
print(x in [10, 20, 30]) # True
print(x not in [10, 20, 30]) # False
print(x is 10) # True
print(x is not 10) # False
print(x in range(1, 11)) # True
print(x not in range(1, 11)) # False

# Boolean values are returned when you use the bool() function
print(bool(0)) # False
print(bool(1)) # True
print(bool("Hello")) # True
print(bool("")) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(bool(None)) # False