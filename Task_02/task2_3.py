for fizz_buzz in range(101):
    if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizz_buzz % 3 == 0:
        print("Fizz")
        continue
    elif fizz_buzz % 5 == 0:
        print("Buzz")
        continue
    print(fizz_buzz)
