import os
#FORMULA GEOMETRICA
#DECLARACION DE LAS VARIABLES
figura,base,altura="",0.0,0.0

figura=os.sys.argv[1]import os

base=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#PROCESSING
area=round(base*altura)/2

#VERIFICADORES
area_perfecta=(area<=100)

#OUTPUT
print("################################")
print("#   FORMULA GEOMETRICA         #")
print("################################")
print("#")
print("# Figura : ", figura)
print("# Base   : ", base)
print("# altura : ", altura)
print("# Area   : ", area)

#CONDICIONALES MULTIPLES
#SI EL AREA ES Menor o igual a 100 es area perfecta
if (area_perfecta==True):
    print("area perfecta")

#SI EL AREA ES MENOR QUE 100 EJERCICIO MAL RESUELTO
if (area_perfecta<100):
    print("ejercicio mal resuelto")

#SI EL AREA ES IGUAL A 100 EJERCICIO EXCELENTE
if (area_perfecta==100):
    print("ejercicio excelente")
#fin_if
