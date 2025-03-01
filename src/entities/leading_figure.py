import pygame as pg

class Default_figure:
    def __init__(self, w=200, h=200, color=(255,255,255), speed=10, screen=0):
        self.w = w
        self.h = h
        self.center_x = screen.get_width() // 2
        self.center_y = screen.get_height() // 2
        self.figure = pg.Rect(self.center_x - self.w // 2, self.center_y - self.h // 2, w, h)
        self.color = color
        self.speed = speed

    
    
    def move(self, keys):
        
        if keys[pg.K_w]:
            self.figure.y -= self.speed
        
        if keys[pg.K_s]:
            self.figure.y += self.speed
        
        if keys[pg.K_a]:
            self.figure.x -= self.speed
        
        if keys[pg.K_d]:
            self.figure.x += self.speed
    
    
    def draw_figure(self, screen):
        
        pg.draw.rect(screen, self.color, self.figure)
    
    