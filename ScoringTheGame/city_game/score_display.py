import pygame
from score_keeper import ScoreKeeper

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class ScoreDisplay():
    def __init__(self, score_keeper, screen):
        self.score_keeper = score_keeper
        self.screen = screen

    def draw(self):
        if pygame.font:
            font = pygame.font.Font(None, 36)
            self.draw_score(font)
            self.draw_lives(font)

    def draw_score(self, font):
        score = self.score_keeper.get_score()
        score_text = "score: {0}".format(str(score))
        label = font.render(score_text, 1, (255,255,0))
        self.screen.blit(label, (200, 200))

    def draw_lives(self, font):
        lives = self.score_keeper.get_remaining_lives()
        lives_text = "lives: {0}".format(str(lives))
        label = font.render(lives_text, 1, (0,255,255))
        self.screen.blit(label, (100, 200))
