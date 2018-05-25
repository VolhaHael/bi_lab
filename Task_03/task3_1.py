# 1 Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

list_1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
print(list_1)

# 2 Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].

list_2 = list_1[::2]
print()
print(list_2)

# 3 Use a list comprehension to construct
# the list ['1a', '2a', '3a', '4a'].

list_3 = ['1a', '2a', '3a', '4a']
print()
print('list_1 and list_3 the same: ')
print(list_1 == list_3 and list_3 == list_1)

# 4 Simultaneously remove the element '2a' from
# the above list and print it.

del list_3[1]
print()
print('After deleting: ')
print(list_3)

# 5 Copy the above list and add '2a' back
# into the list such that the original is still missing it.

list_4 = list_3[:]
list_4.append('2a')
print()
print('old version of list: ')
print(list_4)
print('new version of list: ')
print(list_3)
