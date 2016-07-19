# paddle game
# variables 
x=250
y=250
xSpeed=5
ySpeed=3
    

def setup():
    size(500,500)
    
def draw():
    global x,y 
    global xSpeed,ySpeed
    background(255)
    ellipse (x,y,50,50)
    fill(190,210)
    x = xSpeed + x
    y = ySpeed + y
#condtional # 425/75 wall boundry
    if x > 425 or x < 75: 
       xSpeed = xSpeed * -1 
    if y >425 or y <75:
        ySpeed=ySpeed * -1
    rect(mouseX,30,100,30)  
    if x > mouseX and x < mouseX + 30 and y < 60:
        ySpeed