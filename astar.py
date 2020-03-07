import pygame
from pygame.locals import *
class Node:
    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.x = x
        self.y = y
        self.h = 0
        self.g = 0
        self.f = 0
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
