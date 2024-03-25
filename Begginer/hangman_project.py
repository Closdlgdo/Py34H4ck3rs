import random

print("""Welcome to Hangman!""")

wordList = ["hacker", "python", "computer", "science", "random"]

chosenWord = random.choice(wordList)
emptyList = []

for letter in chosenWord:
    emptyList.append("_")

print(emptyList)

guess = input("Guess a letter: ").lower()

# 1 use a while loop so your game keeps going until the word has been guessed
while "_" in emptyList:

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            emptyList[position] = letter
    print(emptyList)

    if guess not in chosenWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        break

    guess = input("Guess a letter: ").lower()


if "_" not in emptyList:
    print("You win!")