import pygame.font
from pygame.sprite import Group
from life import Life

class Scoreboard(object):
    """Manage the display of score, level and lives"""

    def __init__(self, screen, settings, status):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = settings.score_text_color
        self.color = settings.score_background
        self.font = pygame.font.SysFont(None, settings.score_font_size)
        self.lives = Group()
        self.update(status)

    def update(self, status):
        # score
        score_str = "{:,}".format(int(round(status.score, -1)))
        self.score_image = self.font.render(score_str, True, self.text_color, self.color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
        # best score
        best_score_str = "{:,}".format(int(round(status.best_score, -1)))
        self.best_score_image = self.font.render(best_score_str, True, self.text_color, self.color)
        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = 10
        # level
        level_str = "Level " + str(status.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = self.score_rect.bottom + 5
        # lives
        if len(self.lives) != status.lives:
            self.lives = Group()
            for i in range(status.lives):
                 life = Life(self.screen, i)
                 self.lives.add(life)

    def draw(self):
        # draw score board
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

