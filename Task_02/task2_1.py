input_str = input("Your string:")

input_str = input_str.casefold()

rev_str = input_str[::-1]

if input_str == rev_str:
    print(input_str + " - it is palindrome")
else:
    print(input_str + " - it is not palindrome")
