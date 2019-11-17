import os
#BOLETA DE VENTA
#DECLARACION DE VARIABLES
cliente,arroz,manzana,aceite="",0.0,0.0,0.0

cliente=os.sys.argv[1]
arroz=float(os.sys.argv[2])
manzana=float(os.sys.argv[3])
aceite=float(os.sys.argv[4])

#PROCESSING
total=round(arroz+manzana+aceite)

#VERIFICADOR
cliente_sastifecho=(total>50)

# OUTPUT
print("#######################################")
print("#    BODEGA - MI DANNA   ")
print("#######################################")
print("#")
print("# cliente    : ", cliente)
print("# arroz      : ", arroz)
print("# manzana    : ", manzana)
print("# aceite     : ", aceite)
print("# total      : ", total)
print("#######################################")

#CONDICIONAL SIMPLE
#SI EL CLIENTE LLEVA DE PRODUCTO MAS 50 SOLES SE LE DESCUENTA EL 10%
if (cliente_sastifecho==True):
    print("Descuento el 10%")
#fin_if



angulo,pi,tiempo=0.0,0.0,0.0

angulo=float(os.sys.argv[1])
pi=float(input("Ingrese pi:"))
tiempo=float(input("ingrese tiempo:")import os
#FORMULA FISICA
#DECLARACION DE VARIABLES
)

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

#CONDICIONAL SIMPLE
#si el la velocidad angular resulta mayor a 5 sera un excelente resultado
if (velocidad_angular==True):
    print("excelente resultado")
#fin_if
