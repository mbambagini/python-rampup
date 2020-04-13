import pygame.font

class Button(object):
    """Generic button object"""

    def __init__(self, screen, width, height, background, text_color, size, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.color = background
        self.font = pygame.font.SysFont(None, size)
        # create rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # create message
        self.msg_image = self.font.render(msg, True, text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class PlayButton(Button):
    def __init__(self, screen, settings):
        super(PlayButton, self).__init__(screen, \
                                         settings.play_button_width, \
                                         settings.play_button_height, \
                                         settings.button_background, \
                                         settings.button_text_color, \
                                         settings.button_font_size, \
                                         "Play")

class PauseButton(Button):
    def __init__(self, screen, settings):
        super(PauseButton, self).__init__(screen, \
                                          settings.pause_button_width, \
                                          settings.pause_button_height, \
                                          settings.button_background, \
                                          settings.button_text_color, \
                                          settings.button_font_size, \
                                          "Game paused")
