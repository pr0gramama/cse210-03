from game.terminal_service import TerminalService

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
        self._terminal_service = TerminalService()
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

    def make_guess(self):
        # Here is the input which is called in Director in get_inputs
        guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        return guess.lower()

    def set_parachute(self, number): 
        """Draw the parachute every time
        """
        for i in range(len(self.parachute)):
            print(self.parachute[i])

    def get_text(self, won):
        """Prints the output for the endgame, either "won" or "lost" """
        
        if won == True:
                end_game = "  \\0/ \n   | \n__/_\__ \nYou win!"
        else:
            end_game = "   \ /\n___\|/___\n    x\nYou lose"
        self._terminal_service.write_text(end_game)

    
    def is_clean(self):  
        #This is not working.  Needs to clear the parachute line by line if
        #is_found doesn't return True.
        """ True when the parachute is all clean
        """
        pass