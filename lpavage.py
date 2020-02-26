from tkinter import *
from enum import Enum
import random
import sys


class Direction(Enum):
    NO = 1
    NE = 2
    SO = 3
    SE = 4


def randomColor():
    r = random.randrange(30, 245)
    g = random.randrange(30, 245)
    b = random.randrange(30, 245)
    color = '#' + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]
    return color.upper()


def launch(event):
    widget = event.widget
    widget.config(bg='black')
    row = widget.grid_info()['row']
    col = widget.grid_info()['column']
    grid[row][col] = -1
    root.unbind("<Button-1>")
    root.after_cancel(id)
    pavage(0, 0, l, row, col)

def quadrant(p, q, l, i, j):
    if (i-p < 2**(l-1)):
        if (j-q < 2**(l-1)):
            return Direction.NO
        else :
            return Direction.NE
    else :
        if (j-q < 2**(l-1)):
            return Direction.SO
        else :
            return Direction.SE


def poseTuile(i, j, dir):
    color = randomColor()
    tab = [[0 for _ in range(2)] for _ in range(3)]
    if dir == Direction.NO:
        tab[0] = [i+1, j]
        tab[1] = [i+1, j+1]
        tab[2] = [i, j+1]

    elif dir == Direction.NE:
        tab[0] = [i, j-1]
        tab[1] = [i+1, j-1]
        tab[2] = [i+1, j]

    elif dir == Direction.SO:
        tab[0] = [i, j+1]
        tab[1] = [i-1, j+1]
        tab[2] = [i-1, j]
    else :
        tab[0] = [i, j-1]
        tab[1] = [i-1, j-1]
        tab[2] = [i-1, j]

    global count
    root.after(1*count, lambda: poseTuileAux(tab, color))
    count+=1

def poseTuileAux(tab, color):
    for k in range(3):
        r, c = tab[k][0], tab[k][1]
        canvas[r][c].config(bg=color)
def pavage(p, q, l, i, j):
    dir = quadrant(p, q, l, i, j)
    if l == 1:
        poseTuile(i, j, dir)
    else :
        m = 2**(l-1)
        if (dir == Direction.NE) :
            pavage(p, q, l-1, p+m-1, q+m-1) # NO
            pavage(p, q+m, l-1, i, j)       # NE
            pavage(p+m, q, l-1, p+m, q+m-1) # SO
            pavage(p+m, q+m, l-1, p+m, q+m) # SE
            poseTuile(p+m-1, q+m, dir)
        elif dir == Direction.NO :
            pavage(p, q, l-1, i, j)         # NO
            pavage(p, q+m, l-1, p+m-1, q+m) # NE
            pavage(p+m, q, l-1, p+m, q+m-1) # SO
            pavage(p+m, q+m, l-1, p+m, q+m) # SE
            poseTuile(p+m-1, q+m-1, dir)
        elif dir == Direction.SE :
            pavage(p, q, l-1, p+m-1, q+m-1) # NO
            pavage(p, q+m, l-1, p+m-1, q+m) # NE
            pavage(p+m, q, l-1, p+m, q+m-1) # SO
            pavage(p+m, q+m, l-1, i, j)     # SE
            poseTuile(p+m, q+m, dir)
        else : # dir == Direction.SO
            pavage(p, q, l-1, p+m-1, q+m-1) # NO
            pavage(p, q+m, l-1, p+m-1, q+m) # NE
            pavage(p+m, q, l-1, i, j)       # SO
            pavage(p+m, q+m, l-1, p+m, q+m) # SE
            poseTuile(p+m, q+m-1, dir)
l = int(input("Enter the size of the 2D Array as 2^(your number)"))
# l = int(sys.argv[1])
size = 2**l

grid = [[0 for _ in range(size)] for _ in range(size)]

root = Tk()
root.title("LPavage")
f = Frame(root)
f.pack()
count = 0
canvas = [[None for i in range(size)] for j in range(size)]
for line in range(size):
    for column in range(size):
        canvas[line][column] = Canvas(f, width=512//size, height=512//size, background='white')
        canvas[line][column].grid(row=line, column=column)
root.bind("<Button-1>", launch)
root.mainloop()
