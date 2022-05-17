#Escriba un programa que dada la lista [1, 2, 3, 4, 5, 6, 7] convierta cada elemento a su cuadrado (n*n) 
# en una lista nueva y luego imprima por pantalla la nueva lista.
#Practica4 Ejercicio 1
lista = [1, 2, 3, 4, 5, 6, 7]
cuadrado = []
for n in lista:
  a=(n*n)
  cuadrado.append(a)
print (cuadrado)