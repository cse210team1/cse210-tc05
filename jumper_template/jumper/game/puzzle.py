import random

class Puzzle:


    def __init__(self):

        self.word = random.choice(["fish", "beans", "dog", "cat"])
        self.guesses = []
        self.masked_word = []


    def record_guess(self, guess):

        self.guesses.append(guess)

    def mask_word(self):
        # loop through the word, if the guess is in the word print that letter otherwise set it to a dash
        self.masked_word.clear

        for letter in self.word:
            if letter in self.guesses:
                self.masked_word.append(letter)
            else:
                self.masked_word.append(-)
        return self.masked_word

    def is_solved(self):

        if self.masked_word == self.word:
            return True 
        else:
            return False

    def in_word(self, guess):

        if guess in self.guesses:
            return True
        else:
            return False