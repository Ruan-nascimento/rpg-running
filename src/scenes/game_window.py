import pygame as pg
import sys

pg.init()

class Game:
    
    def __init__(self, screen):
        self.running = True
        self.fill = (0, 0, 255)
        self.screen = screen
    
    
    def run(self):
        
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                    self.running = False
                
                # keys
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return 'menu'
            
            
            self.screen.fill(self.fill)
            
            # update
            pg.display.update()
            
        pg.quit()