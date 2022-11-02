import pygame as pg
from random import choice,seed,random
from config import *
from service import *

seeds = random()
seed(seeds)
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
running = True
queue = [((400,400),(1,0,0,0)),((400,400),(0,1,0,0)),((400,400),(0,0,1,0)),((400,400),(0,0,0,1))]
history = [(400,400)]
draw_lines(screen,20)
screen.blit(wall_empty,(400,400))
last_type =  None

while running:
    if queue:
        block = queue[-1]
        queue.pop()
        if get_position(*block) in history:
            continue
        if 15<block[0][0]>W or 15<block[0][1]>H:
            continue
        type_block = choice(types)
        while last_type == type_block:
            type_block = choice(types)
        last_type = type_block
        paries = wall(type_block,get_position(*block))
        while not check(block[0],paries):
            paries.rotate()
        else:
            history.append(paries.position_wall)
        queue += add_queue(block[0],paries=paries)
        paries.draw(screen=screen)
        
    else:
        print('finish')
        pg.image.save(screen, f'Results/{seeds}.jpg' )
        running = False
    pg.display.update() 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()