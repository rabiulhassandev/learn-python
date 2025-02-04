# Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Creating a dictionary
my_dict = {
    "name": "Python",
    "version": 3.8
}
print(my_dict) # {'name': 'Python', 'version': 3.8}

# Accessing Items
print(my_dict["name"]) # Python
print(my_dict.get("version")) # 3.8

# Change Values
my_dict["version"] = 3.9
print(my_dict) # {'name': 'Python', 'version': 3.9}

# Loop through a dictionary
for key in my_dict:
    print(key, my_dict[key]) 

# Adding Items
my_dict["year"] = 2020
print(my_dict) # {'name': 'Python', 'version': 3.9, 'year': 2020}

# Removing Items
my_dict.pop("year")
print(my_dict) # {'name': 'Python', 'version': 3.9}

# Copy a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy) # {'name': 'Python', 'version': 3.9}

# Nested Dictionary
my_dict = {
    "name": "Python",
    "version": 3.8,
    "author": {
        "name": "Guido van Rossum",
        "year": 1989
    }
}

print(my_dict) # {'name': 'Python', 'version': 3.8, 'author': {'name': 'Guido van Rossum', 'year': 1989}}

# Dictionary Methods
# clear() - Removes all the elements from the dictionary
my_dict.clear()
print(my_dict) # {}

# fromkeys() - Returns a dictionary with the specified keys and values
keys = ["name", "version", "author"]
values = "Python"
new_dict = dict.fromkeys(keys, values)
print(new_dict) # {'name': 'Python', 'version': 'Python', 'author': 'Python'}

# get() - Returns the value of the specified key
my_dict = {
    "name": "Python",
    "version": 3.8
}
print(my_dict.get("name")) # Python

# items() - Returns a list containing a tuple for each key value pair
print(my_dict.items()) # dict_items([('name', 'Python'), ('version', 3.8)])

# keys() - Returns a list containing the dictionary's keys
print(my_dict.keys()) # dict_keys(['name', 'version'])

# pop() - Removes the element with the specified key
my_dict.pop("version")
print(my_dict) # {'name': 'Python'}

# popitem() - Removes the last inserted key-value pair
my_dict.popitem()
print(my_dict) # {}

# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
my_dict = {
    "name": "Python",
    "version": 3.8
}
print(my_dict.setdefault("name")) # Python
print(my_dict.setdefault("year", 2020)) # 2020
print(my_dict) # {'name': 'Python', 'version': 3.8, 'year': 2020}

# update() - Updates the dictionary with the specified key-value pairs
my_dict.update({"year": 2021})
print(my_dict) # {'name': 'Python', 'version': 3.8, 'year': 2021}

# values() - Returns a list of all the values in the dictionary
print(my_dict.values()) # dict_values(['Python', 3.8, 2021])
