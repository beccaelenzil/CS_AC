import pygame
from game import Game

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()


person_props = [
    {'width': 30, 'height':30, 'image':pygame.image.load("images/dude.png").convert() }
]

game = Game()
game.setup()
game.run()


