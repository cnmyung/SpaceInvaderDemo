import sys
import pygame

from ammo import Ammo


def update_ammo(ammo):
    """updates the position of bullets"""
    ammo.update()


def check_keydown_events(event, board_settings, screen, ship, ammo):
    """handles event - key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(ammo) < board_settings.bullets_onscreen_limit:
            new_ammo = Ammo(board_settings, screen, ship)
            ammo.add(new_ammo)


def check_keyup_events(event, ship):
    """handles event - key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(board_settings, screen, ship, ammo):
    """Mouse and Key event handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # check_keydown_events(event,ship)
            check_keydown_events(event, board_settings,screen,ship,ammo)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(board_settings, screen, ship, ammo):
    """Acts as the animator, moves ship"""
    screen.fill(board_settings.bg_color)
    for bullet in ammo.sprites():
        bullet.draw_ammo()

    ship.place_ship()
    pygame.display.flip()
