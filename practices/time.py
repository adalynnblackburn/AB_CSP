# AB 7th Time Practice

time = int(input("What time is it right now in military time?\n"))

if time >= 5 and time <12:
    print("Good Morning!")
elif time >= 12 and time < 18:
    print("Good Afternoon")
elif time >= 18 and time <20:
    print("Good evening")
else:
    print("Go back to bed!")