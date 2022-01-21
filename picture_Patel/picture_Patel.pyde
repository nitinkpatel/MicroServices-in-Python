#****************************************************************
#Name: Nitinkumar Patel
#Student ID : 0358801
#Question 2 of Basic operation Assignment
#Draw a picture of a room layout with furniture placement
# top view layout, center triangle table, carpet and flower pots in the corners
# door and window on one wall, cupboard on opposite wall
# sofa and 3 paintings on one wall, TV unit and one paintaing on opposite wall 
#****************************************************************
#Set the size of the canvas
size(1000,1000)

#create integer variables
centralPointOfRoom = 500
lineWidth = 3
minimumCoordinate=100
maximumCoordinate=900

#Set the four corner lines of the room to give top view prospective
line(centralPointOfRoom,centralPointOfRoom,minimumCoordinate,minimumCoordinate)
line(centralPointOfRoom,centralPointOfRoom,maximumCoordinate,maximumCoordinate)
line(centralPointOfRoom,centralPointOfRoom,maximumCoordinate,minimumCoordinate)
line(centralPointOfRoom,centralPointOfRoom,minimumCoordinate,maximumCoordinate)

#Set the bottom floor
rect(300,300,400,400)

#set the cupboard and fill wooden color
line(650,400,800,300)
line(650,500,800,500)
fill(193, 154, 107)
rect(800,300,50,200)
line(650,450,800,400)
line(650,500,650,400)
ellipse(710,415,30,5)
ellipse(710,445,30,5)

#set the sofa of cream color
strokeWeight(lineWidth)
fill(255,253,208)
rect(350,300,275,minimumCoordinate)
line(350,300,325,250)
line(500,300,500,250)
line(625,300,650,250)
line(325,250,650,250)
rect(325,250,325,15)

#Set the TV unit (TV table and Television on it)
fill(255,200,10)
rect(350,650,275,50)
strokeWeight(8)
line(400,700,350,725)
line(550,700,600,725)
line(350,725,600,725)

#set the carpet and center table of triangle shape
strokeWeight(1)
fill(255,246,215)
rect(350,425,275,200)
fill(234,240,240)
strokeWeight(2)
triangle(500,575,400,450,600,450)

#set the paintaings/photos on the wall behind sofa and tv
strokeWeight(2)
fill(135,206,235)
ellipse(500,200,minimumCoordinate,25)
ellipse(400,175,minimumCoordinate,20)
ellipse(600,175,minimumCoordinate,20)
ellipse(475,775,200,50)

#set the flower pot in two corners of the room
stroke(0,128,0)
fill(155,118,83)
ellipse(675,325,55,55)
ellipse(675,675,55,55)

#Set the door with handle
stroke(0,0,0)
ellipse(260,675,10,25)
stroke(255,255,255)
strokeWeight(10)
line(200,800,200,700)
line(300,625,200,700)

#set the window beside the door
line(275,350,200,300)
line(200,600,200,300)
line(275,575,275,350)
line(275,575,200,600)
