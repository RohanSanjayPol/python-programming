# coding exercise

#creating an coin choice is game
# 0 is head
# 1 is tail

import random as rd
def coinGame():
    x=rd.randint(0,1)
    if(x==0):
        print("head")
    else:
        print("Tail")   

coinGame()   

# dice game
def diceGame():
    x=rd.randint(1,6)
    if(x==1):
        print("one")
    elif(x==2):
        print("two")
    elif(x==3):
        print("three")

diceGame()        