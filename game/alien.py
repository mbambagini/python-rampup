import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """An instance of this class is an alien in the screen"""

    def __init__(self, screen, settings, level, init_x, init_y, offset_x):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.center_x = float(init_x)
        self.rect.centerx = self.center_x
        self.y = float(init_y)
        self.rect.y = self.y
        self.x_speed = settings.alien_initial_speed_x * level
        dist = offset_x - self.rect.width / 2
        self.max_x = self.center_x + dist
        self.min_x = self.center_x - dist
        self.y_speed = settings.alien_initial_speed_y * level

    def update(self):
        self.center_x += self.x_speed
        if self.center_x > self.max_x:
            self.center_x = self.max_x
            self.x_speed = -self.x_speed
        if self.center_x < self.min_x:
            self.center_x = self.min_x
            self.x_speed = -self.x_speed
        self.rect.centerx = self.center_x

        self.y += self.y_speed
        self.rect.y = self.y

    def reachBottom(self):
         if self.rect.bottom >= self.screen.get_rect().bottom:
             return True
         return False

    def draw(self):
        self.screen.blit(self.image, self.rect)

