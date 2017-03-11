import pygame
from scene import Scene
from score_keeper import ScoreKeeper
from sound_player import SoundPlayer


class Game():
    def setup(self):
        self.score_keeper = ScoreKeeper()
        self.sound_player = SoundPlayer()
        self.scene = Scene(700, 500, screen, self.score_keeper, self.sound_player)

    def run(self):
        # Loop until the user clicks the close button.
        done = False
        self.sound_player.play_theme_song()

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.scene.person.jump(self.score_keeper.velocity)
                        self.sound_player.play_jumping_sound()
                    #elif event.type == pygame.K_RIGHT:
                        #print "got up event"
                        #self.scene.person.jump()
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    #click_sound.play()

            # --- Game logic should go here

            # --- Screen-clearing code goes here

            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.

            # If you want a background image, replace this clear with blit'ing the
            # background image.
            if self.score_keeper.get_level() == 1 :
                screen.blit(background_image, [0, 0])
            elif self.score_keeper.get_level() == 2:
                screen.blit(level_2_background, [0, 0])
            elif self.score_keeper.get_level() == 3:
                screen.blit(level_3_background, [0, 0])
            elif self.score_keeper.get_level() == 4:
                screen.blit(level_4_background, [0, 0])
            elif self.score_keeper.get_level() == 5:
                screen.blit(level_5_background, [0, 0])
            else:
                screen.blit(level_5_background, [0, 0])


            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            mouse_position = pygame.mouse.get_pos()
            x = mouse_position[0]
            y = mouse_position[1]

            # Copy image to screen:
            #screen.blit(player_image, [x, y])
            self.scene.next_tick()

            # --- Drawing code should go here

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Close the window and quit.
        pygame.quit()




pygame.display.set_caption("My Game")

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#load images
background_image = pygame.image.load('images/city_scape_bgd.png').convert()
level_2_background = pygame.image.load('images/level_2_bgd.png').convert()
level_3_background = pygame.image.load('images/level_3_bgd.png').convert()
level_3_background = pygame.image.load('images/level_3_bgd.png').convert()
level_4_background = pygame.image.load('images/level_4_bgd.png').convert()
level_5_background = pygame.image.load('images/level_5_bgd.png').convert()
level_6_background = pygame.image.load('images/level_6_bgd.png').convert()
