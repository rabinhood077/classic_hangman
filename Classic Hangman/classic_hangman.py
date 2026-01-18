import random

# Hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """
]

# Word list
words = ["python", "django", "computer", "developer", "programming"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("🎯 Welcome to Hangman Game!")

while wrong_guesses < max_attempts:
    print(hangman_stages[wrong_guesses])

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)
    print("Guessed letters:", guessed_letters)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You won!")
        print("The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ Letter already guessed.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print(hangman_stages[wrong_guesses])
    print("\n💀 Game Over!")
    print("The word was:", word)
