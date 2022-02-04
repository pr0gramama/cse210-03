from game.words_service import Words
class Sketcher:
    """The person drawing the parachute and hyphens acording to the coincidence in the word. 
    
    Attributes:
        letter (string): The letter entered (a-z).
    """
    def __init__(self):
        """Constructs a new Sketcher.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._word = Words()
        self.word_guess = []
        self.parachute = ["    ___   ",
                          "   /___\  ",
                          "   \   /  ",
                          "    \ /   ",
                          "     O    ",
                          "    /|\   ",
                          "    / \   ",
                          "          ",
                          "^^^^^^^^^^",
        ]

    def set_hyphens(self,word):
        """Draws the hyphens of the current word.
        Returns:
            string: The current word,
        """
        word = self._word.get_word()
        print()
        #print(word)
        for i in range(len(word)):
            self.word_guess.append("_")
            print(self.word_guess[i], end=" ")
        print()

    def set_parachute(self,guess):
        """Draw the parachute every time
        """
        for i in range(len(self.parachute)):
            print(self.parachute[i])
        
    def is_clean(self):
        """ True when the parachute is all clean
        """
        pass