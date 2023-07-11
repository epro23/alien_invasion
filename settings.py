class Settings:
    """A class to store settings for Alien Invasion."""

    def __init__(self):
        """Initialize static game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_limit = 2
        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.4

        # how quickly alien point value increases
        self.score_scale = 2

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout game."""
        self.ship_speed = 3
        self.bullet_speed = 10
        self.alien_speed = 1.0

        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # scoring settings
        self.alien_points = 10
    
    def increase_speed(self):
        """Increase speed settings and points earned."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)



