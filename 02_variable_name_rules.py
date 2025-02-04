# Rules for Python variables:
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)

# Examples of valid variable names:
myvar = "Hassan"
my_var = "Hassan"
_my_var = "Hassan"
myVar = "Hassan"
MyVar = "Hassan"
MYVAR = "Hassan"
myvar2 = "Hassan"

# Examples of invalid variable names:
# 2myvar = "Hassan"
# my-var = "Hassan"
# my var = "Hassan"
# myVar@ = "Hassan"
# myvar! = "Hassan"











# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "Hassan"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "Hassan"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "Hassan"

# Many developers use snake_case in Python, but choose the naming convention that you like the most.
# Remember that variable names are case-sensitive.
# This will create two variables: y and Y
y = 4
Y = "Hassan"
# Y will not overwrite y
print(y)

# Assign Value to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z = x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# If you try to combine a string and a number, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

