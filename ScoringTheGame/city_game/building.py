import pygame

class Building(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        super(Building, self).__init__()

        self.width = width
        self.height = height
        self.image = image
        self.x = 700
        self.y = 500-height

    def move(self, delta=0.5):
        self.x -= delta

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])