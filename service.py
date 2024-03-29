import pygame as pg
from config import *
from random import random
#Variables

pg.init()
sc = pg.display.set_mode((H, W))

wall_break = pg.transform.scale(pg.image.load('Image/break.png').convert(),(size_cell,size_cell))
wall_empty = pg.transform.scale(pg.image.load('Image/empty.png').convert(),(size_cell,size_cell))
wall_wall = pg.transform.scale(pg.image.load('Image/wall.png').convert(),(size_cell,size_cell))
wall_corner = pg.transform.scale(pg.image.load('Image/corner.png').convert(),(size_cell,size_cell))
wall_tunnel = pg.transform.scale(pg.image.load('Image/tunnel.png').convert(),(size_cell,size_cell))
types = (wall_break,wall_empty,wall_wall,wall_corner,wall_tunnel)

connects = {
wall_break:(0,0,0,1),
wall_empty:(1,1,1,1),
wall_wall:(1,0,1,1),
wall_corner:(0,0,1,1),
wall_tunnel:(1,0,1,0),
}

coordinates ={
(1,0,0,0):(size_cell,0),
(0,1,0,0):(0,-size_cell),
(0,0,1,0):(-size_cell,0),
(0,0,0,1):(0,size_cell),
}

#Classes

class wall():
    type_wall = None
    position_wall = None
    connect = None
    def __init__(self, type_wall:pg.Surface, position_wall:tuple) -> None:
        self.type_wall = type_wall
        self.position_wall = position_wall
        self.connect = connects[type_wall]
    def rotate(self) -> None:
        self.connect = self.connect[-1:] + self.connect[:-1]
        self.type_wall = pg.transform.rotate(self.type_wall,90)
    def draw(self,screen: pg.Surface) -> None:
        screen.blit(self.type_wall,self.position_wall)
    def get_name(ind):
        match ind:
            case 0:
                return "wall_break"
            case 1:
                return "wall_empty"
            case 2:
                return "wall_wall"
            case 3:
                return "wall_corner"
            case 4:
                return "wall_tunnel"
                
#Function


def draw_lines(screen:pg.Surface, light:int) -> None:
    for x in range(size_cell,W,size_cell):
        pg.draw.line(screen,(light,light,light),(x,0),(x,H))
    for y in range(size_cell,H,size_cell):
        pg.draw.line(screen,(light,light,light),(0,y),(W,y))

def get_position(pos: tuple, connect: tuple) -> tuple:
    return (pos[0]+coordinates[connect][0], pos[1]+coordinates[connect][1])

def check(wall_position:tuple,wall_connect:wall) -> bool:
    for i in range(4):
        if wall_connect.connect[i] == 1:
            join = list(zero_connect)
            join[i] = 1
            join = tuple(join)
            if get_position(wall_connect.position_wall, join) == wall_position:
                return True
    return False

def add_queue(wall_position: tuple, paries: wall) -> tuple:
    new_queue = []
    new_connect = []
    for i in range(4):
        if paries.connect[i] == 1:
            join = list(zero_connect)
            join[i] = 1
            join = tuple(join)
            if get_position(paries.position_wall, join) == wall_position:
                join = list(paries.connect)
                join[i] = 0
                for i in range(4):
                    if join[i] == 1:
                        new_connect = list(zero_connect)
                        new_connect[i] = 1
                        new_queue.append((paries.position_wall,tuple(new_connect)))
    return tuple(new_queue)
def choice():
    rnd = random()
    prob_sum = 0
    for i, prob in enumerate(probabilities.values()):
        prob_sum += prob
        if rnd < prob_sum:
            return types[i]