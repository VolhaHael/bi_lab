# 1 Create the list ['a', 'b', 'c'], then create a tuple from that list.

list_1 = ['a', 'b', 'c']
tuple_1 = tuple((list_1[:]))
print('list: ')
print(list_1)
print('tuple: ')
print(tuple_1)
print()

# 2 Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered, but it's
# not entirely obvious)

tuple_2 = ('a', 'b', 'c')
list_2 = list(tuple_2[:])
print('tuple: ')
print(tuple_1)
print('list: ')
print(list_2)
print()

# 3 Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code).

a, b, c = 'a', 2, 'gamma'
print(a)
print(b)
print(c)
print()

# 4 Create a tuple containing just a single element which in turn
# contains the three elements 'a', 'b', and 'c'. Verify that the
# length is actually 1 by using the len() function.

tuple_3 = (['a', 'b', 'c'],)
print(tuple_3)
print(len(tuple_3))
