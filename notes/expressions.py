# AB 7th Expressions notes

# What is an algorithm?
name = input("What is your name:\n")
print("Hello",name)

# Treyson has 12 apples, he has 5 friends that he wants to give apples to. How many apples does each friend get?
apples = 12
friends = 5
print("Each friend gets", apples/friends, "apples!")

# Average age of a group of 4 people
friend1 = 13
friend2 = 2
friend3 = 65
friend4 = 34
total = friend1+friend2+friend3+friend4/4
print("The average age of the 4 friends is", total)

num_one = int(input("Tell me a number:\n"))
num_two = float(input("Tell me another number\n"))
num_one += num_two
print("Addition(+): ", num_one)
num_one -= num_two
print("Subtraction(-): ", num_one)
num_one *= num_two
print("Multiplication(*): ", num_one)
num_one /= num_two
print("Division(/): ", round(num_one, 2)) # round(number to round, number of decimal places)
num_one **= num_two
print("Exponents(**): ", num_one)
num_one //= num_two
print("Integer Division(//): ", num_one)
num_one %= num_two
print("Modulo(%): ", num_one)