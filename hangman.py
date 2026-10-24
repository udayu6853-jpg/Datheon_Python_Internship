
import random


def load_words():
    """Load English words from words.txt."""
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
                and 4 <= len(word.strip()) <= 12
            ]

        if not words:
            raise ValueError("No suitable words found.")

        print("English word list loaded successfully!")
        return words

    except (FileNotFoundError, ValueError):
        print("Word list unavailable. Using default words.")
        return [
            "python",
            "computer",
            "program",
            "developer",
            "keyboard"
        ]


# ASCII gallows stages: stage 0 to stage 6
gallows = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]


def play_hangman(words):
    """Run one round of the Hangman game."""
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses available.")

    while wrong_guesses < max_attempts:
        # Display the current gallows stage
        print(gallows[wrong_guesses])

        # Display guessed and hidden letters
        masked_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", masked_word)

        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))
        else:
            print("Guessed letters: None")

        print("Attempts remaining:", max_attempts - wrong_guesses)

        # Get input from the player
        guess = input("Enter one letter: ").lower().strip()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        # Prevent duplicate guesses from receiving a penalty
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        # Check whether the guessed letter is in the word
        if guess in secret_word:
            print("Correct guess!")

            # Check whether all letters have been guessed
            if all(letter in guessed_letters for letter in secret_word):
                print("\n" + "=" * 35)
                print("Congratulations! You won!")
                print("The word was:", secret_word)
                print("=" * 35)
                return
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    # Display the final gallows and defeat message
    print(gallows[max_attempts])
    print("\n" + "=" * 35)
    print("Game over! You lost.")
    print("The correct word was:", secret_word)
    print("=" * 35)


def main():
    """Load words and start the game."""
    words = load_words()
    print("A random word will be selected for the game.")

    while True:
        play_hangman(words)

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).lower().strip()

        if play_again not in ("yes", "y"):
            print("Thank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()
