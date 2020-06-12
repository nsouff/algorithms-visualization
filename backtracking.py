import pygame
class Sudoku():
    def __init__(self, filename):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        with open(filename) as file:
            for i in range(9):
                for j in range(9):
                    self.grid[i][j] = int(file.read(1))
                assert(file.read(1) == '\n')
s = Sudoku('sudoku')
print(s.grid)
