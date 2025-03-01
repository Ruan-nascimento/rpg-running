import pygame as pg

def draw_button(screen, text, x, y, width, height, color, hover_color, font):

    button_rect = pg.Rect(x, y, width, height)
    mouse_pos = pg.mouse.get_pos()
    

    current_color = hover_color if button_rect.collidepoint(mouse_pos) else color
    

    pg.draw.rect(screen, current_color, button_rect, border_radius=10)
    

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)


    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            return True  
    
    return False  