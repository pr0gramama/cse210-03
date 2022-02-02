
class Matcher:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._list = [] # start with 
    
    def get_match(self, list):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        pass
        

    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return True

    def get_text(self):
        pass
        