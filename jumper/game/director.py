from game.terminal_service import TerminalService
from game.words_service import Words
from game.sketcher import Sketcher
from game.matcher import Matcher


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
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
        self.letter = "" # no es privada
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
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        word = self._words.get_word() #get the word from the list at the beginning of the game
        self._sketcher.set_hyphens(word,self.guess) # dibuja los guiones de acuerdo a la cantindad de letras y al juego, debe guardar lista actualizada
        self._sketcher.set_paratrooper(self.guess) # dibuja el paracaidista de acuerdo al juego anterior, debe guardar matriz actualizada
        self.letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ") #pide una letra por pantalla y la guarda en atributo. Se usa get para obtenerlo
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = self._matcher.get_match(self.letter) # Busca si hay coincidencia y cambia la lista de palabras y la matriz del paracaidista
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        text = self._matcher.get_text() # obtiene el mensaje adecuado si gano o perdio
        self._terminal_service.write_text(text) # coloca el mensaje en pantalla
        if self._matcher.is_found():  #If the puzzle is solved the game is over.
            self._is_playing = False
        if self._sketcher.is_clean(): # If the paratropper is clean the game is over
            self._is_playing = False