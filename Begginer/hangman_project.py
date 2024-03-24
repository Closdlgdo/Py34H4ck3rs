import random
# Create a greeting
print("""Welcome to Hangman!""")
# create your own word list
wordList = ["hacker", "python", "computer", "science", "random"]
# randomly choose a word from the list you have created
chosenWord = random.choice(wordList)
# ask the user to guess a letter
guess = input("Guess a letter: ").lower()
# bonus make the program take the input from the user and make it lowercase
guess = guess.lower()
# Check if the letter is in the word
if guess in chosenWord:
    print("Correct!")
else:
    print("Wrong!")
