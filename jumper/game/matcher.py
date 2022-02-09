import random
from game.sketcher import Sketcher
class Matcher:
    """The user looking for the coincidence of the letter in the word. The responsibility
        of the matcher is to guess the correct word before the parachute (Sketcher) disappears.

    Attributes:

    """

    def __init__(self):
        """Constructs a new Matcher.

        Args:
            self (Matcher): An instance of Matcher.
        """
        list_words = random.choice(["dish", "chair", "cheese", "cat", "house",
                                    "car", "smell", "break", "seat", "ghost", "album", "apple", "baker",
                                    "beach", "bread", "close", "death", "dream", "error", "faith", "fruit",
                                    "green", "happy", "human", "label", "learn", "lunch", "magic", "money",
                                    "music", "night", "paint", "phone", "pride", "queen", "radio", "river",
                                    "sleep", "smoke", "space", "sugar", "table", "tired", "train", "virus",
                                    "woman", "world", "youth"])
        self._word = [] 
        for letter in list_words:
            self._word.append(letter)

        self.guesses = []
        self._unknown_word = []
        self.match = False
        self._sketcher = Sketcher

    def set_hyphens(self):
        """ Loops through the letters in the word.  If the guesses is found in the word
        print that letter, otherwise set it to an underscore."""
        self._unknown_word.clear

        for letter in self._word:
            if letter in self.guesses:
                self._unknown_word.append(letter)
            else:
                self._unknown_word.append("_")
        return self._unknown_word

    def get_word(self, guess):
        self.guesses.append(guess)

    def get_match(self):
        """If the guessed word is the random word, return True, otherwise the word is wrong.

        Args:
            self (Matcher): An instance of Matcher.

        Returns:
            string: 
        """
        if self._unknown_word == self._word:
            return True
        else:
            return False

    def is_found(self, guess):
        """If the guessed letter is found in the random word, return true, otherwise the 
        guess is wrong

        Args:
            self (Matcher): An instance of Matcher.

        Returns:
        boolean: True if the matcher was found; false if otherwise.

        """
        for letter in self._word:
            if letter == guess:
                self.match = True
        return self.match

    def outcome(self, wrong, _unknown_word):  # HELP! THIS IS NOT WORKING
        """Gives the player 4 chances to guess the letters."""
        if wrong >= 5:
            return False
        elif _unknown_word == self._word:
            return True
        else:
            return None
