# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# Creating a set
my_set = {"apple", "banana", "cherry"}
print(my_set) # {'banana', 'apple', 'cherry'}

# Access Items
for item in my_set:
    print(item) # banana, apple, cherry

# Add Items
my_set.add("orange")

# Update Items
my_set.update(["mango", "grapes"])

# Remove Items
my_set.remove("banana")

# Clear Items
my_set.clear()

# Delete Set
del my_set

# Set Methods
# add() - Adds an element to the set
# clear() - Removes all the elements from the set
# copy() - Returns a copy of the set
# difference() - Returns a set containing the difference between two or more sets
# difference_update() - Removes the items in this set that are also included in another, specified set
# discard() - Remove the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() - Returns a set with the symmetric differences of two sets
# symmetric_difference_update() - inserts the symmetric differences from this set and another
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others

# Frozen Set
# A frozen set is a set that is immutable. Once it is created, you cannot change its items.

# Creating a frozen set
my_frozen_set = frozenset({"apple", "banana", "cherry"})
print(my_frozen_set) # frozenset({'banana', 'apple', 'cherry'})