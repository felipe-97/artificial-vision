
import os
from random import randint, uniform 

acumulado1 = 0
acumulado2 = 0

os.system("cls")

print("Enter first number: ")
print("[1]. Basic Level ")
print("[2]. Medium Level ")
print("[3]. Advance Level")
print("Please, enter any option (1-3): ")
op = input()
if op == '1' :
    print("Basic Level 50 Points")
    print("::::::::::::::::::::::::")
    while acumulado1 <= 50 or acumulado2 <= 50:
        print("Turno jugador1")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice1->",dice1,"Dice2->",dice2)
        print ("Lleva", acumulado1,"+",dice1,"+",dice2)
        acumulado1 = acumulado1+dice1+dice2 
        print("Acumulado del jugador1:", acumulado1 )
        print("____________________________:")
        print("Turno jugador2")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("Dice 1->",dice1,"Dice 2->",dice2)
        print ("Lleva", acumulado2,"+",dice1,"+",dice2)
        acumulado2 = acumulado2+dice1+dice2
        print("Acumulado del jugador2:", acumulado2 )
        print("____________________________:")
    

        if acumulado1 >=50 :
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador1")
               
        elif acumulado2 >=50:
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Ganador jugador2")    
               
      
elif op == '2' :
    print("Medium Level 70 Points")
    print("::::::::::::::::::::::::")
    print("Dice 1: ", dice1)
    print("Dice 2: ", dice2)
    print("Acumulado",dice1+dice2)
elif op == '3' :
    print("Advance Level 100 Points")
    print("::::::::::::::::::::::::")
    print("Dice 1: ", dice1)
    print("Dice 2: ", dice2)
    print("Acumulado",dice1+dice2)
else :
    print("::: Invalid option :::")