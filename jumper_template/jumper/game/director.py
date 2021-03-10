from game.console import Console
from game.jumper import Jumper
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
        self.jumper = Jumper()
        self.keep_playing = True
        self.puzzle = Puzzle()
        self.wrong_guess = 0
        self.masked_word = []
        self.outcome = None
        self.last_guess = None
        
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

        self.last_guess = self.jumper.make_guess()
        self.puzzle.record_guess(self.last_guess)
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
       
        self.masked_word = self.puzzle.mask_word()
        print(self.wrong_guess)
        if self.puzzle.in_word(self.last_guess) == False:
            self.wrong_guess += 1
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        self.jumper.midgame_avatar(self.wrong_guess)
        self.console.write(self.masked_word)

        self.keep_playing = (self.puzzle.outcome(self.wrong_guess, self.masked_word) == None)
        if self.keep_playing == False:
            self.jumper.endgame_avatar(self.puzzle.outcome(self.wrong_guess, self.masked_word))
        self.masked_word.clear()

