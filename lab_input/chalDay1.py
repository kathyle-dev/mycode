#!/user/bin/env python3

print("Hello, " + input("Please enter your name: ")+"!", " Happy " +  input("What day of the week is it? ") + "!")

# using .format

print("Hello, {}! Happy {}!".format(input("What's your name? "), input("What day is it? ")))

# using f string
name = input("What's your name? ")
day = input("What day is it? ")
print(f"Hello, {name}! Happy {day}!")

