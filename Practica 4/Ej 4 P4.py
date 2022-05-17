#Escriba un programa que tome por teclado la temperatura media de cada día de la semana. Una vez tomados los datos que deben ser ingresados 
# por teclado, debe informar la temperatura máxima y la mínima y qué día ocurrió cada una
#Practica 4 Ejercicio 4

tmax=-999999
tmin=999999
dmin=str
dmax=str
def Tmax(temperatura, diamax):      #esta funcion compara la temperatura max actual con la ingresada y guarda la mayor y en que dia ocurrio
    global tmax
    global dmax
    if temperatura > tmax:
        tmax = temperatura
        dmax = diamax

def Tmin(temperatura, diamin):      #esta funcion compara la temperatura min actual con la ingresada y guarda la menor y en que dia ocurrio
    global tmin
    global dmin
    if temperatura < tmin:
        tmin = temperatura
        dmin = diamin

dias=["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
for a in dias:
    temp=float(input("Ingrese temperatura del dia  " + a ))
    Tmin(temp,a)
    Tmax(temp,a)
print (f"la temperatura maxima fue el dia  {dmax} con  {tmax}")
print (f"la temperatura minima fue el dia  {dmin} con  {tmin}")
