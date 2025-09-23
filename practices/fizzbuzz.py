# AB 7th FizzBuzz

x = 1
while x < 51:
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{x}")
    x += 1