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
                    self.running = False
                    return 'quit'
                    sys.exit()
                    

            
            # background
            self.screen.blit(self.background, (0, 0))
            
            
            #button play
            if draw_button(self.screen, "Jogar", 440, 230, 400, 60, (205,133,63), (210,105,30), self.font):
                return 'game'
            
            #button options
            if draw_button(self.screen, "Opções", 440, 330, 400, 60, (205,133,63), (210,105,30), self.font):
                return 'options'
            
            #button leave game
            if draw_button(self.screen, "Sair do Jogo", 440, 430, 400, 60, (205,133,63), (210,105,30), self.font):
                self.running = False
                sys.exit()
            
            
            # updates
            pg.display.flip()
        