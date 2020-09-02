import pygame
import sys
from pygame.locals import *
import tkinter
from tkinter import simpledialog


black = (0, 0, 0)
white = (255,255,255)
clock = None
digits = [None for _ in range(9)]
FPS = None

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'sudoku' # default sudoku grid file


def init_grid(filename):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    with open(filename) as file:
        for i in range(9):
            for j in range(9):
                grid[i][j] = int(file.read(1))
            assert(file.read(1) == '\n')
    return grid
def draw(grid, window):
    window.fill(white)
    for i in range(9):
        width = 1
        if i%3 == 0:
            width = 3
        pygame.draw.line(window, black, (i*100, 0), (i*100, 900), width)
        pygame.draw.line(window, black, (0, i*100), (900, i*100), width)
        for j in range(9):
            if grid[i][j] != 0:
                for n in range(1, 10):
                    if grid[i][j] == n:
                        window.blit(digits[n-1], (j*100 + 30, i*100 + 30))
                        pass
    clock.tick(FPS)
    pygame.display.update()
def valid_number(grid, n, x, y):
    for i in range(9):
        if grid[x][i] == n or grid[i][y] == n:
            return False

    for i in range((x//3) * 3, (x//3 + 1)*3):
        for j in range((y//3) * 3, (y//3 + 1)*3):
            if grid[i][j] == n:
                return False

    return True

def find_pos(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return False

def solve(grid, window):
    draw(grid, window)
    pos = find_pos(grid)
    if not pos:
        return True
    x, y = pos
    for n in range(1, 10):
        if valid_number(grid, n, x, y):
            grid[x][y] = n
            if solve(grid, window):
                return True
            grid[x][y] = 0
    return False

def init_digits():
    global digits
    font = pygame.font.SysFont("Arial", 50)
    for i in range(9):
        digits[i] = font.render(str(i+1), True, black)


def freeze(window):
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False

def init_fps():
    global FPS
    pop = tkinter.Tk()
    pop.withdraw()
    FPS = simpledialog.askinteger("Steps per second", "How many steps per second ?", initialvalue=10)
    pop.destroy()
def main():
    global clock
    pygame.init()
    window = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku Solver")
    clock = pygame.time.Clock()
    grid = init_grid(filename)
    init_digits()
    init_fps()
    draw(grid, window)
    solve(grid, window)
    freeze(window)
if __name__ == '__main__':
    main()
