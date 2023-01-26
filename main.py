import pygame as pg
from random import seed,random
from config import *
from service import *
from copy import deepcopy
from os import path,mkdir

if not path.isdir("Results"):
    mkdir("Results")

seeds = random()
seed(seeds)
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
running = True
center = ((W//size_cell)//2*size_cell,(H//size_cell)//2*size_cell)
queue = [(center,(1,0,0,0)),(center,(0,1,0,0)),(center,(0,0,1,0)),(center,(0,0,0,1))]
history = [center]
draw_lines(screen,20)
screen.blit(wall_empty,center)
last_type =  None

while running:
    if queue:
        block = queue[-1]
        queue.pop()
        pos = block[0]
        print(*pos)
        if get_position(*block) in history:
            continue
        if 0>pos[0] or W<pos[0] or 0>pos[1] or H<pos[1]:
            continue
        print(*pos)
        type_block = choice()
        '''while last_type == type_block:
            type_block = choice()'''
        last_type = type_block
        paries = wall(type_block,get_position(*block))
        while not check(pos,paries):
            paries.rotate()
        else:
            history.append(paries.position_wall)
        queue += add_queue(pos,paries=paries)
        paries.draw(screen=screen)
        
    else:
        print('finish')
        pg.image.save(screen, f'Results/{seeds}.jpg' )
        running = False
    pg.display.update()
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()