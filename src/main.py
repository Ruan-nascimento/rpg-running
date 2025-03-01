import pygame as pg

pg.init()

def main_game():

    # important variables 
    clock = pg.time.Clock()
    frames_per_second = 60

    # screen configurations
    window = pg.display.set_mode((0,0), pg.FULLSCREEN)
    pg.display.set_caption("Sem Nome")


    # loop configurations
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        
        #screen updates
        clock.tick()
        pg.display.flip()

    # end configurations
    pg.quit()


# init only in this archive
if __name__ == "__main__":
    main_game()