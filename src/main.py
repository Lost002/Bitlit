from numbers import mainDisplay
from os import system

bitValues = []
lr = 0

"""A function for initializing the bit displayer and values. As well as the main display."""
def init():
    global bitValues
    for _ in range(9):
        bitValues.append(0)

"""A function for displaying everything"""
def display():
    pass
    
init()
display()

while True:
    for _ in bitValues:
        print(_,end="")
    print("\n",end="")
    for _ in range(lr):
        print(" ",end="")
    opt = input("")
    if opt == "<" and lr > 0:
        lr -= 1
    elif opt == ">" and lr < 7:
        lr += 1
    elif opt == "+" and bitValues[lr] == 0:
        bitValues[lr] = 1
    elif opt == "-" and bitValues[lr] == 1:
        bitValues[lr] = 0
    elif opt == "!":
        ### Check and display binary
        pass
    elif opt == "exit":
        system("clear")
        print("Terminated...")
        exit()
    system("clear")