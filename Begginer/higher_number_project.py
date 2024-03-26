# We will create a small.txt project that will receive two input ints, then it will output the
# highest of those two numbers.

print("Enter the first number")
first_number = int(input())

print("Enter the second number")
second_number = int(input())

print(f"The highest number is {max(first_number, second_number)}")