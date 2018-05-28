# 1 Define a function generate_numbers(number) which returns a
# dictionary where the keys are numbers between 1 and n
# (both included) and the values are square of keys. n –
# function argument. Default is 20.


def generate_numbers(numbers=20):
    dict1_ = {}
    for i in range(1, numbers + 1):
        dict1_[i] = i * i
    return dict1_


print(generate_numbers())
print()

# 2 Define a function count_characters(count_me_string) which
# count and return the numbers of each character in a
# count_me_string argument.


def count_characters(count_me_string):
    dict_1 = {}
    for i in count_me_string:
        dict_1[i] = count_me_string.count(i)
    return dict_1


print(count_characters("aaabbcdd"))
