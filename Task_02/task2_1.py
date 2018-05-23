input_str = (input("Your string:"))

input_str = input_str.casefold()

rev_str = input_str[::-1]

if list(input_str) == list(rev_str):
    print(input_str + " - it is palindrome")
else:
    print(input_str + " - it is not palindrome")
