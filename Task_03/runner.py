import pytask


def runner(args):
    if args != 0:
        for i in args:
            getattr(pytask, i)()
    else:
        getattr(pytask, 'generate_numbers')()
        getattr(pytask, 'count_characters')()
        getattr(pytask, 'fizzbuzzz')()
        getattr(pytask, 'is_palindrome')()
    return


runner(['generate_numbers', 'fizzbuzzz'])
