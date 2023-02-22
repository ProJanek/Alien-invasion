class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        #self.screen_width = 1200
        #self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Rocket settings
        self.ship_speed = 10
        self.ship_left = 2

        # Bullet settings
        self.bullet_speed = 12.0
        self. bullet_width = 10
        self.bullet_height = 10
        self.bullet_color =(60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings 
        self.alien_speed = 1.0
        self.alien_speed_drop = 100
        # flee_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1