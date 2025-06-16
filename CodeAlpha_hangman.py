import random

word_list = ["apple", "grape", "mango", "peach", "lemon"]

chosen_word = random.choice(word_list)
guessed_word = ["_"] * len(chosen_word)
guessed_letters = []
attempts_left = 6

print("  Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts_left > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(" You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(" Good guess!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong guess.")
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    print()


if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("You're out of attempts. The word was:", chosen_word)
