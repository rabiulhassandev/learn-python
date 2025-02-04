# Tuple
# Tuple is a collection of items which is ordered, unchangeable, and allow duplicate values.


# Empty Tuple
empty_tuple = ()
print(empty_tuple)  # ()

# Tuple with items
tuple_with_items = (1, 2, 3, 4, 5)
print(tuple_with_items)  # (1, 2, 3, 4, 5)

# Tuple with mixed data types
tuple_mixed_data_types = (1, "Hello", 3.4)
print(tuple_mixed_data_types)  # (1, 'Hello', 3.4)

# Tuple with nested tuple
tuple_nested_tuple = (1, (2, 3, 4), 5)
print(tuple_nested_tuple)  # (1, (2, 3, 4), 5)

# Tuple with one item
tuple_one_item = (1,)
print(tuple_one_item)  # (1,)

# Tuple without parenthesis
tuple_without_parenthesis = 1, 2, 3, 4, 5
print(tuple_without_parenthesis)  # (1, 2, 3, 4, 5)

# Access Tuple Items
print(tuple_with_items[0])  # 1
print(tuple_with_items[-1])  # 5
print(tuple_nested_tuple[1][0])  # 2

# Slicing Tuple
print(tuple_with_items[1:4])  # (2, 3, 4)

# Change Tuple Values
# Tuple is unchangeable, so you cannot change, add, or remove items after the tuple has been created.
# But you can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple_to_list = list(tuple_with_items)
tuple_to_list[1] = 6
tuple_with_items = tuple(tuple_to_list)
print(tuple_with_items)  # (1, 6, 3, 4, 5)

# Loop Through Tuple
for item in tuple_with_items:
    print(item)

# Check if Item Exists
if 1 in tuple_with_items:
    print("Yes, 1 is in tuple_with_items")

# Tuple Length
print(len(tuple_with_items))  # 5

# Add Items
# You cannot add items to a tuple. Tuples are unchangeable.

# Remove Items
# You cannot remove items in a tuple. Tuples are unchangeable.

# Join Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Multiply Tuples
tuple4 = tuple1 * 2
print(tuple4)  # (1, 2, 3, 1, 2, 3)

# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
print(tuple_with_items.count(1))  # 1
print(tuple_with_items.index(1))  # 0


# Using Asterisk *
# If the number of variables is less than the number of items, you can add an * to the variable name and the values will be assigned to the variable as a list.
tuple_unpack = (1, 2, 3, 4, 5)
a, b, *c = tuple_unpack
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]

# Loop Through Tuple
for item in tuple_unpack:
    print(item)
