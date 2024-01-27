import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows # save away
        self.nCols = nCols # save away 
        self.myRow = random.randrange(self.nRows) # chooses a random row 
        self.myCol = random.randrange(self.nCols) # chooses a random col 
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1) #
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)
        
    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols 

N_MONSTERS = 20 
N_ROWS = 100
N_COLS = 200
MAX_SPEED = 4
monsterList = []
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)
    monsterList.append(oMonster)



 

