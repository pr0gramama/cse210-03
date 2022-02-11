from pickle import FALSE
from game.terminal_service import TerminalService
from game.sketcher import Sketcher
from game.matcher import Matcher


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        matcher (Matcher): The game's skeeer matching letter in the word.
        is_playing (boolean): Whether or not to keep playing.
        sketcher (Seeker): The game's sketcher, parachute and word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._sketcher = Sketcher()
        self._matcher = Matcher()
        self._terminal_service = TerminalService()
        self._unknown_word = []  # container for unknown word chosen by random module -mary ann
        # supposed to add up wrong guesses.  Not working (Matcher: outcome)
        self._wrong_guess = 0
        self.last_guess = ""  # most recent letter guessed by user
        # SEE Matcher function outcome.  This may be a problem.
        self.outcome = None

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        print("\n the word has as many letters as the hyphens:")
        self._unknown_word = self._matcher.set_hyphens()
        self._sketcher.set_parachute(0)
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Draw the parachute, dashes and letters each time.

        Args:
            self (Director): An instance of Director.
        """
        self.last_guess = self._sketcher.make_guess()
        self._matcher.get_word(self.last_guess)

    def _do_updates(self):
        """Check matching and change the lists, word and parachute.

        Args:
            self (Director): An instance of Director.
        """
        self._unknown_word = self._matcher.set_hyphens()
        print()
        print(self._matcher._word) #it is only for control. Yuu can erase it
        self._matcher.is_found(self._sketcher.guess)
        if self._matcher.match:
            self._matcher.match = False
        else:
            self._wrong_guess += 1
        self._sketcher.set_parachute(self._wrong_guess)

    def _do_outputs(self):
        """Ask for input on the screen. Post the appropriate message if win or lose.

        Args:
            self (Director): An instance of Director.
        """
        self._is_playing = (self._matcher.outcome(
            self._wrong_guess, self._unknown_word) == None)
        if self._is_playing == False:
            self._sketcher.get_text(self._matcher.outcome(
                self._wrong_guess, self._unknown_word))
        self._unknown_word.clear()
