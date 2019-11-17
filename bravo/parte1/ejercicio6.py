import os
#BOLETA DE VENTA
#DECLARACION DE VARIABLES
vendedor,precio_fierros,precio_alambres="",0,0.0

vendedor=os.sys.argv[1]
precio_fierros=int(os.sys.argv[2])
precio_alambres=float(os.sys.argv[3])

#PROCESSING
precio_venta=round(precio_fierros+precio_alambres)

#VERIFICADORES
vendedor_sastifecho=(precio_venta>50)

#OUTPUT
print("#############################")
print("#  FORMULA MATEMATICA       #")
print("#############################")
print("#")
print("# Vendedor        : ", vendedor)
print("# Precio de fierros: ", precio_fierros)
print("# Precio de alambres: ", precio_alambres)
print("# Precio de venta : ", precio_venta)
print("##############################")

#CONDICIONALES SIMPLE
#SI EL PRECIO DE VENTA SUPERA A LOS 50 SOLES EL VENDEDOR ESTARA SASTIFECHO
if (vendedor_sastifecho==True):
    print("vendedor sastifecho")
#fin_if
