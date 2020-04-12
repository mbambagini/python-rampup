import pygame.font

class Button(object):

    def __init__(self, screen, settings, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = settings.button_width
        self.height = settings.button_height
        self.color = settings.button_background
        self.text_color = settings.button_text_color
        self.font = pygame.font.SysFont(None, settings.button_font_size)
        # create rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # create message
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

