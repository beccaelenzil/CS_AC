import pygame
import random

from building import Building
from person import Person

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Scene():
    def __init__(self, width, height, screen):
        self.buildings = []
        self.width = width
        self.height = height
        self.screen = screen
        x = width
        while x > 100:
            building = self.create_building()
            building.move(x)
            building.draw(screen)
            x -= random.randint(building.width+10, building.width+50)

    def next_tick(self):
        for building in self.buildings:
            building.move()
            if self.building_is_off_screen(building):
                self.remove_building(building)
            else:
                building.draw(screen)
        if self.can_new_building_be_created():
            self.create_building()


    #building directions

    def can_new_building_be_created(self):
        most_recent_building = self.buildings[-1]
        if self.building_is_on_screen(most_recent_building):
            return True
        else:
            return False

    def create_building(self):
        num_buildings = len(building_props)
        building_props_index = random.randint(0, num_buildings - 1)
        props = building_props[building_props_index]
        building = Building(props['width'] + random.randint(25,75), props['height'], props['image'])
        self.buildings.append(building)
        return building

    def remove_building(self, building):
        self.buildings.remove(building)

    def building_is_on_screen(self, building):
        if building.x<700 - building.width:
            return True
        else:
            return False

    def building_is_off_screen(self, building):
        if building.x< 0 - self.width:
            return True
        else:
            return False

    #person directions

    def create_person(self):
        props = building_props[0]
        person = Person(0, props['height'], props['image'])
        return person



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

building_props = [
    { 'width': 50, 'height': 100, 'image': pygame.image.load("images/50x100.png").convert() },
    { 'width': 125, 'height': 100, 'image': pygame.image.load("images/125x150.png").convert() },
    { 'width': 100, 'height': 175, 'image': pygame.image.load("images/100x175.png").convert() },
    { 'width': 75, 'height': 150, 'image': pygame.image.load("images/75x150.png").convert() },
    { 'width': 75, 'height': 225, 'image': pygame.image.load("images/75x225.png").convert() },
    { 'width': 100, 'height': 250, 'image': pygame.image.load("images/100x250.png").convert() },

]

person_props = [
    {'width': 30, 'height':30, 'image':pygame.image.load("images/dude.png").convert() }
]

game = Game()
game.setup(screen)
game.run()


