import pygame

from scene import Scene

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game():
    def setup(self, screen):
        self.scene = Scene(700, 500, screen)
        self.scene.create_building()

    def run(self):
        # Loop until the user clicks the close button.
        done = False

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
            mouse_position = pygame.mouse.get_pos()
            x = mouse_position[0]
            y = mouse_position[1]

            # Copy image to screen:
            #screen.blit(player_image, [x, y])
            self.scene.next_tick()

            # --- Drawing code should go here
            # Process each snow flake in the list

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Close the window and quit.
        pygame.quit()


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#load images
background_image = pygame.image.load('images/city_scape_bgd.png').convert()

person_props = [
    {'width': 30, 'height':30, 'image':pygame.image.load("images/dude.png").convert() }
]

game = Game()
game.setup(screen)
game.run()


