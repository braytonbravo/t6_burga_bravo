import os
#FORMULA FISICA
#DECLARACION DE VARIABLES
angulo,pi,tiempo=0.0,0.0,0.0

angulo=float(os.sys.argv[1])
pi=float(input("Ingrese pi:"))
tiempo=float(input("ingrese tiempo:"))

# PROCESSING
velocidad_angular=round(angulo/tiempo)

#VERIFICADORES
velocidad_angular=(velocidad_angular>5)

# OUTPUT
print("################################")
print("# FORMULA FISICA")
print("################################")
print("#")
print("# El valor del angulo es : ", angulo)
print("# El valor de  pi es     : ", pi)
print("# El valor del tiempo es : ", tiempo)
print("# La velocidad angular es: ", velocidad_angular )
print("#################################")

#CONDICIONAL MULTIPLE
#si la velocidad angular resulta mayor a 5 sera un excelente resultado
if (velocidad_angular==True):
    print("excelente ejercicio")

#si la velocidad angular resulta menos a 5 sera un ejercicio mal hecho
if (velocidad_angular<5):
    print("ejercicio mal hecho")
#si la velocidad angular resulta igual a 5 es un resultado aproximado
if (velocidad_angular==5):
    ("resultado aproximado")

#fin_if
