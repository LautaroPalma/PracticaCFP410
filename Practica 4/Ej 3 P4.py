#Escriba un programa que genere una lista con números consecutivos del 1 al 1000
#Practica 4 Ejercicio 3
contador = 0
lista = []
while contador <= 1000: 	
    contador += 1
    lista.append(contador)
cant = len(lista)
print(cant)