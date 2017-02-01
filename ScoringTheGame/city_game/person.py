import pygame

class Person():
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = image
        self.x = 0
        self.y = 500

    def move(self, delta = 0.5):
        self.x += delta

    def jump(self):
       if self.event.type == pygame.K_SPACE or self.event.type == pygame.K_UP:
           self.y += 0.1

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])


