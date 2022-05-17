#Escriba un programa que genere una lista de 100 elementos con números enteros aleatorios entre -1000 y 1000.
#  Y luego informe la suma y el promedio de todos los elementos de la lista.
#Practica 4 Ejercicio 2
import random
contador = 0
prom = 0
lista = []
while contador < 100: 	
    numero= random.randint(-1000, 1000)
    lista.append(numero)
    contador += 1
    prom += numero
print(prom/100)