import pygame


class Ship:

    def __init__(self, screen, board_settings):
        """initialize the ship to starting position on screen"""
        self.screen = screen
        self.board_settings = board_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # aligns ship to start in the bottom-center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # movements
        self.moving_right = False
        self.moving_left = False

    def update_pos(self):
        """updates the ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.board_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.board_settings.ship_speed_factor

        self.rect.centerx = self.center

    def place_ship(self):
        self.screen.blit(self.image,self.rect)