# AB 7th Conditionals Notes

homework_done = input("Is your homeword done: ").strip().capitalize()

if homework_done == "Yes":
    print("Yes you can go!")

else:
    print("Then go do your homework!")

grade = 84

if grade > 89:
    print(f"You have {grade}% that is an A!")
if grade > 79:
    print(f"You have {grade}% that is a B!")
else:
    print(f"You have a {grade}% that is not an C or lower :(")