import pygame
black = (0, 0, 0)
white = (255,255,255)
class Sudoku():
    def __init__(self, filename):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        with open(filename) as file:
            for i in range(9):
                for j in range(9):
                    self.grid[i][j] = int(file.read(1))
                assert(file.read(1) == '\n')
    def draw(self, window):
        for i in range(9):
            width = 1
            if i %3 == 0:
                width = 3
            pygame.draw.line(window, black, (i*100, 0),(i*100, 900), width)
            pygame.draw.line(window, black, (0, i*100),(900, i*100), width)
            for j in range(9):
                if self.grid[i][j] != 0:
                    pass
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
