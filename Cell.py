from Utils import countBombs

class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.posX = x*size
        self.posY = y*size
        
        self.hidden = True
        self.bomb = False
        self.lost = False
        self.highlight = False
        self.data = 0
    
    def update(self):
        self.render()
    
    def render(self):
        stroke(0)
        strokeWeight(1)
        if self.lost:
            fill(200, 0, 0)
        elif self.highlight:
            fill(0, 200, 0)
        elif self.hidden:
            fill(50)
            if self.isHovering():
                fill(100)
        else:
            fill(150)
        rect(self.posX, self.posY, 50, 50)
        if not self.hidden:
            fill(20, 20, 20)
            textSize(20)
            if self.bomb:
                text("L", self.posX+self.size*2/8, self.posY+self.size*8/10)
            elif self.data != 0:
                text(self.data, self.posX+self.size*2/8, self.posY+self.size*8/10)
    
    def click(self):
        self.hidden = False
        self.data = countBombs(self.x, self.y)
    
    def isHovering(self):
        return mouseX > self.posX and mouseX < self.posX+self.size and mouseY > self.posY and mouseY < self.posY+self.size
