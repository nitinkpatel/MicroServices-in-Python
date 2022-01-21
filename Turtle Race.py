
from turtle import *                #importing turtle module
from random import randint          #importing random numbers

penup()
goto(-280,280)                      #starting location for numbers


for step in range(15):              #creating track
    write(step, align ='center')    #writing 0 to 14
    right(90)                       #turn right
    for dots in range(8):           #Dashed lines
        penup()
        forward(20)                     #leave vertical gap
        pendown()                       #drawing line
        forward(20)                     #draw required length
    penup()                         #going back to top
    backward(320)
    left(90)                        #turn left and leave horizontal gap
    forward(40)

srk = Turtle()                      # srk is red turtle
srk.color('red')
srk.shape('turtle')
srk.penup()
srk.goto(-300,40)                  #location of red turtle(x,y)
srk.pendown()

for move in range(36):              #rotated 360 degree for twirl effec
  srk.left(10)

kris = Turtle()                     # second blue turtle named kris
kris.color('blue')
kris.shape('turtle')
kris.penup()
kris.goto(-300,100)
kris.pendown()

for move in range(60):
  kris.left(6)

remo = Turtle()
remo.color('green')
remo.shape('turtle')
remo.penup()
remo.goto(-300,160)
remo.pendown()

for move in range(12):
  remo.left(30)

robo = Turtle()
robo.color('orange')
robo.shape('turtle')
robo.penup()
robo.goto(-300,220)
robo.pendown()

for move in range(45):
  robo.left(8)

for move in range(200):             #to reach till the finish line
    srk.forward(randint(1,5))       #assigned random distance
    kris.forward(randint(1,5))
    remo.forward(randint(1,5))
    robo.forward(randint(1,5))
