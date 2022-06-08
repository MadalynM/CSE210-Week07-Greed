from game.casting.actor import Actor

class Gem(Actor):
    
    """Responsibility: provide information of the score to be awarded


    Attributes:

    """

    def __init__(self):
        super().__init__()
        
        """Constructs a new Gem."""
    
        self.point = 0

    def add_point(self):
        self.point = 1

        return self.point
