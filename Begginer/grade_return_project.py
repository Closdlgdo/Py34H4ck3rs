# Write a program that prompts the user to enter their score (out of 100)
# and outputs their letter grade.

score = int(input("Enter your score (out of 100):"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")