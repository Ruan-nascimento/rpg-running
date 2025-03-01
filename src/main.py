import pygame as pg
import sys
from scenes.main_menu import Menu
from scenes.game_window import Game

pg.init()



# screen configurations
pg.display.set_caption("RPG")


# scene swift
scene = 'menu'

while True:

    if scene == 'menu':
        menu = Menu(pg.display.set_mode((1280, 720)))
        scene = menu.run()
    
    elif scene == 'game':
        game = Game(pg.display.set_mode((1280, 720)))
        scene = game.run()
    
    elif scene == 'quit':
        pg.quit()
        sys.exit()