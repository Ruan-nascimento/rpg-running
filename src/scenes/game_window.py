import pygame as pg
import sys
import random as rd
from entities.leading_figure import Default_figure

pg.init()

class Game:
    
    def __init__(self, screen):
        self.running = True
        self.fill = (0, 10, 10)
        self.screen = screen
        self.info = pg.display.Info()
        self.height = self.info.current_h
        self.width = self.info.current_w
        self.player = Default_figure(60, 60, (220, 110, 44), 3, self.screen)
        
        # important variables 
        self.clock = pg.time.Clock()
        
        #tree settings
        self.tree = pg.image.load("assets/images/tree_normal.png")
    
        
    
    def run(self):
        
        
        pg.key.set_repeat(1, 10)
            
        while self.running:
            
            # variables
            keys = pg.key.get_pressed()
            # screen
            self.screen.fill(self.fill)
            
            # events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    sys.exit()
                
                # keys
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return 'menu'

                # control main actor
                self.player.move(keys)
            

            # objects on screen
            self.player.draw_figure(self.screen )
            
            
            # update
            pg.display.update()
            self.clock.tick(60)
            
        pg.quit()