import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet shot from the ship"""

    def __init__(self, screen, settings, init_x, init_y):
        super(Bullet, self).__init__()

        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = init_x
        self.rect.centery = init_y

        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

