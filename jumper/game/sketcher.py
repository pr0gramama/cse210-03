from game.terminal_service import TerminalService
# from game.matcher import Matcher


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
        self.guess = ""

    def make_guess(self):
        try:
            self._word = [] 
            self._unknown_word = []
            self._lives = 5
            self.match = False
            # Here is the input which is called in Director in get_inputs
            self.guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
            if self.guess.isalpha():
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
            else:
                self.guess.isalpha() != self._word
                self.guess == False
                self._terminal_service.write_text("\nInvalid input! Enter a letter")
            return self.guess.lower()
        except TypeError as err:
            self._terminal_service.write_text(err)

        

    def set_parachute(self, number):
        """Draw the parachute every time
        """
        print()
        for i in range(number):
            self.parachute[i] = ""
        if number == 5:
            self.parachute[i] = "     x      "

        for i in range (len(self.parachute)):
            print(self.parachute[i])

    def get_text(self, won):
        """Prints the output for the end game, either "won" or "lost" """
        if won == True:
            end_game = "You win!"
        else:
            end_game = "You lose"
        self._terminal_service.write_text(end_game)