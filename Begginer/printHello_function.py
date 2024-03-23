# Create a program that can take an input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello, [name]"
import time


name = input("What is your name? ")


def my_function():
    print(f"Hello, {name}")


print("Program starting...")
time.sleep(1)

print("Almost there...")
time.sleep(3)

print("Still not there...")
time.sleep(5)

my_function()