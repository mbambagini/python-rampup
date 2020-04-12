# todo: pause

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from status import GameStatus
from alien import Alien
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard
from utils import prepare_game
from utils import create_screen
from utils import check_events, update_objects_and_game, draw_objects

def main_game_loop():
    # create screen
    cfg = Settings()
    pygame.init()
    screen = create_screen(cfg)
    # create main objects of the game
    status = GameStatus(cfg)
    ship = Ship(screen, cfg)
    scoreboard = Scoreboard(screen, cfg, status)
    aliens = Group()
    bullets = Group()
    playBtn = Button(screen, cfg, "Play")
    # setup game to start
    prepare_game(cfg, screen, status, bullets, aliens, ship)
    # main loop
    while True:
       # check user input
       check_events(cfg, screen, ship, bullets, playBtn, status)
       # update object states
       screen.fill(cfg.getBackgroundColor())
       update_objects_and_game(cfg, screen, ship, aliens, bullets, scoreboard, playBtn, status)
       # draw objects
       draw_objects(ship, aliens, bullets, scoreboard, playBtn, status)
       pygame.display.flip()

# start game
main_game_loop()

