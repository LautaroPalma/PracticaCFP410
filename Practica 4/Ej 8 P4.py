# Modifique el programa anterior para que el programa contenga una lista predefinida
# por el programador de palabras no válidas o prohibidas para ingresar.

lista = []
prohibidas = ["a","s","d"]
n=1
cant= int (input ("ingrese la cantidad de palabras que va a ingresar: "))
while (n<=cant):
    palabra= input ("Ingrese una palabra:")
    if palabra in prohibidas:
        print("Esa palabra esta prohibida, ingresa otra: ")
        n-=1
    else:
        lista.append(palabra)
    n+=1

lista.sort()
print(lista)
#pal= input("que palabra busca de la lista: ")
#n=lista.count(pal)
#print(f"la palabra esta {n} veces")