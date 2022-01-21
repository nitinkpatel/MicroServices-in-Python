#Name : Nitin Kumar Patel
#Student ID : 0358801
#--------------------------------

#to use random choice
from random import choice

#declared the list of team names
teams = ['Challangers', 'Royals', 'KnightRiders', 'Kings', 'Devils']

#randomly importing player names from text file 
players= []
file = open('players.txt', 'r')
players= file.read().splitlines()

#declared empty lists to form teams
teamA = []
teamB = []

#distribut all players from players list to teams list
while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    #stop when all players get selected
    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

#randomly select name of teams
nameOne = choice(teams)
nameTwo = choice(teams)

#used dictionally for random printing of team names
teamPlayer = { nameOne : teamA,
               nameTwo : teamB
    }

print ('Here are your teams : ')
for k,v in teamPlayer.items():
    print (k,v)

