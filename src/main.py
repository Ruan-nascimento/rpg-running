import pygame as pg
import sys
from scenes.main_menu import Menu
from scenes.game_window import Game

pg.init()



# important variables 
clock = pg.time.Clock()
frames_per_second = 60

# screen configurations
pg.display.set_caption("Sem Nome")


# scene swift
scene = 'menu'

while True:

    if scene == 'menu':
        menu = Menu(pg.display.set_mode((1280, 720)))
        scene = menu.run()
    
    elif scene == 'game':
        game = Game(pg.display.set_mode((0,0), pg.FULLSCREEN))
        scene = game.run()