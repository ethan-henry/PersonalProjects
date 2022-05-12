from random import random
import random
from tkinter import Image

from numpy import absolute
import cv2
import mouse
import time
import keyboard
from PIL import ImageGrab
import numpy as np


# Ideas: would it be faster to read in number of mines left and test every spot to see the probability that the mine is there
# Using Stack and go back algorithm?

# start_time = time.time()
# When identifying numbers, only need to scan a couple of pixels pixel (middle of box maybe, as well as side for known or flag/unknown) to cut down time needed

# Is there any way to optimize the algorithm?  The current algorithm looks in all 8 of the surrounding squares of a number, count flags and open spaces, and uses that

# Implement an automatic restart maybe?
# if it read in a mine at any point, restart the program by clicking the little face


index = 0
x = 16
y = 16

tlFirstSquare_x = 39
tlFirstSquare_y = 230

mousex = 30
mousey = 186

grid = []

def updateGrid():
    grid = []
    coord = [tlFirstSquare_x, tlFirstSquare_y]
    image = ImageGrab.grab()
    while len(grid) < y:
        temp = []
        coord[0] = tlFirstSquare_x
        while len(temp) < x:
            block = image.crop((coord[0], coord[1], (coord[0] + 18), (coord[1] + 18)))
            pixel = block.getdata()
            if (pixel[0] == (255, 255, 255)):
                if (pixel[153] == (255, 0, 0)):
                    temp.append(-1)
                    # Flag
                else:
                    temp.append(-2)
                    # Unknown
            else:
                test = pixel[153]
                if (test == (88, 0, 253)):
                    temp.append(1)
                elif (test == (122, 180, 139)):
                    temp.append(2)
                elif (test == (226, 119, 131)):
                    temp.append(3)
                elif (test == (136, 123, 169)):
                    temp.append(4)
                elif (test == (178, 127, 131)):
                    temp.append(5)
                elif (test == (189, 189, 189)):
                    temp.append(0)
                elif (test == (26, 26, 26) or test == (28, 17, 18)):
                    print('You lose :(')
                    # mouse.move(587, 155)
                    # mouse.click('left')
                    # temp = []
                    # grid = []
                    # coord = [437, 230]
                    break
                else:
                    print("idk", test)
                    block.show()
            coord[0] += 20
        coord[1] += 20
        grid.append(temp)
    return grid

def moveMouse(x, y):
    mouse.move(30 + (x * 16), 186 + (y * 16))
    return

flagged = []
clicked = []

def moves(gridTemp):
    noMoves = True
    bestMove = []
    best = 100
    for i in range(x):
        for j in range(y):
            greenList = []
            if (gridTemp[j][i] > 0):
                flags = 0
                green = 0
                for jj in range(max(0, j-1), min(j+2, len(gridTemp))):
                     for ii in range(max(0, i-1), min(i+2, len(gridTemp[0]))):
                        if (gridTemp[jj][ii] == -1):
                            flags += 1
                        elif(gridTemp[jj][ii] == -2):
                            green += 1
                            if ((jj, ii) not in greenList):
                                greenList.append([jj, ii])
                for k in greenList:
                    if (flags == gridTemp[j][i]) and (k[1], k[0]) not in clicked:
                        clicked.append((k[1], k[0]))
                        moveMouse(k[1], k[0])
                        mouse.click('left')
                        mouse.move(5, 5, absolute=True)
                        green -= 1
                        noMoves = False
                    if (flags + green == gridTemp[j][i]) and (k[1], k[0]) not in flagged:
                        flagged.append((k[1], k[0]))
                        moveMouse(k[1], k[0])
                        mouse.click('right')
                        mouse.move(5, 5, absolute=True)
                        flags += 1
                        green -= 1
                        noMoves = False
                if (gridTemp[j][i] - flags > 0):
                    # print(gridTemp[j][i])
                    # print(flags, green)
                    temp = (green + flags) / (gridTemp[j][i] - flags)
                    if (temp < best):
                        print(greenList)
                        bestMove = [i, j]
                        best = temp
    return noMoves, bestMove

mouse.move(x/2 * 16 + tlFirstSquare_x, y / 2 * 16 + tlFirstSquare_y)
mouse.click('left')
mouse.move(5, 5)

counter = 0

while(True):
    if (keyboard.is_pressed('q')):
        print("YOU PRESSED EXIT")
        break
    grid = updateGrid()
    noMoves, bestMove = moves(grid)
    if noMoves:
        counter += 1
    else:
        counter = 0

    if (counter >= 5):
        print(bestMove)
        moveMouse(bestMove[0], bestMove[1])