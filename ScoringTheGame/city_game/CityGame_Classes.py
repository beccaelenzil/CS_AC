import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Blding(pygame.sprite.Sprite):
    def __init__(self):

        super()__init__()

        self.height = 0
        self.width = 0
        self.image = ""
        self.number = 0
        self.x = -self.width
        self.y = 500-self.height

    def move(self):
        for i in self.x<700:
            self.x += 0.1

    def randBlding(self):

blding1 = Blding()
blding1.height = 100
blding1.width = 50
blding1.image = pygame.image.load("images/100x50.png").convert()
blding1.number = 1


blding2 = Blding()
blding2.height = 125
blding2.width = 150
blding2.image = pygame.image.load("images/100x50.png").convert()
blding2.number = 2

blding3 = Blding()
blding3.height = 225
blding3.width = 75
blding3.image = pygame.image.load("images/225x75.png").convert()
blding3.number = 3

aBlding = Blding()
aBlding.number = random.randint(0,3)

blding_list = [blding1, blding2, blding3]
blding = random.choice(blding_list)
print blding
#load images
background_image = pygame.image.load('images/city_scape_bgd.png').convert()


xPos = -aBlding.width
yPos = aBlding.height

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #click_sound.play()

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0, 0])

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    #screen.blit(player_image, [x, y])
    screen.blit(aBlding.image, [xPos, yPos])

    # --- Drawing code should go here
    # Process each snow flake in the list
    aBlding.move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()


