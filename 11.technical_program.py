'''
    PROBLEM#1 - Array
        x is a one-element list containing an empty list
        Then we multiply it by 2
        creating seemingly two-element list, [[], []]
        Be careful though, the two empty lists inside x are REFERENCES of each other.
        Anything that happens to one, Also happens to the other.
        So, x is showing, when we append 2 to the second empty list (index 1),
        it also happens it to the first element of list.
'''

x = [[]] * 2
print(x)

x[1].append(10);
print(x)


