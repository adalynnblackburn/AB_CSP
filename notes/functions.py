# AB 7th Functions Notes

def welcome():
    name = input("What is your name?")
    print(f"Hello, {name}!")

welcome()
welcome()
welcome()
welcome()

def add(number, number_two):
    number += number_two
    print(number)

num_one = 12
num_two = 4

add(80, 8)
add(3, 6)
add(9, 20)
add(11, 71)
add(num_one, num_two)

import random

def roll(mod):
    return random.randint(2,18) + mod

strength = roll(0)
dextarity = roll(1)
intelligence = roll(1)
charisma = roll(0)
print("Here are your stats!")
print(f"Strength: {strength}\nDex: {dextarity}\nInt: {intelligence}\nChar: {charisma}")