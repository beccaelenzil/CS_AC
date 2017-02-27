import pygame
from scene import Scene

width = 30
height = 30

WHITE = (255, 255, 255)

class Person():
    def __init__(self):
        self.x = 100
        self.y = 60
        self.image = pygame.image.load("images/dude.png").convert()
        self.image.set_colorkey(WHITE)
        self.velocity = 0
        self.acceleration = 0.1

    def left(self):
        return self.x

    def right(self):
        return self.x + width

    def move(self, delta = 0.5):
        self.x += delta

    def jump(self):
        self.velocity = -5

    def update_position(self):
        new_y = self.acceleration + self.velocity + self.y
        if new_y == self.scene.ground_height:
            new_velocity = 0
        else:
            new_velocity = self.acceleration + self.velocity
        self.y = new_y
        self.velocity = new_velocity


    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

