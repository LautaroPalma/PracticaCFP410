'Trabajo Practico 1'
#Desarrolle un programa que permita que el usuario escriba texto en modo interactivo hasta que llegue la palabra @fin
#  En dicho momento debe terminar la toma de palabras y debe informar la cantidad de palabras escritas que no figuran
#  en el diccionario.

'''la funcion "contpalabra" verifica si las palabras se encuentran en el diccionario e indica la cantidad de las que no lo estan'''
def contpalabra(archivo):
    with open(archivo ,'r', encoding ='utf-8') as file:
        dic = open('spanish.lst','r', encoding ='utf-8')
        d= dic.read()
        cont = 0
        errores=[]
        a , b = 'áéíóúü' , 'aeiouu'
        trans= str.maketrans(a,b)
        for linea in file.readlines():
            pal=linea.lower()
            for p in pal.split():
                p = ''.join(filter(str.isalnum, p))
                palabra =p.translate(trans)
                if palabra not in d:
                    cont+= 1
                    errores.append(palabra)
                    print(palabra)
        if cont==0:
            print('no hay ninguna palabra fuera del diccionario')
        else:
            print(f'hay {cont} palabra/s que no esta/n en el diccionario')
        dic.close()
        nuevapalabra= endicc(errores, dic)
        

def endicc(palabra, dic):
    a= int(input("1:Re escribir la palabra \n 2:Agregarla al diccionario de palabras \n 3:Ignorar y seguir \n"))
    if a ==1:
        np=input("Ingrese la palabra para corregir: ")
        return np
    elif a ==2:
        ap= palabra
        ap.append(dic)
    else:
        pass

'''la funcion "escribir" permite ingresar texto hasta que  el usuario ingrese "@fin" y luego verifica si estan dentro del dicc(contpalabra)'''               
def escribir():
    file='file.txt'
    with open(file, 'wt', encoding = 'utf-8') as archivo:
        a=input("ingrese el texto hasta ingresar '@fin': ")
        while a != "@fin":
            archivo.write(a +'\n')
            a=input("ingrese el texto hasta ingresar '@fin': ")
        print("finalizó el texto")
    contpalabra(file)

#Modifique el programa de la primer etapa para que levante el texto desde un archivo en texto plano. El programa 
# no debe perder la funcionalidad adquirida en la primer etapa y debe ser capaz de realizar las dos opciones 
# dependiendo la elección del usuario.

'''la funcion "leer" permite leer un archivo de texto y luego verifica si estan dentro del dicc(contpalabra)'''               

def leer():
    arc=input('ingrese el nombre del archivo ')
    contpalabra(arc)


'''la funcion "elegirtexto" es para elegir el metodo de entrada del archivo para que sea procesado'''                 
def elegirtexto():
    a= int(input('elija un metodo de entrada para el texto:\n 1:texto interactivo\n 2: archivo de texto\n'))
    if a ==1:
        escribir()
    else:
        leer()

def parametrosSO():
    import sys
    a = len(sys.argv)
    print("Total arguments passed:", a)

    if a ==1:
        escribir()
    else:
        contpalabra(sys.argv[1])



#elegirtexto()
parametrosSO()