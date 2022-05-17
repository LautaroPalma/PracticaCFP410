import random
from random import shuffle

#Escriba un módulo para crear el mazo.
numeros = []
cartas = []
def palos():
    global numeros
    numeros = []
    for a in range (12):
        numeros.append(a+1)
    return numeros

def mazo():
    global numeros , cartas
    palos()
    cartas = []
    for a in range (4):
        for n in numeros:
            cartas.append(n)
        cartas.remove(8)
        cartas.remove(9)
    return cartas

#Escriba un módulo para barajar las cartas (mezclarlas)
def mezclar():
    random.shuffle(cartas)

#Escriba un módulo que, dada una carta le devuelva el valor de la misma
def valor(c):
    if c<=7:
        return c
    else:
        return 0.5

#Escriba un módulo que le permita saber si un jugador se pasó del puntaje o no. Lo que indicaría si perdió o no.
def sepaso(pjug):
    if pjug> 7.5:
        print ("El jugador se paso")
    else:
        input("otra carta o quedarse con el puntaje")




carta=int
palos()
mazo()
mezclar()
print(cartas)
jugadores= int(input("Ingrese la cantidad de jugadores"))
for a in range (jugadores):
    cartas.pop(carta)
    valor(carta)
    sepaso()