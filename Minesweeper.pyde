from Cell import Cell
import Utils

W = 500
H = W
SIZE = 20

cells = [range(SIZE) for y in range(SIZE)]
bombX = -1
bombY = -1
started = False

def setupGrid():
    size = W / SIZE
    for y in range(SIZE):
        for x in range(SIZE):
            cells[x][y] = Cell(x, y, size)
    Utils.setCells(cells)

def setBombs(percentage, notX, notY):
    numBombs = percentage * SIZE*SIZE
    while numBombs > 0:
        y = int(random(SIZE))
        x = int(random(SIZE))
        if x == notX and y == notY:
            continue
        randomCell = cells[x][y]
        randomCell.bomb = True
        numBombs -= 1

def chunk(x, y):
    cells[x][y].click()
            
    yy = y-1
    if yy < 0:
        yy = 0
    xx = x-1
    if xx < 0:
        xx = 0
    while yy <= y+1:
        if yy >= len(cells):
            break
        while xx <= x+1:
            if xx >= len(cells):
                break
            cells[xx][yy].data = Utils.countBombs(xx, yy)
            if cells[xx][yy].data == 0 and cells[xx][yy].hidden:
                chunk(xx, yy)
            elif cells[xx][yy].hidden:
                cells[xx][yy].click()
            xx += 1
        yy += 1
        xx = x-1
        if xx < 0:
            xx = 0
    
def mousePressed():
    global started
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            cell = cells[x][y]
            if cell.isHovering():
                if not started:
                    started = True
                    setBombs(0.2, x, y)
                cell.click()
                if not cell.bomb and cell.data == 0:
                    chunk(x, y)
                elif cell.bomb:
                    global bombX, bombY
                    bombX = x
                    bombY = y
                    thread("lose")
                thread("checkWin")

def keyPressed():
    global started
    if keyCode == ord('R'):
        setupGrid()
        started = False

def checkWin():
    Utils.checkWin()

def lose():
    Utils.loseAnimation(bombX, bombY)

def setup():
    global cells
    size(W, H)
    setupGrid()
    # setBombs(0.20)

def draw():
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            cells[x][y].update()
