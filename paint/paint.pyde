from random import *
eColor = color(0,0,0)
def setup():
    size(1000,500)
    fill(122,16,200)
    rect(0,0,100,100)
    
    fill(250,0,0)
    rect(100,0,100,100)
    
    fill(175,222,33)
    rect(200,0,100,100)
    
    fill(175,22,103)
    rect(300,0,100,100)

    fill(100,100,100)
    rect(400,0,100,100)
    
    fill(200,200,0)
    rect(500,0,100,100)
    
    fill(255,0,100)
    rect(600,0,100,100)
   
    fill(34,67,255)
    rect(700,0,100,100)   
    
    fill(100,200,100)
    rect(800,0,100,100)
    
    fill(255,100,200)
    rect(900,0,100,100)
def draw():
    global eColor 
    x= mouseX
    y= mouseY
    if mouseButton == LEFT:
        if mouseY < 100:
            if mouseX < 100:
                eColor = color(122,16,200)
            elif mouseX < 200:
                eColor = color(250,0,0)
            elif mouseX < 300:
                eColor = color(175,222,33)
            elif mouseX < 400:
                eColor = color(100,100,100)
            elif mouseX < 500:
                 eColor =color(200,200,0)
            elif mouseX < 600:
                 eColor =color(255,0,100)
            elif mouseX < 700:
                 eColor =color(34,67,255)
            elif mouseX < 800:
                 eColor =color(100,200,100)
            elif mouseX < 900:
                 eColor =color(255,100,200)
        else:
            fill(eColor)
            ellipse (mouseX, mouseY,10,10)