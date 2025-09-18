# AB 7th Conditionals Notes

homework_done = input("Is your homeword done: ").strip().capitalize()

if homework_done == "Yes":
    print("Yes you can go!")

else:
    print("Then go do your homework!")

grade = 120
if grade >= 90:
    if grade > 100:
        print("You cheated that isn't possible!")
    else:
        print(f"You have {grade}% that is an A!")
elif grade >= 80 and not grade > 100:
    print(f"You have {grade}% that is a B!")
elif grade >= 70 and not grade > 100:
    print(f"You have a {grade}% that is not an C!")
else:
    print(f"You have a {grade}% that is a D or lower :(")


name = input("What is your name: ")

if name == "Ms LaRose":
    print("You are the teacher!")
elif name == "Tia" or name == "Ashley":
    print("You are the TA")
else:
    print(f"Hello {name}, you are a student!")