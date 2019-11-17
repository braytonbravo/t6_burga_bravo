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

#CONDICIONAL DOBLE
#SI EL CLIENTE LLEVA DE PRODUCTO MAS 50 SOLES SE LE DESCUENTA EL 10%
if (cliente_sastifecho==True):
    print("Descuento el 10%")
#SI EL CLIENTE LLEVA PRODUCTOS MENOS DE 50 SOLES NO TENDRA DESCUENTO
if (cliente_sastifecho<50):
    print("no tienes descuento")

#fin_if
