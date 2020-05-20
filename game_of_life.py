import pygame
from pygame.locals import *
def drawGrid(color):
    for i in range(0, height, 10):
        pygame.draw.line(window, color, (0, i), (width, i), 1)
    for i in range(0, width, 10):
        pygame.draw.line(window, color, (i, 0), (i, height), 1)

def update_cell(x, y, old_grid, new_grid):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if grid[x + i][y + j] == 1:
                count += 1
    if old_grid[x][y] == 0 and count == 3:
        new_grid[x][y] = 1
        fill_rect(x, y, 1)
    elif old_grid[x][y] == 1 and count != 2 and count != 3:
        new_grid[x][y] = 0
        fill_rect(x, y, 0)
    else:
        new_grid[x][y] = old_grid[x][y]
def update_grid():
    global grid
    new_grid = [[0 for _ in range(h + 2)] for _ in range(w + 2)]
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            update_cell(i, j, grid, new_grid)
    grid = new_grid
def draw_life():
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        pygame.draw.rect(window, black, ((cur[0]//10)*10, (cur[1]//10)*10, 10, 10))
        grid[cur[0]//10 + 1][cur[1]//10 + 1] = 1

def fill_rect(x, y, c):
    if c == 0:
        pygame.draw.rect(window, white, ((x-1)*10, (y-1)*10, 10, 10))

    elif c == 1:
        pygame.draw.rect(window, black, ((x-1)*10, (y-1)*10, 10, 10))

def remove_grid():
    window.fill(white)
    for i in range(1, w+1):
        for j in range(1, h+1):
            if grid[i][j] == 1:
                pygame.draw.rect(window, black, ((i-1)*10, (j-1)*10, 10, 10))

    pygame.display.flip()
black = (0,0,0)
white = (255,255,255)
width = 1500
w = 150
height = 800
h = 80
grid = [[0 for _ in range(h + 2)] for _ in range(w + 2)]
pygame.init()
pygame.display.set_caption("Game of life")
window = pygame.display.set_mode((width, height))
window.fill(white)
drawGrid(black)
pygame.display.update()
running = 1
update_it = 0
while running:
    if running == 2 and pygame.time.get_ticks() >= update_it:
        update_grid()
        pygame.display.flip()
        update_it = pygame.time.get_ticks() + 100

    for event in pygame.event.get():
        if running == 1:
            draw_life()
            pygame.display.flip()

        if event.type == QUIT:
            running = 0
        elif running == 1 and event.type == KEYDOWN and event.key == K_SPACE :
            remove_grid()
            running = 2
            update_it = pygame.time.get_ticks() + 100
