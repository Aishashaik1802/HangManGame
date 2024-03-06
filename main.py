import random

def select_random_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "lemon", "melon", "pear", "peach"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters) and incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess. You have {} attempts left.".format(max_attempts - incorrect_guesses))

        print(display_word(word, guessed_letters))

    if "_" not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word: {}".format(word))
    else:
        print("Sorry, you've run out of attempts. The word was: {}".format(word))

hangman()