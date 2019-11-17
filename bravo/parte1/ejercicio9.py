import os
#BOLETA DE VENTA
#DECLARACION DE LAS VARIABLES
productos,pu_01,pu_02,pu_03="",0,0.0,0

productos=os.sys.argv[1]
pu_01=int(os.sys.argv[2])
pu_02=float(os.sys.argv[3])
pu_03=int(os.sys.argv[4])

# PROCESSING
importe_total=round(pu_01+pu_02+pu_03)

#VERIFICADORES
total_de_productos=(importe_total>30)

# OUTPUT
print("##############################################")
print("#  BOLETA DE VENTA ")
print("##############################################")
print("#")
print("# Los productos son : ", productos)
print("# El P.U 01 es     : s/.", pu_01)
print("# El P.U es     : s/.", pu_02)
print("# El P.U 03 es     : s/.", pu_03)
print("# El importe total es: s/.", importe_total)
print("##############################################")

#CONDICIONALES SIMPLE
#SI LOS PRODUCTOS SUPERAN LOS 30 SOLES GANA OTRO PRODUCTO ADICIONAL
if (total_de_productos==True):
    print("gano un producto adicional")
#fin_if
