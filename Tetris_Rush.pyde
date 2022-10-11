import random

NUM_ROWS = 20
NUM_COLS = 10

class Block():
    def __init__(self,x,y,w,h):
        self.w = w
        self.h = h
        self.x=x
        self.y=y
        self.colors = {"Red":(255,51,52), "Blue":(12,150,228), "Green":(30,283,66), "Yellow":(246,187,0), "Purple":(76,0,153), "White":(255,255,255), "Black":(0,0,0)}
        self.block_color = self.colors[random.choice(self.colors.keys())]
    
    def display(self):
        fill(self.block_color[0], self.block_color[1], self.block_color[2])
        rect(self.x,self.y,self.w,self.h)
        
    def move(self,start_x,start_y):
        self.start_x = self.start_x + self.deltax
        self.start_y = self.start_y + self.deltay

num_list = [0]

class Game():
    def __init__(self):
        
        self.speed = 0
        self.start_y = 0
        
        for i in range(10):
            num_list.append(i*20)
        self.start_x = random.choice(num_list)
        
        self.block=Block(self.start_x,self.start_y,20,20)
        
        self.deltax = 0
        self.deltay = 20
        
    def display(self):  
        self.block.display()
        self.block.move(self.start_x,self.start_y)
    
game = Game()

def setup():
    size(200,400)
    background(210)
    stroke(180)   
    for i in range(NUM_ROWS):
        line(0, 20*i, 200, 20*i) 
    for c in range(NUM_COLS):
        line(20*c, 0, 20*c, 400)

def draw():
    frameRate(1)
    game.display()
    """if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1:
        background(210)
    #this calls the display method of the game class 
        game.display()"""
