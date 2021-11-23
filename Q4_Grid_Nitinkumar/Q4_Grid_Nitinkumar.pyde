#Name : Nitinkumar Patel
#Student ID : 0358801
#Date : 03-11-2021
#Assign-2 : Que-4 : track hovering of mouse pointer and change the background color
#**************************************************************
#declare global variable
x= 255

#set the drawing area with required size
def setup():
    size (300, 300)

#use draw function for animation    
def draw():
    background(x)

#vertical lines to create 9 squares
    line(100,0,100,300)
    line(200,0,200,300)

#horizontal lines to create 9 squares
    line(0,100,300,100)
    line(0,200,300,200)
    
#using mousemoved function, to track hovering of mouse pointer
def mouseMoved():
    
#decide the 3 squares of middle row, for which background color will change
    global x
    if mouseX>0 and mouseX<300 and mouseY>100 and mouseY<200 :
        x=90
    else:
        x=255
        
  
