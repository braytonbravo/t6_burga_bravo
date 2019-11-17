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
print("# El P.U 02 es     : s/.", pu_02)
print("# El P.U 03 es     : s/.", pu_03)
print("# El importe total es: s/.", importe_total)
print("##############################################")

#CONDICIONALES MULTIPLES
#SI LOS PRODUCTOS SUPERAN LOS 30 SOLES GANA OTRO PRODUCTO ADICIONAL
if (total_de_productos==True):
    print("gano un producto adicional")

#SI LOS PRODUCTOS NO SUPERA LOS 30 SOLES NO TENDRA VALE
if (total_de_productos<30):
    print("no trendra vale")

#SI LOS PRODUCTOS LLEGAN HASTA LOS 30 SOLES GANA 5 SOLES
if (total_de_productos==30):
    print("gana 5 soles adicional")

#fin_ifimport os
#BOLETA DE VENTA
#DECLARACION DE LAS VARIABLES
cliente,precio_de_la_hibuprofeno,precio_de_omeprazol,precio_del_alcohol="",0,0,0.0

cliente=os.sys.argv[1]
precio_de_la_hibuprofeno=int(os.sys.argv[2])
precio_de_omeprazol=int(os.sys.argv[3])
precio_del_alcohol=float(os.sys.argv[4])

# PROCESSING
total_a_pagar=round(precio_de_la_hibuprofeno+precio_de_omeprazol+precio_del_alcohol)

#VERIFICADORES
cliente_complacido=(total_a_pagar<20)

# OUTPUT
print("#####################################")
print("#  BOTICA - MI SALUD                #")
print("#####################################")
print("#")
print("# Cliente                      : ", cliente)
print("# El precio del hibuprofeno es : s/.", precio_de_la_hibuprofeno)
print("# El precio del omeprazol es   : s/.", precio_de_omeprazol)
print("# El precio del alcohol es     : s/.", precio_del_alcohol)
print("# El total a pagar es          : s/.", total_a_pagar)
print("#####################################")

#CONDICIONALES MULTIPLES
#SI EL CLIENTE GASTA MENOS DE 20 SOLES NO TENDRA DESCUENTO
if (cliente_complacido==True):
    print("No tendra descuento")

#SI EL CLIENTE GASTA MAYOR A VEINTE SOLES TENDRA DESCUENTO UNICO
if (cliente_complacido>20):
    print("descuento unico")

#SI EL CLIENTE GASTA MAS DE 30 SOLES TENTRA DESCUENTO POR CADA PRODUCTO
if (cliente_complacido>30):
    print("descuento por cada producto")
#fin_if

