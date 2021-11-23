#Name : Nitinkumar Patel
#Student ID : 0358801
#Date : 11 Nov 2021
#Assignment-3 : Question-2 :  using loop print number or messages as per spacific requirement
#*********************************************************************************************
#birth month : June, birth day : 5
#favorite number between 3 and 9 is : 7

#loop that starts at 100 and go to zero decreasing by one and print all values
counter = 100
while counter >= 0:

#check for a favorite number or multiple of 7
    if counter%7 == 0:
        print "favorite"
        
#check for the birth day or birth month along with favorite number or multiple of it
        if counter == 6 or counter == 5:
            print "happy birthday nitin-kumar" 
            
#check for the birth month or birth number
    elif counter == 6 or counter == 5:
        print "happy birthday nitin-kumar" 
        
#print the current iteration and decrease it by one
    else:
        print str(counter)
    counter -= 1
