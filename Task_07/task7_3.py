# function to compute 5/0 with try/except
def zero_div():
    try:
        print(5/0)
    except ZeroDivisionError as zde:
        for err in zde.args:
            print(err)


# IndexError
def print_list_element(the_list, index):
    try:
        print(the_list[index])
    except IndexError:
        print("Index is out of bounds!")


def add_to_list_in_dict(the_dict, list_name, element):
    try:
        length = the_dict[list_name]
        print("%s already has %d elements." % (list_name, len(length)))
    except KeyError:
        the_dict[list_name] = []
        print("Created %s." % list_name)
    finally:
        the_dict[list_name].append(element)
        print("Added %s to %s." % (element, list_name))


# zero test
zero_div()

# IndexError test
print_list_element(["a", "b", "c"], 3)

# dict test
test_dict = {"a": [1, 2, 3, 5], "b": [3, 6, 9]}
add_to_list_in_dict(test_dict, "c", 10)
add_to_list_in_dict(test_dict, "a", 6)
