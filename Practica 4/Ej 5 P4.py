#Dada la lista [10, 20, [300, 400, [5000, 6000], 500], 30, 40] escriba un programa que modifique esa lista e imprima en pantalla 
# la siguiente lista [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40].

lista = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#lista.remove([300, 400, [5000, 6000], 500])
#lista.insert(2,[300, 400, [5000, 6000, 7000], 500])
lista[2][2].insert(2,7000)
print(lista)