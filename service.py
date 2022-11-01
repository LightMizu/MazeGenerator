import pygame
from config import *
#Variables

wall_break = pygame.image.load('Image/break.png').convert()
wall_empty = pygame.image.load('Image/empty.png').convert()
wall_wall = pygame.image.load('Image/wall.png').convert()

wall_corner = pygame.image.load('Image/corner.png').convert()

wall_tunnel = pygame.image.load('Image/tunnel.png').convert()

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
    def __init__(self, type_wall, position_wall:tuple) -> None:
        self.type_wall = type_wall
        self.position_wall = position_wall
        self.connect = connects[type_wall]
    def rotate(self) -> None:
        self.connects = self.connects[-1:] + self.connects[:-1]
        self.type_wall = pygame.transform.rotate(self.type_wall,90)