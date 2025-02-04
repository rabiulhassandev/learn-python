# String
# In Python, a string is a sequence of Unicode characters. It is a sequence of characters enclosed within single, double, or triple quotes. For example, 'Python', "Python", or """Python""".

# Example: How to create a string in Python
# Single line string
name = "Python"
print(name)

# Multi-line string
description = """Python is a high-level, interpreted, 
interactive and object-oriented scripting language."""
print(description)

# Accessing characters in a string
# We can access characters in a string using the index. The index starts from 0. We can access a character using the index in square brackets.

# Example: How to access characters in a string
name = "Python"
print(name[0]) # P
print(name[1]) # y
print(name[2]) # t
print(name[3]) # h
print(name[4]) # o
print(name[5]) # n
print(name[-1]) # n
print(name[-2]) # o
print(name[-3]) # h
print(name[-4]) # t
print(name[-5]) # y
print(name[-6]) # P

# Slicing a string
# Slicing is used to get a substring from a string. We can specify the start and end index to get a substring. The syntax of slicing is string[start:end].

# Example: How to slice a string
name = "Python"
print(name[0:2]) # Py
print(name[2:5]) # tho
print(name[1:6]) # ython
print(name[:4]) # Pyth
print(name[2:]) # thon
print(name[:]) # Python
print(name[0:6:2]) # Pto
print(name[0:6:3]) # Ph

# String Concatenation
# We can concatenate two or more strings using the + operator.

# Example: How to concatenate strings
first_name = "Rabiul"
last_name = "Hassan"
full_name = first_name + " " + last_name
print(full_name) # Rabiul Hassan

# String Repetition
# We can repeat a string multiple times using the * operator.

# Example: How to repeat a string
name = "Python"
print(name * 3) # PythonPythonPython

# String Methods
# Python has many built-in methods that you can use on strings. Here are some of the most commonly used string methods:

# capitalize() - Converts the first character to upper case
# lower() - Converts all characters to lower case
# upper() - Converts all characters to upper case
# title() - Converts the first character of each word to upper case
# swapcase() - Swaps cases, lower case becomes upper case and vice versa
# len() - Returns the length of the string
# strip() - Removes any whitespace from the beginning or the end
# replace() - Replaces a string with another string
# split() - Splits the string into a list
# join() - Joins the elements of a list into a string
# find() - Searches the string for a specified value and returns the position of where it was found
# count() - Returns the number of times a specified value occurs in a string
# startswith() - Returns true if the string starts with the specified value
# endswith() - Returns true if the string ends with the specified value
# isalnum() - Returns true if all characters in the string are alphanumeric
# isalpha() - Returns true if all characters in the string are in the alphabet
# isdigit() - Returns true if all characters in the string are digits
# islower() - Returns true if all characters in the string are lower case
# isupper() - Returns true if all characters in the string are upper case
# istitle() - Returns true if the string follows the rules of a title
# isspace() - Returns true if the string contains only whitespace

# Example: How to use string methods
name = "Rabiul Hassan"
print(name.capitalize()) # Rabiul hassan
print(name.lower()) # rabiul hassan
print(name.upper()) # RABIUL HASSAN
print(name.title()) # Rabiul Hassan
print(name.swapcase()) # rABIUL hASSAN
print(len(name)) # 12
print(name.strip()) # Rabiul Hassan
print(name.replace("Rabiul", "Python")) # Python Hassan
print(name.split(" ")) # ['Rabiul', 'Hassan']
print("-".join(["Rabiul", "Hassan"])) # Rabiul-Hassan
print(name.find("Hassan")) # 7
print(name.count("a")) # 3
print(name.startswith("Rab")) # True
print(name.endswith("san")) # True
print(name.isalnum()) # False
print(name.isalpha()) # False
print(name.isdigit()) # False
print(name.islower()) # False
print(name.isupper()) # False
print(name.istitle()) # True
print(name.isspace()) # False

# Escape Characters
# In Python, an escape character is a backslash \ followed by a character. It is used to represent characters that are difficult or impossible to type directly. For example, \n represents a new line, \t represents a tab, and \\ represents a backslash.

# Here are some of the most commonly used escape characters:

# \n - New Line
# \t - Tab
# \\ - Backslash
# \' - Single Quote
# \" - Double Quote

# Example: How to use escape characters
print("Hello\nWorld") # Hello
                      # World
print("Hello\tWorld") # Hello   World
print("Hello\\World") # Hello\World
print("Hello\'World") # Hello'World
print("Hello\"World") # Hello"World

# String Formatting
# String formatting allows you to format a string with placeholders that are replaced by the values of variables. There are three ways to format a string in Python:

# Using the % operator
# Using the format() method
# Using f-strings (Python 3.6+) - f-strings are prefixed with 'f' and are enclosed in curly braces {}

# Using the % Operator
# The % operator is used to format a string using a format string and a tuple of values. The format string contains placeholders %s, %d, %f, etc. that are replaced by the values of the tuple.

# Example: How to format a string using the % operator
name = "Python"
version = 3.8
print("Welcome to %s %s" % (name, version)) # Welcome to Python 3.8

# Using the format() Method
# The format() method is used to format a string using curly braces {} as placeholders. The values are passed as arguments to the format() method.

# Example: How to format a string using the format() method
name = "Python"
version = 3.8
print("Welcome to {} {}".format(name, version)) # Welcome to Python 3.8
print("Welcome to {0} {1}".format(name, version)) # Welcome to Python 3.8
print("Welcome to {name} {version}".format(name="Python", version=3.8)) # Welcome to Python 3.8

# Using f-strings
# f-strings are prefixed with 'f' and are enclosed in curly braces {}. The values are passed directly inside the curly braces.

# Example: How to format a string using f-strings
name = "Python"
version = 3.8
print(f"Welcome to {name} {version}") # Welcome to Python 3.8


# String Interpolation
# String interpolation is the process of evaluating a string containing one or more placeholders. The placeholders are replaced by the values of variables. It is also known as string formatting.

# Example: How to use string interpolation
name = "Python"
version = 3.8
print(f"Welcome to {name} {version}") # Welcome to Python 3.8
