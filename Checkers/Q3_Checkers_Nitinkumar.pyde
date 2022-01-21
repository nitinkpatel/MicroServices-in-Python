#Name : Nitinkumar Patel
#Student ID : 0358801
#Date : 12 Nov 2021
#Assignment-3 : Question-3 : 8*8 checkerboard with color
#********************************************************
#set the size of canvas
size (400,400)

# set 8*8 squares to cover entire canvas
for x in range(350):
    for y in range(350):

# select alternate squares using if loop
        if (x+y)%2 == 0:

#light color squares
            fill(255,255,128)
            rect(x*50,y*50,50,50)

        else:
#dark color squares
            fill(128,0,64)
            rect(x*50,y*50,50,50)


    
