import os
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_GEMS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("Score: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - 50)
    position = Point(x, y)


    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    
    # create the gems

    for n in range(DEFAULT_GEMS):

        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS -10)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        dx = 0#variable for velocity
        dy = 1
        velocity = Point(dx, dy)#setting velocity
        
        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_velocity(velocity)
        cast.add_actor("gems", gem)
    
        
        
        

    # create the stones

    for n in range(DEFAULT_GEMS):

        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS -10)
        dx = 0#variable for velocity
        dy = 1
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        velocity = Point(dx, dy)#setting velocity
        
        

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        stone = Gem()
        stone.set_text("o")
        stone.set_font_size(FONT_SIZE)
        stone.set_color(color)
        stone.set_position(position)
        stone.set_velocity(velocity)
        cast.add_actor("stones", stone)
        
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()