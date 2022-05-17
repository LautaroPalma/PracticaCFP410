#Escriba un programa que permita escribir una lista de n palabras. Al inicio del programa se le preguntará al usuario 
# la cantidad de palabras que va a ingresar y luego se ingresarán ese número de palabras por teclado.
#Al final debe imprimir la lista de palabras en orden alfabético.

lista = []
cant= int (input ("ingrese la cantidad de palabras que va a ingresar: "))
for a in range (cant):
    palabra= input ("Ingrese una palabra:")
    lista.append(palabra)
    a+=1
lista.sort()
print(lista)