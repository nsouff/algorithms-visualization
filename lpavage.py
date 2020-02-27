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
    row = event.x // (512//size)
    x0  = row * (512//size)
    col = event.y // (512//size)
    y0 = col * (512//size)
    x1 = x0 + 512//size
    y1 = y0 + 512//size
    widget.create_rectangle(x0, y0, x1, y1, fill='black')
    widget.unbind("<Button-1>")
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
    root.after(speed*count, lambda: poseTuileAux(tab, color))
    count += 1

def poseTuileAux(tab, color):
    for k in range(3):
        r, c = tab[k][0], tab[k][1]
        x0 = r*(512//size)
        y0 = c*(512//size)
        canva.create_rectangle(x0, y0, x0 + 512//size, y0 + 512//size, fill=color)


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
if len(sys.argv) > 1:
    l = int(sys.argv[1])
else :
    l = int(input("Enter the size of the 2D Array as 2^(your number)"))
if len(sys.argv) > 2:
    speed = int(sys.argv[2])
else :
    speed = int(input("Enter the speed of each step (in ms)"))
size = 2**l

root = Tk()
root.title("LPavage")
root.geometry("512x512")
canva = Canvas(root, width=512, height=512, bg='white')
canva.pack(fill=BOTH, expand=True)

count = 0
for line in range(0, 513, 512//size):
    canva.create_line([(0, line), (512, line)])
    canva.create_line([(line, 0), (line, 512)])

canva.bind("<Button-1>", launch)
root.mainloop()
