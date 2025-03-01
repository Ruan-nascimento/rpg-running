import pygame as pg
import random as rd

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




def set_trees(path, n_tree, screen, tree):

    tree_image = pg.image.load(path)  

  
    num_trees = n_tree
    trees = []

    for _ in range(num_trees):
        x = rd.randint(30, screen.get_width() - 30)  
        y = rd.randint(10, screen.get_height() - 10)  
        trees.append(tree(x, y, tree_image))  


    barriers = [tree.rect for tree in trees]  
    
    return trees
