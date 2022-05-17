# Modifique el programa anterior agregando la opción de cuenta palabras. 
# Al finalizar el programa y luego de imprimir la lista pregunte qué palabra le gustaría buscar en la lista. 
# Luego debe contar la cantidad de veces que aparece dicha palabra.

lista = []
n=0
cant= int (input ("ingrese la cantidad de palabras que va a ingresar: "))
for a in range (cant):
    palabra= input ("Ingrese una palabra:")
    lista.append(palabra)
    a+=1
lista.sort()
print(lista)
pal= input("que palabra busca de la lista: ")
n=lista.count(pal)
print(f"la palabra esta {n} veces")