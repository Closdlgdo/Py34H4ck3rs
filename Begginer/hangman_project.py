import random

print("""Welcome to Hangman!""")

wordList = ["hacker", "python", "computer", "science", "random"]
# create an empty list
# for each letter in the chosenWord add a "_" that will be printed to the console
# example: if the word is hacker: ["_","_","_","_","_","_"]

chosenWord = random.choice(wordList)
emptyList = []

for letter in chosenWord:
    emptyList.append("_")

print(emptyList)

guess = input("Guess a letter: ").lower()
# Loop through each of the letters in the chosen word
# if the letter is in the word, replace the "_" with the letter
# Example: if the chosen word is hacker, and the user guessed "h", the list will be ["h","_","_","_","_","_"]

for position in range(len(chosenWord)):
    letter = chosenWord[position]
    if letter == guess:
        emptyList[position] = letter
print(emptyList)