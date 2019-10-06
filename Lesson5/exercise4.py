'''
@author: cristianlepore
'''

L = [2, 1, 3]
print(L)

# Append will append only one element to the list, while with the command extend you can add more element to a list
L.append([5, 6])
print(L)
L.extend([7, 8])
print(L)

# New example
s = 'abc'
L = list(s)
print(L)

L = [4, 2, 9]
print(sorted(L))
# Notice that L is not changed
print(L)

# This will return None
print(L.sort())
# The list is now sorted
print(L)

# Reverse the list L
L.reverse()
print(L)
