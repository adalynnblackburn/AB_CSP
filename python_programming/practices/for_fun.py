import random

print("🌄 Welcome to The Oregon Trail (Short Edition) 🌄")
print("Travel 500 miles to Oregon before you run out of food or die!\n")

# Starting stats
miles = 0
food = 300
health = 100
ammo = 50
money = 100
day = 1

def status():
    print(f"\nDay {day}: {miles}/500 miles traveled.")
    print(f"Food: {food}  Health: {health}  Ammo: {ammo}  Money: ${money}")

def random_event():
    global food, ammo, health, miles
    roll = random.random()
    if roll < 0.1:
        print("🌪️ A storm slowed you down. Lose 10 miles.")
        miles = max(0, miles - 10)
    elif roll < 0.15:
        print("💀 A party member got sick. -10 health.")
        health -= 10
    elif roll < 0.20:
        lost = random.randint(10, 30)
        food = max(0, food - lost)
        print(f"🐀 Rats ate {lost} food.")
    elif roll < 0.23:
        print("🏕️ You found abandoned supplies! +20 food, +10 ammo.")
        food += 20
        ammo += 10

def river_cross():
    global miles, food, health, money
    print("🌊 You’ve reached a river!")
    print("Options: [F]ord the river (risky) or [P]ay $10 for a ferry (safe)")
    choice = input("> ").lower()
    if choice == "p":
        if money >= 10:
            money -= 10
            print("You paid and crossed safely.")
        else:
            print("Not enough money! You must ford instead.")
            choice = "f"
    if choice == "f":
        if random.random() < 0.3:
            print("Your wagon tipped! Lost 30 food and 10 health.")
            food = max(0, food - 30)
            health -= 10
        else:
            print("You crossed safely!")
    miles += 10

def trading_post():
    global food, ammo, money
    print("🏪 You reached a trading post!")
    print("You can buy: [1] 50 food for $10, [2] 20 ammo for $10, [3] Leave")
    choice = input("> ")
    if choice == "1" and money >= 10:
        money -= 10
        food += 50
        print("You bought 50 food.")
    elif choice == "2" and money >= 10:
        money -= 10
        ammo += 20
        print("You bought 20 ammo.")
    else:
        print("You continue your journey.")

while miles < 500 and health > 0 and food > 0:
    status()
    print("\nChoose: [T]ravel  [R]est  [H]unt  [S]tatus  [Q]uit")
    choice = input("> ").lower()

    if choice == "t":
        dist = random.randint(20, 40)
        miles += dist
        food -= 10
        print(f"You traveled {dist} miles.")
        # special events
        if miles % 100 == 0:
            river_cross()
        elif miles % 150 == 0:
            trading_post()
        else:
            random_event()

    elif choice == "r":
        print("You rested and recovered 10 health.")
        health = min(100, health + 10)
        food -= 5

    elif choice == "h":
        if ammo < 5:
            print("Not enough ammo to hunt!")
        else:
            ammo -= 5
            if random.random() < 0.6:
                found = random.randint(20, 50)
                food += found
                print(f"You hunted successfully and got {found} food!")
            else:
                print("You didn’t find any animals.")

    elif choice == "s":
        status()
        continue

    elif choice == "q":
        print("You gave up your journey west.")
        break

    else:
        print("Invalid choice.")
        continue

    # End-of-day effects
    day += 1
    food -= 5
    health -= 2

# Ending
print("\n🏁 Final Results 🏁")
if miles >= 500:
    print("🎉 You made it to Oregon safely! Congratulations, pioneer!")
elif health <= 0:
    print("💀 Your party has perished on the trail.")
else:
    print("🥀 You ran out of food and couldn’t continue.")
print(f"Days traveled: {day}, Miles: {miles}, Food: {food}, Health: {health}, Ammo: {ammo}, Money: ${money}")
