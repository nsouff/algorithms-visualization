import pygame
from pygame.locals import *
import math
from queue import PriorityQueue
class Node:
    def __init__(self, x=None, y=None, parent=None):
        self.parent = parent
        self.g = self.f = 0
        self.x = x
        self.y = y


def heuristic(n1, end):
    return abs(n1.x - end.x) + abs(n1.y - end.y)

def drawGrid():
    for i in range(0, height, 10):
        pygame.draw.line(window, (0,0,0), (0, i), (width, i), 1)
    for i in range(0, width, 10):
        pygame.draw.line(window, (0,0,0), (i, 0), (i, height), 1)

def initGrid():
    grid = [[Node(i, j) for i in range(w + 2)] for j in range(h + 2)]
    for i in range(w+2):
        grid[0][i] = None
        grid[h+1][i] = None
    for j in range(h+2):
        grid[j][0] = None
        grid[j][w+1] = None
    return grid

def wall():
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        pygame.draw.rect(window, black, ((cur[0]//10)*10, (cur[1]//10)*10, 10, 10))
        grid[cur[1]//10 + 1 ][cur[0]//10 + 1] = None

def clear():
    window.fill(white)
    drawGrid()

black = (0,0,0)
white = (255,255,255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,255,0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
width = 1500
w = 150
height = 800
h = 80
pygame.init()
pygame.display.set_caption("A*")
window = pygame.display.set_mode((width, height))
window.fill(white)
pygame.display.update()
drawGrid()
grid = initGrid()
start = (0, 0)
goal = (0, 0)

def draw_path(end):
    pygame.draw.rect(window, green, ((end.x-1)*10, 10*(end.y-1), 10, 10))
    if end.parent != None: draw_path(end.parent)



def astar(start, goal):
    first = grid[start[0] + 1][start[1] + 1]
    end = grid[goal[0] + 1][goal[1] + 1]
    first.f = math.sqrt((first.x-end.x)**2 + (first.y - end.y)**2)
    closedList = []
    openList = []
    openList.append(first)
    while len(openList) > 0:
        u = min(openList, key=lambda x:x.f)
        if u.x == end.x and u.y == end.y:
            draw_path(u)
            return
        childs = []
        j = u.x
        i = u.y
        if grid[i][j+1] != None: childs.append(grid[i][j+1])
        if grid[i][j-1] != None: childs.append(grid[i][j-1])
        if grid[i+1][j] != None: childs.append(grid[i+1][j])
        if grid[i-1][j] != None: childs.append(grid[i-1][j])
        for child in childs:
            if child in closedList:
                continue
            g = u.g + 1
            if child in openList:
                if g < child.g:
                    child.g = g
                    child.parent = u
                    child.f = heuristic(child, end) + g
            else:
                child.g = g
                openList.append(child)
                pygame.draw.rect(window, purple, (10*(child.x-1), 10*(child.y -1), 10, 10))
                child.f = heuristic(child, end) + g
                child.parent = u
        openList.remove(u)
        closedList.append(u)
        pygame.draw.rect(window, yellow, ((u.x-1) * 10, (u.y-1) * 10 , 10, 10))
        pygame.display.flip()




running = 1
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        elif running == 1 and event.type == KEYDOWN and event.key == K_SPACE :
            running = 2
        elif running == 2 and event.type == MOUSEBUTTONDOWN:
            if grid[event.pos[1]//10 + 1][event.pos[0]//10 + 1] == None:
                continue
            start = (event.pos[1]//10, event.pos[0]//10)
            pygame.draw.rect(window, blue, ((event.pos[0]//10)*10, (event.pos[1]//10)*10, 10, 10))
            running = 3
        elif running == 3 and event.type == MOUSEBUTTONDOWN:
            if grid[event.pos[1]//10 + 1][event.pos[0]//10 + 1] == None:
                continue
            goal = (event.pos[1]//10, event.pos[0]//10)
            pygame.draw.rect(window, red, ((event.pos[0]//10)*10, (event.pos[1]//10)*10, 10, 10))
            running = 4
            pygame.display.flip()
            astar(start, goal)
            running = 5
        elif running == 5 and event.type == KEYDOWN and event.key == K_SPACE:
            clear()
            grid = initGrid()
            running = 1

        if running == 1: wall()
        pygame.display.flip()
