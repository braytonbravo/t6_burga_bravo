import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
comprador,galletas,caramelos="",0,0.0
#INPUT
comprador=os.sys.argv[1]
galletas=int(os.sys.argv[2])
caramelos=int(os.sys.argv[3])
#PROCESSING
total=round(galletas+caramelos)
#OUTPUT
print("#################################")
print("#   BODEGA-DON MIGUEL     ")
print("############################")
print("#")
print("# comprador:",comprador)
print("#galletas:" ,galletas)
print("#caramelos:",caramelos)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(total<30):
    print("participas para un sorteo de bicicletas")
if(total>60):
    print("participas para un sorteo de televisores")
#fin_if
