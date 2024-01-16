import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

    def choose_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # You can continue with the logic in the next task

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the code
hangman_game = Hangman(["Pineapple", "Mango", "orange", "grapes", "strawberry"])

# You can call ask_for_input multiple times to test different guesses
hangman_game.ask_for_input()
