from game.console import Console

class Jumper():
    def __init__(self):
        self.console = Console()
        self.parachute = [" ___", "/___\ ", "\   /", " \ /"]

    def make_guess(self):
        guess = self.console.read("Guess a letter [a-z]: ")
        return guess.lower()

    def midgame_avatar(self, number):
        """Prints the avatar at various midgame stages
        
        Args:
            number (of wrong guesses so far)

        Returns:
            prints a string
        """
        parachute_left = ""
        for i in range(number, 4):
            parachute_left += self.parachute[i] + "\n"
        avatar = parachute_left +  "  0 \n /|\ \n / \ "
        self.console.write(avatar)

    def endgame_avatar(self, won):
        """Prints the avatar for one of two endgame states
        
        Args:
            won (boolean)

        Returns:
            prints a string
        """
        if won == True:
            avatar = "  \\0/ \n   | \n__/_\__ \nYou win!"
        else:
            avatar = "   \ /\n___\|/___\n    x\nYou lose"
        self.console.write(avatar)
