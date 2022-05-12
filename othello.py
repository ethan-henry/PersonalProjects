from re import A
import random
import time

board = []
gameOver = False

# Need to make game over condition
# need to check if there are no valid moves

for i in range(8):
    temp = []
    for j in range(8):
        temp.append(-1)
    board.append(temp)

def move(x, y, color, check):
    if not (board[y][x] == -1):
        return ([], False)
    oldVal = board[y][x]
    board[y][x] = color
    safe = False
    output = []
    temp = []
    for i in range(x + 1, 8):
        if (board[y][i] == -1):
            break
        elif (board[y][i] != color):
            temp.append((y, i))
        elif (board[y][i] == color):
            output += temp
            if (len(temp) > 0):
                safe = True
            break
            
    temp = []
    for i in range(x - 1, -1, -1):
        if (board[y][i] == -1):
            break
        elif (board[y][i] != color):
            temp.append((y, i))
        elif (board[y][i] == color):
            output += temp
            if (len(temp) > 0):
                safe = True
            break
    temp = []
    for i in range(y + 1, 8):
        if (board[i][x] == -1):
            break
        elif (board[i][x] != color):
            temp.append((i, x))
        elif (board[i][x] == color):
            output += temp
            if (len(temp) > 0):
                safe = True
            break
    temp = []
    for i in range(y - 1, -1, -1):
        if (board[i][x] == -1):
            break
        elif (board[i][x] != color):
            temp.append((i, x))
        elif (board[i][x] == color):
            output += temp
            if (len(temp) > 0):
                safe = True
            break
            
    temp = []
    for i in range(1, 8):
        if (x + i < 8) and (y + i < 8):
            if (board[y+i][x+i] == -1):
                break
            elif (board[y+i][x+i] != color):
                temp.append((y+i, x+i))
            elif (board[y+i][x+i] == color):
                output += temp
                if (len(temp) > 0):
                    safe = True
                break
    temp = []
    for i in range(1, 8):
        if (y + i < 8) and (x - i >= 0):
            if (board[y+i][x-i] == -1):
                break
            elif (board[y+i][x-i] != color):
                temp.append((y+i, x-i))
            elif (board[y+i][x-i] == color):
                output += temp
                if (len(temp) > 0):
                    safe = True
                break
    temp = []
    for i in range(1, 8):
        if (y - i >= 0) and (x + i < 8):
            if (board[y-i][x+i] == -1):
                break
            elif (board[y-i][x+i] != color):
                temp.append((y-i, x+i))
            elif (board[y-i][x+i] == color):
                if (len(temp) > 0):
                    safe = True
                output += temp
                break
    temp = []
    for i in range(1, 8):
        if (y - i >= 0) and (x - i >= 0):
            if (board[y-i][x-i] == -1):
                break
            elif (board[y-i][x-i] != color):
                temp.append((y-i, x-i))
            elif (board[y-i][x-i] == color):
                if (len(temp) > 0):
                    safe = True
                output += temp
                break
    if (not safe or check):
        board[y][x] = oldVal
    return output, safe

# def check(x, y, deltaX, deltaY, num):
#     spaces = 0
#     while ((x >= 0) and (x < 7) and (y >= 0) and (y < 7)):
#         x += deltaX
#         y += deltaY
#         if (board[y][x] == -1):
#             return False
#         if (board[y][x] != num):
#             spaces += 1
#         if (board[y][x] == num):
#             if (spaces >= 1):
#                 return True
#             else:
#                 return False
#     return False

# def checkAll(x, y, num):
#     if (check(x - 1, y, -1, 0, num)):
#         return True
#     if (check(x + 1, y, 1, 0, num)):
#         return True
#     if (check(x, y - 1, 0, -1, num)):
#         return True
#     if (check(x, y + 1, 0, 1, num)):
#         return True
#     if (check(x - 1, y - 1, -1, -1, num)):
#         return True
#     if (check(x + 1, y - 1, 1, -1, num)):
#         return True
#     if (check(x - 1, y + 1, -1, 1, num)):
#         return True
#     if (check(x + 1, y + 1, 1, 1, num)):
#         return True
#     return False

def valid(num):
    output = []
    for i in range(8):
        for j in range(8):
            temp = move(i, j, num, True)
            if (board[j][i] == -1) and temp[1]:
                output.append([i, j])
    return output

board[3][3] = 0
board[3][4] = 1
board[4][3] = 1
board[4][4] = 0

def showboard():
    print("  1  2  3  4  5  6  7  8")
    for i in range(len(board)):
        print(i + 1, end="")
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                print(" △ ", end="")
            elif (board[i][j] == 1):
                print(" ★ ", end="")
            elif (board[i][j] == 2):
                print(" ♦ ", end="")
            else:
                print("   ", end="")
        print("")

def validText(text):
    if not (len(text) == 2):
        return False
    try:
        int(text[0])
        int(text[1])
    except:
        return False
    num1 = int(text[0])
    num2 = int(text[1])
    if (num1 in range(1, 9) and num2 in range(1, 9)):
        return True
    else:
        return False

index = 0
p1 = 0
p2 = 0
while not gameOver:
    showboard()
    temp = False
    isValid1 = valid(1)

    while ((not temp) and (len(isValid1) > 0)):
        validMove = False
        print("Star's Turn")
        # text = input("Enter your move: ")
        # text1 = text.split(" ")
        # if (validText(text1)):
        if(True):
            num = random.choice(isValid1)
            flip = move(num[0], num[1], 1, False)
            # flip = move(int(text1[0]) - 1, int(text1[1]) - 1, 1, False)
            temp = flip[1]
            if (not temp):
                print("NOT A VALID MOVE")
            for i in flip[0]:
                board[i[0]][i[1]] = 1
                p1 += 1
                p2 -= 1
            p1 += 1
        else:
            print("NOT A VALID ENTRY")
    showboard()
    temp = False
    isValid0 = valid(0)
    while ((not temp) and (len(isValid0) > 0)):
        print("Triangle's turn")
        # text = input("Enter your move: ")
        # text1 = text.split(" ")
        # if (validText(text1)):
        if (True):
            num = random.choice(isValid0)
            flip = move(num[0], num[1], 0, False)
            # flip = move(int(text1[0]) - 1, int(text1[1]) - 1, 0, False)
            temp = flip[1]
            if (not temp):
                print("NOT A VALID MOVE")
            for i in flip[0]:
                board[i[0]][i[1]] = 0
                p2 += 1
                p1 -= 1
            p2 += 1
        else:
            print("NOT A VALID ENTRY")

    if (len(valid(1)) == 0) and (len(valid(0)) == 0):
        gameOver = True

tp1 = 0
tp2 = 0
print("\nGAME OVER")

print("Player 1: ", p2 + 2)
print("Player 2: ", p1 + 2)

if (p1 > p2):
    print("Player 1 WINS")
elif (p2 > p1):
    print("Player 2 WINS")
else:
    print("TIE GAME, how'd you even do that...")

# f.close()