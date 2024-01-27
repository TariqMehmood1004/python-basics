
'''
    y is initially a list containing two empty lists: y = [[], []]
    Assigning the second element to the first element (y[0] = y[1]) 
    makes both elements reference the same list.
    Appending 1 to the second empty list (index 1) affects both elements 
    since they reference the same list.
    This example demonstrates the impact of assignment and mutability 
    when working with nested lists in Python. Understanding these concepts is 
    crucial for avoiding unexpected behavior in your programs.
'''

# Python Program #2 - List of Lists

# Initializing y as a list containing two empty lists
y = [[], []]

# Displaying the initial state of the list
print(f"Initial State: {y}")

# Assigning the second element to the first element (they now reference the same list)
y[0] = y[1]

# Appending 1 to the second empty list (index 1)
y[1].append(1)

# Displaying the final state of the list
print(f"Final State: {y}")


