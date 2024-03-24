import random

print("""Welcome to Hangman!""")

wordList = ["hacker", "python", "computer", "science", "random"]
# create an empty list
# for each letter in the chosenWord add a "_" that will be printed to the console
# example: if the word is hacker: ["_","_","_","_","_","_"]
emptyList = []

chosenWord = random.choice(wordList)

guess = input("Guess a letter: ").lower()


for letter in chosenWord:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")
