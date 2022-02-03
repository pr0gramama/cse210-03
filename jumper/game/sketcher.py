from game.words_service import Words
class Sketcher:
    """The person drawing the parachute and hyphens with the coincidence in the word. 
    
    Attributes:
        letter (string): The letter entered (a-z).
    """
    def __init__(self):
        """Constructs a new Sketcher.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._word = Words()

    def set_hyphens(self,word):
        """Draws the hyphens of the current word.
        Returns:
            string: The current word,
        """
        word = self._word.get_word()
        print()
        print(word)
        for i in word:
            print("_", end=" ")
        print()

    def set_parachute(self,guess):
        """Draw the parachute every time
        """
        print()
        print ("    ___   ")
        print ("   /___\  ")
        print ("   \   /  ")
        print ("    \ /   ")
        print ("     O    ")
        print ("    /|\   ")
        print ("    / \   ")
        print ()
        print (" ^^^^^^^^")
        
    def is_clean(self): 
        pass