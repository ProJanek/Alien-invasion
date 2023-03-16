import pygame.font
from pygame.sprite import Group
from ship import Ship
from life import Life

class Scoreboard:
    """A class to report scoring information.""" 

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font setiings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 28)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_life()

    def prep_score(self):
        """Turn the score into rendered image."""
        rounded_score = round(self.stats.score, - 1)
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20 
        
    def prep_high_score(self):
        """Turn the high score into rendered image."""
        high_score = round(self.stats.high_score, - 1)
        high_score_str = "High score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Display the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Display the level at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_life(self):
        """Show how many lives are left."""

        self.lives = Group()
        for life_number in range(self.stats.lives_left + 1):
            life = Life(self)
            life.rect.x = 10 + 1.2*life_number*life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def check_high_score(self):
        """Check to see if there  is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score, high score, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.lives.draw(self.screen)