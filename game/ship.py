import pygame

class Ship(object):
    """Main ship class"""

    def __init__(self, screen, settings):
        self.screen = screen
        # load the ship
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # place the ship at the bottom center of the screen
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center
        self.rect.bottom = self.screen_rect.bottom
        # pre-compute border limits
        self.right_border = self.screen_rect.right - self.rect.width/2
        self.left_border = self.screen_rect.left + self.rect.width/2
        # the ship is still
        self.move_factor = 0.0
        self.speed = settings.ship_speed

    def center_ship(self):
        # place the ship at the bottom center of the screen
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center
        self.rect.bottom = self.screen_rect.bottom
        self.move_factor = 0.0

    def update(self):
       self.center += self.move_factor
       if self.center > self.right_border:
          self.center = self.right_border
       if self.center < self.left_border:
          self.center = self.left_border
       self.rect.centerx = self.center

    def move_left(self):
       self.move_factor = -self.speed

    def move_right(self):
       self.move_factor = +self.speed

    def stop(self):
       self.move_factor = 0.0

    def getCannonX(self):
        return self.rect.centerx

    def getCannonY(self):
        return self.rect.centery

    def draw(self):
        # draw the ship
        self.screen.blit(self.image, self.rect)

