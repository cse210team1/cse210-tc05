from game.console import Console
from game.jumper import jumper
from game.puzzle import Puzzle

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = jumper()
        self.keep_playing = True
        self.puzzle = Puzzle()
        self.wrong_guess = 0
        self.masked_word = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """

        record_guess = self.console.read_number("Guess a letter [a-z]: ")
        self.puzzle.record_guess(record_guess)
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
       
        self.masked_word = self.puzzle.mask_word
        if self.puzzle.in_word() == False:
            self.wrong_guess =+ 1
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        parachute_1 = self.jumper.midgame_avatar()
        self.console.write(parachute_1)
        self.console.write(self.masked_word)
        self.keep_playing = (self.jumper.distance[-1] != 0)


