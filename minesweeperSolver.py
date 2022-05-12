from random import random
import random
from tkinter import Image

from numpy import absolute
import cv2
import mouse
import time
from PIL import ImageGrab
import numpy as np

# When identifying numbers, only need to scan a single pixel (middle of box maybe) to cut down time needed

# Hard: x = 20, y = 24, tablex = 460, tabley = 245, box=(575, 305, 1325, 930), boxsize=25, crop = 31
# Medium: x = 14, y = 18, tablex = 490 , tabley =282, box = (611, 355, 1285, 881), boxsize=30 crop = 37.5

grid = []
# Hard:
x = 20
y = 24
tablex = 460
tabley = 245
box = (575, 305, 1325, 930)
boxsize = 25
crop = 31

# Medium:
# x = 14
# y = 18
# tablex = 490
# tabley = 282
# box = (611, 355, 1285, 881)
# boxsize = 30
# crop = 37.5

flagged = []
clicked = []

def updateGrid():
    gridTemp = []
    im2 = ImageGrab.grab(bbox = box)
    for i in range(x):
        temp_row = []
        for j in range(y):
            num1 = 0
            num2 = 0
            num3 = 0
            num4 = 0
            num5 = 0
            num6 = 0
            num7 = 0
            num8 = 0
            blank = 0
            num0 = 0
            flag = 0
            block = im2.crop((crop * j, crop * i, crop * (j + 1), crop * (i + 1)))
            for pixel in block.getdata():
                if pixel == (14, 92, 209): num1 += 1
                elif pixel == (0, 159, 65): num2 += 1
                elif pixel == (236, 0, 38): num3 += 1
                elif pixel == (146, 0, 160): num4 += 1
                elif pixel == (255, 138, 0): num5 += 1
                elif pixel == (0, 155, 168): num6 += 1
                elif pixel == (65, 63, 57): num7 += 1
                elif pixel == (159, 158, 158): num8 += 1
                elif pixel == (130, 229, 80) or pixel == (140, 235, 87) or pixel == (162, 239, 122): blank += 1
                elif pixel == (221, 186,153) or pixel == (236, 196, 159): num0 += 1
                elif pixel == (255, 0, 0): flag += 1
            val = [num0, num1, num2, num3, num4, num5, num6, num7, num8, blank, flag]
            great = val.index(max(val))
            if (great == 0):
                val.pop(0)
                val.pop(8)
                newGreat = val.index(max(val))
                if (val[newGreat] >= 2):
                    temp_row.append(newGreat + 1)
                else:
                    temp_row.append(0)
            elif (great == 9):
                val.pop(9)
                newGreat = val.index(max(val))
                if (val[9] >= 50):
                    temp_row.append(-1)
                else:
                    temp_row.append(-2)
            elif (great > 0) and (great < 9):
                temp_row.append(great)
            elif (great == 10):
                temp_row.append(-1)
        gridTemp.append(temp_row)
    return gridTemp


# Dark green: RGB(130,229,80)
# Light Green: RGB(140, 235, 87)
# Very light green, when you're hovering: RGB(162, 239, 122)

# Dark Brown: RGB(221, 186, 153)
# Light Brown: RGB(236, 196, 159)

# number 1: RGB(14, 92, 209)
# number 2: RGB(0, 159, 66)
# number 3: RGB(236, 0, 44)
# number 4: RGB(146, 0, 160)
# number 5: RGB(255, 142, 0)
# number 6: RGB(0, 155, 168)
# number 7: RGB(65, 63, 57)
# number 8: RGB(159, 158, 158)

# flags: RGB(255, 0, 0)

def stuck(gridTemp):
    greatest = 0
    save = 0
    for i in range(x):
        for j in range(y):
            greens = []
            if (gridTemp[i][j] > 0):
                temp = gridTemp[i][j]
                for ii in range(max(0, i-1), min(i+2, len(gridTemp))):
                    for jj in range(max(0, j-1), min(j+2, len(gridTemp[0]))):
                        if (gridTemp[ii][jj] == -1):
                            temp -= 1
                        elif (gridTemp[ii][jj] == -2):
                            temp += 1
                            greens.append([ii, jj])
                if (greatest < temp):
                    greatest = temp
                    save = greens
    coord = random.choice(save)
    mouse.move(boxsize * (coord[1] + .5) + tablex, boxsize * (coord[0] + .5) + tabley, absolute=True)
    mouse.click('left')
    mouse.move(5, 5, absolute=True)


def moves(gridTemp, noM):
    allGreen = []
    # didSomething = True
    noMoves = noM
    first = 0
    for i in range(x):
        for j in range(y):
            greenList = []
            if (gridTemp[i][j] == -2):
                allGreen.append([i, j])
            if (gridTemp[i][j] > 0):
                flags = 0
                green = 0
                for ii in range(max(0, i-1), min(i+2, len(gridTemp))):
                    for jj in range(max(0, j-1), min(j+2, len(gridTemp[0]))):
                        if (gridTemp[ii][jj] == -1):
                            flags += 1
                        elif(gridTemp[ii][jj] == -2):
                            green += 1
                            if ((ii, jj) not in greenList):
                                greenList.append([ii, jj])
                if (flags + green == gridTemp[i][j]):
                    for k in greenList:
                        if (k[0], k[1]) not in flagged:
                            flagged.append((k[0], k[1]))
                            mouse.move((boxsize * (k[1] + .5)) + tablex, (boxsize * (k[0] + .5)) + tabley, absolute=True)
                            mouse.click('right')
                            mouse.move(5, 5, absolute=True)
                            flags += 1
                            green -= 1
                            noMoves = False
                            # didSomething = False
                elif (flags == gridTemp[i][j]):
                    for k in greenList:
                        if (k[0], k[1]) not in clicked:
                            clicked.append((k[0], k[1]))
                            mouse.move((boxsize * (k[1] + .5)) + tablex, (boxsize * (k[0] + .5) + tabley), absolute=True)
                            mouse.click('left')
                            mouse.move(5, 5, absolute=True)
                            green -= 1
                            noMoves = False
                            # didSomething = False
    return noMoves


#WORK ON:
#   Implement patterns

mouse.move((boxsize * ((x / 2) + .5)) + tablex, (boxsize * ((y / 2) + .5) + tabley), absolute=True)
mouse.click('left')
mouse.move(5, 5, absolute=True)

noM = False

while(True):
    grid = updateGrid()
    noMoves = moves(grid, noM)
    # if noMoves:
    #     stuck(grid)
    # time.sleep(.5)
    # ^ Enable to make The program make a guess when it's stuck
    noM = True
