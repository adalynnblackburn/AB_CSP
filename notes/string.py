# AB 7th String Notes

print("I did it!")

#Examples
first_name = input("What is your first name: \n").strip().title()

last_name = input("What is your last name: \n").strip().title()

full_name = first_name + " " + last_name

sentence = 'The quick brown fox jumps over the lazy dog.'.strip()
print(sentence.find("jumps"))
print(sentence[20:25])
print(sentence[sentence.find("lazy"): len("lazy")+sentence.find("lazy")])
print(len(first_name))
print("Welcome to my program", full_name + "!")

# Sanitazation and Stupid Proofing

# Debugging is fixing code!
    #Syntax Error
error = "This is a bug"
    #Logic Error
numOne = 1
numTwo = 2
print(numOne+numTwo)
    #Run-Time Error
num = 3
print("My favorite number is", num)