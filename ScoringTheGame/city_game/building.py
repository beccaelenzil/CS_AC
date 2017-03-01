import pygame

class Building(pygame.sprite.Sprite):
    def __init__(self, width, height, image):
        super(Building, self).__init__()

        self.width = width
        self.height = height
        self.image = image
        self.x = 700
        self.y = 500-height

    def top(self):
        return 500 - self.height

    def bottom(self):
        return 500

    def move(self, delta=0.5):
        self.x -= delta

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width
