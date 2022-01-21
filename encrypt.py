#define all possible character
alphabet = 'abcdefghijklmnopqurstuvwxyz'

#ask user for numeric key value
key = input('Please enter desired key value :')
key = int(key)

#declare empty string to store new message
newMessage = ''

#ask user for a message to be encrypted
message = input('Please enter your message : ')

#fetch each letter from the message
for character in message:
    if character in alphabet:                   #check for alphabet or special character
        position = alphabet.find(character)     #position of that letter
        newPosition = (position + key)%26       #add key to position to find new position
        newCharacter = alphabet[newPosition]    #relavant new letter
        newMessage += newCharacter              #encrypted message
    else:
        newMessage += character                 #if not alphabe, same special character

print('Your new message is : ', newMessage)
