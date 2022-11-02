import pygame as pg
from config import *
from service import *

pg.init()

screen = pg.display.set_mode((H, W))
running = True

wall_break = pg.image.load('Image/break.png').convert()
wall_empty = pg.image.load('Image/empty.png').convert()
wall_wall = pg.image.load('Image/wall.png').convert()
wall_corner = pg.image.load('Image/corner.png').convert()
wall_tunnel = pg.image.load('Image/tunnel.png').convert()
types = (wall_break,wall_empty,wall_wall,wall_corner,wall_tunnel)

connects = {
wall_break:(0,0,0,1),
wall_empty:(1,1,1,1),
wall_wall:(1,0,1,1),
wall_corner:(0,0,1,1),
wall_tunnel:(1,0,1,0),
}


while running:
    draw_lines(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()