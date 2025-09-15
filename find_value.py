# Dictionary example
my_dict = {"name": "Rani", "age": 23, "city": "Mumbai"}

# Find value in dictionary
key_to_find = "age"
if key_to_find in my_dict:
    print(f"Value of '{key_to_find}' in dictionary is: {my_dict[key_to_find]}")
else:
    print(f"Key '{key_to_find}' not found in dictionary.")

# Tuple example
my_tuple = (10, 20, 30, 40, 50)

# Find value in tuple
value_to_find = 30
if value_to_find in my_tuple:
    print(f"Value {value_to_find} found in tuple at index {my_tuple.index(value_to_find)}")
else:
    print(f"Value {value_to_find} not found in tuple.")
