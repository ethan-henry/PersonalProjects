from random import random
import random
from tkinter import Image

from numpy import absolute
import cv2
import mouse
import time
from PIL import ImageGrab

# Hard dim: (575, 305, 1325, 925)
#PLAN:
#   1. Go through row by row and update the grid
#   2. Figure out best place to click or places where flag can be placed
#   loop

# pseudo for grid update:
# def grid_update(self):
#   read square
#   if light green or dark green:
#       put -2 in the grid
#   else:
#       switch for color:
#           number: put that number in the grid
#           light brown or dark brown: put 0 in the grid
#           flag: put -1 in grid

# Hard: x = 20, y = 24, tablex = 460, tabley = 245
# Medium: x = 14, y = 18, tablex = , tabley =  

grid = []
x = 20
y = 24
tablex = 460
tabley = 245

def updateGrid():
    gridTemp = []
    im2 = ImageGrab.grab(bbox =(575, 305, 1325, 930))
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
            block = im2.crop((31 * j, 31 * i, 31 * (j + 1), 31 * (i + 1)))
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


# Find numbers
# Find flags around
# if flags around + green squares == number:
#   put flag there
# elif there are green blocks around and flags == number:
#   click green
# else:
#   Move on

# page: (575, 305, 1325, 930)
# box: (31 * j, 31 * i, 31 * (j + 1), 31 * (i + 1))
# box center: (31 * (j + .5) + 575, 31 + (i + .5) + 305)

def moves(gridTemp):
    flagged = []
    clicked = []
    allGreen = []
    # didSomething = True
    for i in range(x):
        for j in range(y):
            greenList = []
            if (gridTemp[i][j] == -2):
                allGreen.append([i, j])
            if (gridTemp[i][j] > 0):
                flags = 0
                green = 0
                for ii in range(max(0, i-1), min(i + 2, len(gridTemp))):
                    for jj in range(max(0, j-1), min(j+2, len(gridTemp[0]))):
                        if (gridTemp[ii][jj] == -1):
                            flags += 1
                        elif(gridTemp[ii][jj] == -2):
                            green += 1
                            if ((ii, jj) not in greenList):
                                greenList.append((ii, jj))
                if (flags == gridTemp[i][j]):
                    for k in greenList:
                        if (k[0], k[1]) not in clicked:
                            clicked.append((k[0], k[1]))
                            print(k[0], k[1])
                            mouse.move((25 * (k[1] + .5)) + tablex, (25 * (k[0] + .5) + tabley), absolute=True)
                            mouse.click('left')
                            mouse.move(5, 5, absolute=True)
                            # didSomething = False
                elif (flags + green == gridTemp[i][j]):
                    for k in greenList:
                        if (k[0], k[1]) not in flagged:
                            flagged.append((k[0], k[1]))
                            mouse.move((25 * (k[1] + .5)) + tablex, (25 * (k[0] + .5)) + tabley, absolute=True)
                            mouse.click('right')
                            mouse.move(5, 5, absolute=True)
                            # didSomething = False
    # if (didSomething):
    #     temp = random.choice(allGreen)
    #     print(temp)
    #     mouse.move((25 * (temp[1] + .5)) + 460, (25 * (temp[0] + .5)) + 245, absolute=True)
    #     mouse.click('left')
    #     mouse.move(5, 5, absolute=True)

#1060, 245         

mouse.move((25 * (10 + .5)) + tablex, (25 * (12 + .5) + tabley), absolute=True)
mouse.click('left')
for i in range(75):
    grid = updateGrid()
    moves(grid)
    time.sleep(.29)
    for i in grid:
        for j in i:
            print(j, " ", end="")
        print("\n")

# for i in range(y):
#     for j in range(x):
#         mouse.move((25 * (i + .5)) + 460, (25 * (j + .5)) + 245, absolute=True)
#         time.sleep(1)