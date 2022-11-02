import pygame as pg
from config import *
#Variables

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

coordinates ={
(1,0,0,0):(0,size_cell),
(0,1,0,0):(-size_cell,0),
(0,0,1,0):(0,-size_cell),
(0,0,0,1):(0,size_cell),
}

#Classes

class wall():
    wall = None
    position_wall = None
    connect = None
    def __init__(self, type_wall:pg.Surface, position_wall:tuple) -> None:
        self.type_wall = type_wall
        self.position_wall = position_wall
        self.connect = connects[type_wall]
    def rotate(self) -> None:
        self.connects = self.connects[-1:] + self.connects[:-1]
        self.type_wall = pg.transform.rotate(self.type_wall,90)
        
#Function


def draw_lines(screen:pg.Surface) -> pg.Surface:
    for x in range(size_cell,H,size_cell):
        pg.draw.line(screen,(100,100,100),(x,W),(x,W))
    for y in range(size_cell,H,size_cell):
        pg.draw.line(screen,(100,100,100),(0,y),(H,y))

def get_position(pos: tuple, connect: tuple) -> tuple:
    return (pos[0]+coordinates[connect][0], pos[1]+coordinates[connect][1])

def check(wall:wall,wall_connect:wall) -> bool:
    for i in range(4):
        if wall_connect.connect[i] == 1:
            if get_position(wall_connect.position_wall, wall_connect.connect) == wall.position_wall:
                return True
    return False

