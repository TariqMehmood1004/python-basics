
# Python Data Structures
# 1. List [] - Mutable - Changeable
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10
print(f"List: {my_list}")


# Tuple () - Immutable - Unchangeable
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10
print(f"Tuple: {my_tuple}")



# # Set - {} - Mutable - Changeable
my_set = {1, 2, 3, 4, 5}
my_set.add(10)
print(f"Set: {my_set}")

# # Dictionary - {} - Mutable - Changeable
my_dict = {
    'name': {
        'first': "Tariq",
        'last': "Mehmood",
        'alias': {
            'first': "John",
            'last': "Brrighte",
        },
    }, 
    'age': 21, 
    'address': 'Pakistan',
}
print(f"Dictionary: {my_dict}")
print(f"Name: {my_dict['name']['first']}")
print(f"Name: {my_dict['name']['alias']['first']}")