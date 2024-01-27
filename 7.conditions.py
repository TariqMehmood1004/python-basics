'''
    Conditions:
    1. if-condition
    2. if-else condition
    3. if-elif-else condition
'''
number = int(input("Enter your number: "))

"""if (number > 0):
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
    

# 4%2 == 0
#    2
#    __
# 2 |4
#   - 4
#   __
#   0

# Nested Conditions
if (number > 0):
    if (number % 2 == 0):
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif number < 0:
    if (number % 2 == 0):
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")
"""

# Nested Conditions
if number>0:
    print(f"Positive: {number}")
    if number % 2 == 0:
        print(f"Even: {number}")
    else:
        print(f"Odd: {number}")
elif number < 0:
    print(f"Negative: {number}")
    if number % 2 == 0:
        print(f"Even: {number}")
    else:
        print(f"Odd: {number}")
else:
    print("Zero")