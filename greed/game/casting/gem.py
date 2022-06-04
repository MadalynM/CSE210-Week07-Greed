from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast

class Gem(Actor):
    """Responsibility:


    Attributes:

    """

    def __init__(self):
        """Constructs a new Gem."""
        self._message = ""
        self.point = 0

    def set_message(self, message):
        self._message = message

        return message
    
    def get_message(self):
        return self._message

    def set_point(self):
        self.point = 1

        return self.point