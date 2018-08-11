import pygame

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

    # starts main for the game
    while True:
        e_handlers.check_events(ship)
        ship.updatePos()
        e_handlers.update_screen(board_settings,screen,ship)

        screen.fill(board_settings.bg_color)
        ship.place_ship()

        pygame.display.flip()


run_game()
