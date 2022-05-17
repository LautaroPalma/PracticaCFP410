#Escriba un programa que genere un sorteo para el juego del "amigx invisible". 
# Donde se ingresan los nombres de las personas que participan y a cada uno se le asigna otra persona 
# la cual será su amigx invisible. En caso que las personas sean número impar, 
# complete con el profesor para que nadie se quede sin su amigx invisible. 

import random
lista=[]
c=[]
cant= int (input ("ingrese la cantidad de personas que va a ingresar: "))
for a in range (cant):
    palabra= input ("Ingrese una nombre:")
    lista.append(palabra)
    c.append(palabra)
    a+=1
if (a % 2 != 0):
    lista.append("profesor")
    c.append("profesor")

for a in lista:
    random.shuffle(c)
    elegido= c.pop()
    while a == elegido:
        c.append(elegido)
        random.shuffle(c)
        elegido= c.pop()
    print(f"el amigo invisible de {a} es {elegido}")