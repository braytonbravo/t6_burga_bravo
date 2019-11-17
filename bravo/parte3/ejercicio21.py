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

#Condicion multiple
#SI EL COMPRADOR GASTA MAS DE GANA UN DESUENTO ADICIONAL
if (comprador_sastifecho==True):
    print("ganaste un descuento adicional")

#SI EL COMPRADOR GASTA MENOR QUE 100 NO GANA NADA
if (comprador_sastifecho<100):
    print("no gano nada ")

#SI EL COMPRADOR GASTA 100 acumula puntos
if (comprador_sastifecho==100):
    print("acumula puntos")
#fin_if

