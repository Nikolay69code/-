import pygame
import sys

import Controls
import ino
from scores import Scores
from Gun import *
from Controls import *
from pygame.sprite import Group
from stats import Stats
def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    stats = Stats()
    sc = Scores(screen,stats)
    Controls.create_army(screen,inos)
    while True:
        Controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            Controls.update_bullets(screen,stats,sc,inos,bullets)
            Controls.update(bg_color, screen,stats,sc, gun, inos, bullets)
            Controls.update_inos(stats,screen,sc,gun,inos,bullets)


run()
