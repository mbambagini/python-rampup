import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from status import GameStatus
from alien import Alien
from bullet import Bullet
from time import sleep
from button import Button
from scoreboard import Scoreboard


def create_fleet(settings, screen, status, aliens, num_x, num_y):
    """Create the alien fleet"""
    x_offset = settings.window_x_size / (num_y + 1)
    y_offset = (settings.window_y_size / 2) / (num_x + 1)
    for i in range(1, num_x+1):
        for j in range(1, num_y+1):
            alien = Alien(screen, settings, status.level, x_offset * j, 30 + y_offset * i, x_offset)
            aliens.add(alien)


def prepare_game(settings, screen, status, bullets, aliens, ship):
    """Prepare the main objects to start for the first time"""
    bullets.empty()
    aliens.empty()
    ship.center_ship()
    create_fleet(settings, screen, status, aliens, settings.fleet_num_rows, settings.fleet_num_cols)


def restart_game(settings, screen, status, bullets, aliens, ship):
    prepare_game(settings, screen, status, bullets, aliens, ship)
    sleep(1)


def check_events(cfg, screen, ship, bullets, playBtn, status):
    """Process user input to update object states"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if status.isRunning:
            if event.type == pygame.KEYDOWN:
                # move ship or shoot a bullet
                if event.key == pygame.K_RIGHT:
                    ship.move_right()
                elif event.key == pygame.K_LEFT:
                    ship.move_left()
                elif event.key == pygame.K_SPACE:
                    b = Bullet(screen, cfg, ship.getCannonX(), ship.getCannonY())
                    bullets.add(b)
            elif event.type == pygame.KEYUP:
                # stop the ship
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    ship.stop()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start game
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if playBtn.rect.collidepoint(mouse_x, mouse_y):
                    status.isRunning = True


def update_objects_and_game(settings, screen, ship, aliens, bullets, scoreboard, playBtn, status):
    """Execute a step in the game"""

    # update scoreboard
    scoreboard.update(status)

    if not status.isRunning:
        # if the game is stopped, nothing else to update
        return

    # update ship
    ship.update()
    # detect hit aliens and update score
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        status.updateScore(len(collisions))
    # all aliens destroyed
    if len(aliens) == 0:
        bullets.empty()
        status.levelCompleted()
        restart_game(settings, screen, status, bullets, aliens, ship)
        return
    # removed bullets out of screen and update others
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            continue
        bullet.update()
    # update aliens
    for alien in aliens:
        alien.update()
    # check if game is over: aliens reached the bottom or ship destroyed
    aliensReachedBottom = False
    for alien in aliens:
        if alien.reachBottom():
            aliensReachedBottom = True
            break
    if aliensReachedBottom or pygame.sprite.spritecollideany(ship, aliens):
        status.restartLevelIfPossible()
        restart_game(settings, screen, status, bullets, aliens, ship)


def draw_objects(ship, aliens, bullets, scoreboard, playBtn, status):
    """Draw all active elements on the screen for the current frame"""
    ship.draw()
    for alien in aliens:
        alien.draw()
    for bullet in bullets:
        bullet.draw()
    scoreboard.draw()
    if status.isRunning:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)
        playBtn.draw()


def create_screen(settings):
    """Create and configura main screen object"""
    screen = pygame.display.set_mode(settings.getWindowSize())
    pygame.display.set_caption(settings.getWindowTitle())
    return screen

