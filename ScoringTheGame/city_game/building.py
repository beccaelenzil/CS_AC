import pygame
import random

class Building(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        super(Building, self).__init__()
        self.width = width
        print 'width', self.width
        self.height = height
        self.image = image
        self.x = 700
        self.y = 500-height


    def top(self):
        return 500 - self.height

    def bottom(self):
        return 500

    def move(self, delta=0.8):
        self.x -= delta

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def rand_width(self):
        return self.width + random.randint(50,100)

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width
