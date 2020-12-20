from random import randint, uniform
import os
os.system("cls")

players = []
points = []

print("total players: ", players)

num_player = int(input("ingrese numero de jugadores"))
i=1

while i <= num_player :
    players.append(i)
    points.append(randint(1,6)+ randint(1,6))
    i= i + 1

print("total players: ", players)
print("total points: ", points)
#players2= [1, (2,50)]
#print(players2[0])