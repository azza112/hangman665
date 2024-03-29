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

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            if self.num_letters == 0:
                print("Congratulations! You guessed the word:", self.word)
                break  # Exit the loop when the word is completely guessed

        if self.num_lives == 0:
            print("Game over. You ran out of lives. The word was:", self.word)

# Testing the code
hangman_game = Hangman(["Pineapple", "Mango", "orange", "grapes", "strawberry"])

hangman_game.ask_for_input()
