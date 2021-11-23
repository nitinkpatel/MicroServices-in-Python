#Name : Nitinkumar Patel
#Student ID : 0358801
#Date: 31-10-2021
#Assignment 2 - Question 1 - Determine if the phone should be answered or not based on given scenario
#****************************************************************************************************
#import Ask library to fetch the data from user
import Ask

#create variables
morning = Ask.forBoolean("Is it a morning ?")
mom = Ask.forBoolean("Is mom calling ?")
asleep = Ask.forBoolean("Am i asleep ?")

#check for morning, make answerPhone boolean false for morning except mom is calling
if not(morning):
    answerPhone = True
else:
    if mom:
        answerPhone = True
    else:
        answerPhone = False

#check for asleep, make answerPhone boolean variable false if fall asleep
if asleep:
    answerPhone = False
else:
    answerPhone = answerPhone

#print final value stored in boolean variable : answerPhone
print "Final value of answerPhone variable : " + str(answerPhone)

#as per the final value of answerPhone variable, print the related message
if answerPhone:
    print "Phone answer : Hello"
else:
    print "I do not answer"
