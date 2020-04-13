
class Settings(object):
    """Main settings of the game"""

    def __init__(self):
        # window settings
        self.window_x_size = 800
        self.window_y_size = 600
        self.window_background = (230, 230, 230)
        self.window_title = "Alien Invasion"
        # score settings
        self.score_text_color = (30, 30, 30)
        self.score_background = (230, 230, 230)
        self.score_font_size = 30
        # play button settings
        self.play_button_width = 200
        self.play_button_height = 50
        # pause button settings
        self.pause_button_width = 300
        self.pause_button_height = 70
        # generic button settings
        self.button_background = (0, 0, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font_size = 48
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 2.0
        # fleet settings
        self.fleet_num_rows = 6
        self.fleet_num_cols = 10
        # alien settings
        self.alien_initial_speed_x = 0.1
        self.alien_initial_speed_y = 0.01
        # ship settings
        self.ship_speed = 1.0
        # score system settings
        self.score_per_alien = 10
        self.score_per_level = 2000

    def getWindowSize(self):
        return (self.window_x_size, self.window_y_size)

    def getWindowTitle(self):
        return self.window_title

    def getBackgroundColor(self):
        return self.window_background

