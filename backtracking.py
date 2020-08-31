import pygame
import sys

black = (0, 0, 0)
white = (255,255,255)

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'sudoku' # default sudoku grid


def grid(filename):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    with open(filename) as file:
        for i in range(9):
            for j in range(9):
                grid[i][j] = int(file.read(1))
            assert(file.read(1) == '\n')

def draw(grid, window):
    for i in range(9):
        width = 1
        if i%3 == 0:
            width = 3
        pygame.draw.line(window, black, (i*100, 0), (i*100, 900), width)
        pygame.draw.line(window, black, (0, i*100), (900, i*100), width)
        for j in range(9):
            if gird[i][j] != 0:
                pass

def valid_number(grid, n, x, y):
    for i in range(9):
        if grid[x][i] == n or grid[i][y] == n:
            return False

    for i in range((x//3) * 3, (x//3 + 1)*3):
        for j in range((y//3) * 3, (y//3 + 1)*3):
            if grid[i][j] == n:
                return False

    return True



def main():
    pygame.init()
    window = pygame.display.set_mode((900, 900))
    s = Sudoku('sudoku')
    window.fill(white)
    s.draw(window)
    pygame.display.update()
    while True:
        pass
if __name__ == '__main__':
    main()
