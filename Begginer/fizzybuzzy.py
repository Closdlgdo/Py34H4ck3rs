# FizzBuzz
# If a number is divisible by 3, print "Fizz".
# If a number is divisible by 5, print "Buzz".
# If a number is divisible by both 3 and 5, print "FizzBuzz".\
# Functions do not need to be in order when the print shows. The important part is
# when the function is called.
import time
choice = int(input("Enter a number: "))


def my_function():
    for i in range(1, choice, 3):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print("Program starting...")
time.sleep(3)
my_function()