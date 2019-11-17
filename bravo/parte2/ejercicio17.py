import os
#BOLETA DE VENTA
#DECLARACION DE LAS VARIABLES
cliente,precio_de_licuadora,precio_de_lavadora,precio_del_televisor="",0.0,0.0,0.0

cliente=os.sys.argv[1]
precio_de_licuadora=float(os.sys.argv[2])
precio_de_lavadora=float(os.sys.argv[3])
precio_del_televisor=float(os.sys.argv[4])

# PROCESSING
precio_total=round(precio_de_licuadora+precio_de_lavadora+precio_del_televisor)

#VERIFICADORES
cliente_sastifecho=(precio_total>60)

# OUTPUT
print("############################################")
print("#    PLAZA VEA   ")
print("############################################")
print("#")
print("#  Cliente                   : ", cliente)
print("# El precio de la licuadora es: s/.", precio_de_licuadora)
print("# El precio de lavadora es    : s/.", precio_de_lavadora)
print("# El precio del televisor es  : s/.", precio_del_televisor)
print("# El precio total es          : s/.", precio_total)
print("############################################")

#CONDICIONALES DOBLES
#SI EL CLIENTE COMPRA LOS PRODUCTOS A MAS DE 60 SOLES SE LLEVARA OTRO PRODUCTO ADICIONAL
if (cliente_sastifecho==True):
    print("ganaste un producto adicional")

#SI EL CLIENTE COMPRA LOS PRODUCTOS A MENOS DE 60 SOLES NO TENDRA SU PRODUCTO ADICIONAL
if (cliente_sastifecho<60):
    print("no tendra su producto adicional")

#fin_if


