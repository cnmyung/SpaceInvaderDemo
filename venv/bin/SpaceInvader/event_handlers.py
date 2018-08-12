import sys
import pygame


def check_keydown_events(event, ship):
    """handles event - key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """handles event - key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Mouse and Key event handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(board_settings, screen, ship):
    """Acts as the animator, moves ship"""
    screen.fill(board_settings.bg_color)
    ship.place_ship()
    pygame.display.flip()
