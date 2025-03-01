import pygame as pg
import sys

from utils.utils import draw_button


pg.init()

class Menu:
    
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.fill = (0, 255, 0)
        self.font = pg.font.Font(None, 40)
        
        # images
        self.background = pg.image.load("assets/images/background_menu.jpg")
        
    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                    self.running = False
                    return 'quit'

            
            # background
            self.screen.blit(self.background, (0, 0))
            
            
            #button
            if draw_button(self.screen, "Começar", 540, 330, 200, 60, (0, 128, 255), (0, 200, 255), self.font):
                return 'game'
            
            
            # updates
            pg.display.flip()
        
        pg.quit()
        