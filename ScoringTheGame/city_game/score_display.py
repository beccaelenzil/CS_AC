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
            self.draw_game_over(font)
            self.draw_level(font)
            self.draw_loose_life(font)
            self.draw_level_up(font)

    def draw_score(self, font):
        score = self.score_keeper.get_score()
        score_text = "score: {0}".format(str(score))
        label = font.render(score_text, 1, (204,204,0))
        self.screen.blit(label, (550, 30))

    def draw_lives(self, font):
        lives = self.score_keeper.get_remaining_lives()
        lives_text = "lives: {0}".format(str(lives))
        label = font.render(lives_text, 1, (0,255,255))
        self.screen.blit(label, (550, 50))

    def draw_level(self, font):
        level = self.score_keeper.get_level()
        level_text = "level: {0}".format(str(level))
        label = font.render(level_text, 1, (204,204,0))
        self.screen.blit(label, (550, 70))

    def draw_loose_life(self, font):
        if self.score_keeper.is_person_alive() == False and self.score_keeper.get_remaining_lives() > 0 :
            font = pygame.font.Font(None, 100)
            lives = self.score_keeper.get_remaining_lives()
            game_over_text = "lives remaing: {0}".format(str(lives))
            label = font.render(game_over_text, 1, (255,0,0))
            self.screen.blit(label, (80, 200))

    def draw_level_up(self, font):
        if self.score_keeper.level_up == True and self.score_keeper.is_person_alive()== True and self.score_keeper.game_over() == False and self.score_keeper.level != 1 :
            font = pygame.font.Font(None, 100)
            level = self.score_keeper.get_level()
            game_over_text = "Level Up!"
            label = font.render(game_over_text, 1, (255,0,0))
            self.screen.blit(label, (170, 200))


    def draw_game_over(self, font):
        if self.score_keeper.game_over():
            font = pygame.font.Font(None, 100)
            game_over_text = "GAME OVER"
            label = font.render(game_over_text, 1, (255,0,0))
            self.screen.blit(label, (120, 200))

