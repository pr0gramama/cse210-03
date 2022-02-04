import random
class Words:
    """ 
    Person who obtain a random word of the list
    
    Attributes:
        word (string): A word of the list.
    """
    def __init__(self):
        """Constructs a new Words.

        Args:
            self (Words): An instance of Seeker.
        """
        list_words = ['battery', 'correct', 'horse', 'staple'] # to add more words
        self._word = random.choice(list_words)

    def get_word(self):
        """Gets the current word of the lsit.
        
        Returns:
            string: The current word,
        """
        return self._word
        