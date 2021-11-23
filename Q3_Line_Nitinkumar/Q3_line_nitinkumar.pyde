#Name : Nitinkumar Patel
#Student ID : 0358801
#Date : 01-11-2021
#Assignment-2 : Question-3 : Animation of line moving from left to right
#***************************************************************************

#set the global veriable
x=0

#set drawing area of 310*310 size
def setup():
    size(310,310)
    
#set the line 3 pixel wide and white color
    strokeWeight(3)
    stroke(200)
#create vertical line
    line(x,310,x,0)
    
#create animation using draw function
def draw():
    global x
    x+=10

#begin from other side of the window, when area ends
    if x > width:
        x=0

#cleared background with light gray color
    background(128)
    line(x,310,x,0)
