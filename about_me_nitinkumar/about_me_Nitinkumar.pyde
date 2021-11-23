#****************************************************************************************************************
#Name: Nitin Kumar Patel
#student ID : 0358801
#Date: 22nd Oct,2021
#Question-1 of Basic operation Assignment : about me
#use Ask library to fetch data from user, merge both data and display
#****************************************************************************************************************
#import "Ask" library
import Ask

#create variables (words, whole number and decimal)
fullName = "Nitinkumar Patel"
studentId = 358801
college = "RRC"
currentCity = "Winnipeg"
latitude = 49.936580
longitude = -97.079978 

#user instructed to input their information using Ask library (string, integer and float)
yourFullName = Ask.forString("Please enter your name ")
yourId = Ask.forInt ("Please enter your student Id number")
yourCollege = Ask.forString("Please enter your college name")
yourCity = Ask.forString("Please enter the name of your current city")
yourLatitude = Ask.forFloat("Please enter the Latitude of your current location")
yourLongitude = Ask.forFloat("Please enter the longitude of your current location")

#display the gathered informaiton, str used to print numeric variables
print  "My name is " + fullName + ". " + "Nice to meet you " + yourFullName + "."
print "My student ID number is " + str(studentId) + ". " + "Your student ID number is " + str(yourId) + "."
print "My college name is " + college + ". " + "Your college name is " + yourCollege + "."
print "I am in " + currentCity + ". " + "You are in " + yourCity + "."
print "My current GPS latitude is " + str(latitude) + ". " + "Your current GPS latitude is " + str(yourLatitude) + "."
print "My current GPS longitude is " + str(longitude) + ". " + "Your current GPS longitude is " + str(yourLongitude) + "."
 
