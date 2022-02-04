from game.terminal_service import TerminalService
from game.words_service import Words
from game.sketcher import Sketcher
from game.matcher import Matcher


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        matcher (Matcher): The game's skeeer matching letter in the word.
        is_playing (boolean): Whether or not to keep playing.
        words (Words): The word list handler
        sketcher (Seeker): The game's sketcher, parachute and word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._words = Words()
        self._sketcher = Sketcher()
        self._matcher = Matcher()
        self._terminal_service = TerminalService()
        self.letter = "" 
        self.guess = []
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Draw the parachute, dashes and letters each time.

        Args:
            self (Director): An instance of Director.
        """
        word = self._words.get_word() #get the word from the list at the beginning of the game
        self._sketcher.set_hyphens(word) # draws the dashes according to the number of letters, musts keep an updated list
        self._sketcher.set_parachute(self.guess) # draws the parachute according to the game, must save the updated matrix
        self.letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ") #asks for a letter on the screen and saves it in an attribute. A get function is used to get it
        
    def _do_updates(self):
        """Check matching and change the lists, word and parachute.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = self._matcher.get_match(self.letter)
        
    def _do_outputs(self):
        """Ask for input on the screen. Post the appropriate message if win or lose.

        Args:
            self (Director): An instance of Director.
        """
        text = self._matcher.get_text()
        self._terminal_service.write_text(text)
        if self._matcher.is_found():  #If the puzzle is solved the game is over.
            self._is_playing = False
        if self._sketcher.is_clean(): # If the parachute is clean the game is over
            self._is_playing = False