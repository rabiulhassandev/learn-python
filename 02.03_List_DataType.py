# List
# List is a collection which is ordered and changeable. It allows duplicate members. List is defined by square brackets []. The elements in a list are separated by commas.

# Example: How to create a list
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]


# Accessing elements in a list
# We can access elements in a list using the index. The index starts from 0. We can access an element using the index in square brackets.

# Example: How to access elements in a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # 1
print(my_list[1]) # 2
print(my_list[2]) # 3
print(my_list[3]) # 4
print(my_list[4]) # 5
print(my_list[-1]) # 5
print(my_list[-2]) # 4
print(my_list[-3]) # 3
print(my_list[-4]) # 2
print(my_list[-5]) # 1


# Slicing a list
# Slicing is used to get a sublist from a list. We can specify the start and end index to get a sublist. The syntax of slicing is list[start:end].

# Example: How to slice a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0:2]) # [1, 2]
print(my_list[2:5]) # [3, 4, 5]
print(my_list[1:5]) # [2, 3, 4, 5]
print(my_list[:4]) # [1, 2, 3, 4]
print(my_list[2:]) # [3, 4, 5]
print(my_list[:]) # [1, 2, 3, 4, 5]
print(my_list[0:5:2]) # [1, 3, 5]
print(my_list[0:5:3]) # [1, 4]

# List Concatenation
# We can concatenate two or more lists using the + operator.

# Example: How to concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list) # [1, 2, 3, 4, 5, 6]

# List Repetition
# We can repeat a list multiple times using the * operator.

# Example: How to repeat a list
my_list = [1, 2, 3]
print(my_list * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# List Methods
# Python provides many built-in methods to work with lists. Here are some of the most commonly used list methods:

# append(): Adds an element at the end of the list
# clear(): Removes all the elements from the list
# copy(): Returns a copy of the list
# count(): Returns the number of elements with the specified value
# extend(): Add the elements of a list (or any iterable), to the end of the current list
# index(): Returns the index of the first element with the specified value
# insert(): Adds an element at the specified position
# pop(): Removes the element at the specified position
# remove(): Removes the first item with the specified value
# reverse(): Reverses the order of the list
# sort(): Sorts the list

# Example: How to use list methods
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list) # [1, 2, 3, 4, 5, 6]

my_list.clear()
print(my_list) # []

my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list) # [1, 2, 3, 4, 5]

count = my_list.count(3)
print(count) # 1

my_list.extend([6, 7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

index = my_list.index(3)
print(index) # 2

my_list.insert(2, 9)
print(my_list) # [1, 2, 9, 3, 4, 5, 6, 7, 8]

my_list.pop(2)
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list.remove(3)
print(my_list) # [1, 2, 4, 5, 6, 7, 8]

my_list.reverse()
print(my_list) # [8, 7, 6, 5, 4, 2, 1]

my_list.sort()
print(my_list) # [1, 2, 4, 5, 6, 7, 8]


# List Comprehension
# List comprehension is an elegant way to define and create lists based on existing lists.

# Example: How to use list comprehension
my_list = [1, 2, 3, 4, 5]
new_list = [x * x for x in my_list]
print(new_list) # [1, 4, 9, 16, 25]
