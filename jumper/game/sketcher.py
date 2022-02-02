import random
from game.words_service import Words
class Sketcher:
    """The person looking for the coincidence in the word. 
    
    The responsibility of a Seeker is to search for coincidences between the input for the player and the letters in the word to guess.
    
    Attributes:
        letter (string): The letter entered (a-z).
    """
    def __init__(self):
        """Constructs a new Sketcher.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._word = Words()

    def set_hyphens(self,woed,guess):
        """Draws the hyphens of the current word.
        Returns:
            string: The current word,
        """
        word = self._word.get_word()
        print(word)

    def set_paratrooper(self,guess):
        pass
        
    def is_clean(self):
        pass