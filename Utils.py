
cells = [[]]

def setCells(arr):
    global cells
    cells = arr

def countBombs(x, y):
    yy = y-1
    if yy < 0:
        yy = 0
    xx = x-1
    if xx < 0:
        xx = 0
    count = 0
    while yy <= y+1:
        if yy >= len(cells):
            break
        while xx <= x+1:
            if xx >= len(cells):
                break
            if cells[xx][yy].bomb:
                count += 1
            xx += 1
        yy += 1
        xx = x-1
        if xx < 0:
            xx = 0
    return count

def allRevealed():
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            if cells[x][y].hidden and not cells[x][y].bomb:
                return False
    return True

def winAnimation():
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            cells[x][y].highlight = True
            waitMillis(16)

def checkWin():
    if allRevealed():
        winAnimation()

# def allDead(x, y):
#     yy = y-1
#     if yy < 0:
#         yy = 0
#     xx = x-1
#     if xx < 0:
#         xx = 0
#     count = 0
#     while yy <= y+1:
#         if yy >= len(cells):
#             break
#         while xx <= x+1:
#             if xx >= len(cells):
#                 break
#             if cells[xx][yy].lost:
#                 count += 1
#             xx += 1
#         yy += 1
#         xx = x-1
#         if xx < 0:
#             xx = 0
#     return count == 9

def loseAnimation(bombX, bombY):
    x = bombX
    y = bombY
    count = 0
    total = len(cells)*len(cells[0])
    xMax = 1
    yMax = 1
    xx = 0
    yy = 0
    dir = 0 # 0=up, 1=right, 2=down, 3=left
    while count != total:
        if x >= len(cells):
            x = len(cells)-1
            y += yMax
            xx = 0
            yMax += 1
            xMax -= 1
            dir = 3
            continue
        elif y >= len(cells[0]):
            y = len(cells[0])-1
            x -= xMax
            yy = 0
            xMax += 1
            yMax -= 1
            dir = 0
            continue
        elif x < 0:
            x = 0
            y -= yMax
            xx = 0
            yMax += 1
            xMax -= 1
            dir = 1
            continue
        elif y < 0:
            y = 0
            x += xMax
            yy = 0
            xMax += 1
            yMax -= 1
            dir = 2
            continue
        
        cell = cells[x][y]
        cell.lost = True
        waitMillis(16)
        if dir == 0:    # up
            y -= 1
            yy += 1
        elif dir == 1:  # right
            x += 1
            xx += 1
        elif dir == 2:  # down
            y += 1
            yy += 1
        elif dir == 3:  # left
            x -= 1
            xx += 1
        if xx == xMax:
            xx = 0
            xMax += 1
            dir += 1
        elif yy == yMax:
            yy = 0
            yMax += 1
            dir += 1
        if dir == 4:
            dir = 0
            
    # for y in range(len(cells)):
    #     for x in range(len(cells[y])):
    #         cell = cells[x][y]
    #         cell.lost = True
    #         waitMillis(10)

def waitMillis(m):
    start = millis()
    while millis() < start+m:
        pass
