# milestone_2.py
import random

# Task 1
# Step 1: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Pineapple", "Mango", "Orange", "Grapes", "Strawberry"]

# Step 2: Assign this list to a variable called word_list.
word_list = favorite_fruits

# Step 3: Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Task 2 - Use the random.choice method
word = random.choice(word_list)

print("Randomly generated word:", word)

# Task 3

guess = input("Enter a single letter: ")

# Task 4

if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
else:
        print("Oops! That is not a valid input.")