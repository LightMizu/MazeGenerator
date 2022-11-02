import pygame as pg
from random import choice,seed
from config import *
from service import *


pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((H, W))
running = True
queue = [((400,400),(1,0,0,0)),((400,400),(0,1,0,0)),((400,400),(0,0,1,0)),((400,400),(0,0,0,1))]
history = []
draw_lines(screen)
screen.blit(wall_empty,(400,400))

while running:
    if queue:
        block = queue[-1]
        queue.pop()
        if 0<block[0][0]>816 or 0<block[0][1]>816:
            continue
        paries = wall(choice(types),get_position(*block))
        while not check(block[0],paries):
            paries.rotate()
        if paries.position_wall in history:
                continue
        else:
            history.append(paries.position_wall)
        queue += add_queue(block[0],paries=paries)
        paries.draw(screen=screen)
        
    else:
        print("End")
    pg.display.update() 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()