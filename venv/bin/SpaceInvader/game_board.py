import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import event_handlers as e_handlers


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    board_settings = Settings()
    screen = pygame.display.set_mode((board_settings.screen_width,
                                      board_settings.screen_height))

    pygame.display.set_caption("Space Invaders")
    ship = Ship(screen, board_settings)
    # group that will hold ammo in use
    ammo = Group()

    # starts main for the game
    while True:
        e_handlers.check_events(board_settings,screen,ship,ammo)
        ship.update_pos()
        e_handlers.update_ammo(ammo)
        e_handlers.update_screen(board_settings,screen,ship,ammo)

        # remove bullets off the screen
        for bullet in ammo.copy():
            if bullet.rect.bottom <= 0:
                ammo.remove(bullet)


run_game()
