class Settings:
    """Class that holds settings for the game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        self.ship_speed_factor = 3.0

        # Weapon settings
        self.bullet_speed_factor = 6
        self.bullet_size = 3
        self.bullet_length = 15
        self.bullet_color = 160, 160, 160
        self.bullets_onscreen_limit = 10
