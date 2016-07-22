# Space Invaders
from random import *
#Variables
xSpeed=10
ySpeed=3
count=0
shooting = False
bulletY=435
bulletX=50
x=0
y=0

    
def setup():
    global x,y
    size(500,500)  
    x=width/2
    y=height-65



board = []
#onerow= ["1","1","1","1","1"]
board.append (["1","1","1","1","1"])
board.append (["1","1","1","1","1"])
board.append (["1","1","1","1","1"])
board.append (["1","1","1","1","1"])
'''board.append (onerow) 
board.append (onerow)
board.append (onerow)
board.append (onerow)
'''

  
  

def keyPressed():
    global x
    global bulletX
    global shooting
    print("pressed %s %d" % (key, keyCode))
    
    if keyCode==37 and x>10:
        x=x-xSpeed
    if keyCode==39 and x<=395:
        x=x+xSpeed
    #if keyCode==32
    if keyCode==32:
        shooting = True
        bulletX = x+50
            
                
    

def draw():
    global x,y
    global xSpeed,ySpeed
    global shooting
    global bulletY
    background(255,255,255) #white
    display_board()
    fill(0,0,225)
    rect (x,450,100,20)#bottom
    rect (x+25,y,50,15)#top

    if shooting == True:
        fill(255,0,0)
        ellipse (bulletX,bulletY,10,10) #bullet
        bulletY-= 2
    if bulletY < 0:
        shooting = False 
        bulletY = 435
    
    
def display_board():
    global count
    fill(0,0,275)
    i=0
    j=0

    for row in range(4):
        i=0
        for col in range(4): 
            if board[row][col]=="1" :
                fill(0,0,225)
                rect (i,j,50,50)
                if i<=bulletX <= i+60 and j<=bulletY <= j+60:
                    board[row][col]="0"
            i=i+60
        j=j+60

    