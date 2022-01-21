#Name : Nitinkumar Patel
#Student ID : 0358801
#Date: 31-10-2021
#Assignment 2 - Question 2 - Determine ages of three friends are equally apart or not
#************************************************************************************
#import Ask library to fetch the data from user
import Ask

#create variables to store the ages in whole numbers
friend1 = Ask.forInt("Age of Friend 1 ? : ")
friend2 = Ask.forInt("Age of Friend 2 ? : ")
friend3 = Ask.forInt("Age of Friend 3 ? : ")

#sort the three ages, find oldest, youngest and middle number
#compare friend 1 with remaining two
if friend1 > friend2 and friend1 > friend3:
    oldestFriend = friend1
    if friend2 > friend3:
        middleFriend = friend2
        youngestFriend = friend3
    else:
        middleFriend = friend3
        youngestFriend = friend2

#compare friend 2 with remaining two
if friend2 > friend1 and friend2 > friend3:
    oldestFriend = friend2
    if friend1 > friend3:
        middleFriend = friend1
        youngestFriend = friend3
    else:
        middleFriend = friend3
        youngestFriend = friend1
        
#compare friend 3 with remaining two
if friend3 > friend1 and friend3 > friend2:
    oldestFriend = friend3
    if friend1 > friend2:
        middleFriend = friend1
        youngestFriend = friend2
    else:
        middleFriend = friend2
        youngestFriend = friend1

#find age gap by subtracting numbers               
ageGap12 = oldestFriend - middleFriend
ageGap23 = middleFriend - youngestFriend

#compare age gaps and print the relavant message
if ageGap12 == ageGap23:
    print "The ages of my friends are " + str(ageGap12) + " years apart."
else:    
    print "My friends ages are not the same."
