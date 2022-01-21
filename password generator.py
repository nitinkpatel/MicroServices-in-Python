#importing random functionality
import random 

#storing everything
chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()' 

#ask user for number of passwords
numbers= input('how many number of passwords you want ?')
numbers= int(numbers)

#ask user for length of password
length= input('Please enter desired password length ?')
length=int(length)


for p in range(numbers):                    #repeat loop as per number of password required
    password=''
    for c in range(length):                 #repeat loop as per length of password 
        password += random.choice(chars)
    print(password)
