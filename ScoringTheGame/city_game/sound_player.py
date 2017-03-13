import pygame

class SoundPlayer():
    def __init__(self):
        self.theme_song = pygame.mixer.Sound("sounds/theme.ogg")
        self.jumping_sound = pygame.mixer.Sound("sounds/jump.ogg")
        self.running_sound = pygame.mixer.Sound("sounds/running.ogg")
        self.falling_sound = pygame.mixer.Sound("sounds/falling.ogg")


    def play_theme_song(self):
        self.theme_song.play()


    def play_jumping_sound(self):
        self.jumping_sound.play()


    def play_running_sound(self):
        self.running_sound.play()


    def play_falling_sound(self):
        self.falling_sound.play()

