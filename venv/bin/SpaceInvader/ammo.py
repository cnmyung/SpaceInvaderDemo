import pygame
from pygame.sprite import Sprite


class Ammo(Sprite):
    """Ammunition used by spaceship"""

    def __init__(self, board_settings, screen, ship):
        """constructor for ammo  super class"""
        super(Ammo,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,board_settings.bullet_size,
                                board_settings.bullet_length)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # positional info of ammo
        self.y = float(self.rect.y)
        self.color = board_settings.bullet_color
        self.speed_factor = board_settings.bullet_speed_factor

    def update(self):
        """updates the position of the shots fired by ship up screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_ammo(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
