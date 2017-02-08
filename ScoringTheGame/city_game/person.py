import pygame

width = 30
height = 30

class Person():
    def __init__(self):
        self.x = 100
        self.y = 60
        self.image = pygame.image.load("images/dude.png").convert()

    def move(self, delta = 0.5):
        self.x += delta

    def jump_up(self):
        self.y -= 0.5

    def jump_down(self):
        self.y += 0.5

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])
