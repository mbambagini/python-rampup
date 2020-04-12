import pygame
from pygame.sprite import Sprite

class Life(Sprite):
    """This class represent a life in the score area"""

    def __init__(self, screen, index):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/life.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width * index + 5
        self.rect.y = 10

    def draw(self):
        self.screen.blit(self.image, self.rect)

