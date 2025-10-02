# AB 7th Loops Notes

foods = ["Chocolate", "Pasta", "Brownies", "Cookies", "Garlic", "Bread", "Fajitas"]

#For Loop
for food in foods:
    print(f"{food} is my favorite food!")
    print("Hi!")

for x in range(1,21):
    print(x)

#While loops
#Infintite loop (one of 3 steps missing)
#correct while loop:
i = 1
while i <= 20:
    print(i)
    i+= 1

x = 1
while x < 21:
    if x % 2 == 0:
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number.")
    x += 1

import random

d = 1
end = random.randint(1,20)

while d != end:
    print("Duck")
    d += 1

print("Goose")

while True:
    if d == end:
        print("Goose!")
        break
    else:
        print("Duck")
        d += 1