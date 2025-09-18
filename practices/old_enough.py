# AB 7th Old Enough

age = int(input("What is your age?: "))

if age >= 18 and age < 100:
    print("You are old enough to vote!")
elif age >= 16 and age < 18:
    print("You are old enough to drive!")
elif age >= 15 and age < 16:
    print("You are old enough to get a learners permit!")
elif age >= 4 and age < 15:
    print("You should go to school!")