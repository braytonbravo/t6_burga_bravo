import os
#Boleta de venta
#Declaracion de las variables
comprador,cantidad,pp="",0,0.0

#Input
comprador=os.sys.argv[1]
cantidad=int(os.sys.argv[2])
pp=float(os.sys.argv[3])

#Processing
Total=round(cantidad*pp)

#Verificador
comprador_sastifecho=(Total>120)

#Output
print("######################################")
print("#  BODEGA- MI DANNA")
print("######################################")
print("#")
print("# Comprador          : ", comprador)
print("# Cantidad           : ", cantidad)
print("# Precio por producto: s/.", pp)
print("# Total              : s/.", Total)
print("#####################################")

#Condicion simple
if (comprador_sastifecho==True):
    print("ganaste un descuento adicional")
#fin_if
