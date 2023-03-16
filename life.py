import pygame
from pygame.sprite import Sprite

class Life(Sprite):
    """A class to manage lives."""

    def __init__(self, ai_game):
        """Initialize the lives and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/heart.bmp")
        self.rect = self.image.get_rect()
