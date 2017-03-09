import pygame

width = 30
height = 30

WHITE = (255, 255, 255)

class Person():
    def __init__(self, max_y):
        self.x = 100
        self.y = 60
        self.image = pygame.image.load("images/dude.png").convert()
        self.image.set_colorkey(WHITE)
        self.velocity = 0
        self.acceleration = 0.2
        self.max_y = max_y
        #self.scene = Scene(700, 500, screen)

    def left(self):
        return self.x

    def right(self):
        return self.x + width

    def top(self):
        return self.y

    def bottom(self):
        return self.y + height

    def move(self, delta = 0.5):
        self.x += delta

    def jump(self):
        self.velocity = -5

    def freeze(self):
        self.velocity = 0
        self.acceleration = 0

    def unfreeze(self):
        self.acceleration = 0.1

    def update_position(self):
        new_y = self.acceleration + self.velocity + self.y
        new_velocity = self.acceleration + self.velocity
        if new_y < self.max_y - height:
            self.y = new_y
            self.velocity = new_velocity
        else:
            self.y = self.max_y-height
            self.velocity = 0


    def update_max_y(self, new_max_y):
        self.max_y = new_max_y

    def trip(self):
        self.velocity = 0

    def regenerate(self):
        self.x = 100
        self.y = 60



    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

