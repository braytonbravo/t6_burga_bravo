import os
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
