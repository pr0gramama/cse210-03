import random
class Words:
    """The person looking for the coincidence in the word. 
    
    The responsibility of a Seeker is to search for coincidences between the input for the player and the letters in the word to guess.
    
    Attributes:
        word (string): A word of the list.
    """
    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        list_words = ['battery', 'correct', 'horse', 'staple']
        self._word = random.choice(list_words)

    def get_word(self):
        """Gets the current word of the lsit.
        
        Returns:
            string: The current word,
        """
        return self._word
        