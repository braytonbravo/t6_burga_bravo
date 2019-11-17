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
#VEREFICADOR
comprador_gandor=(total>60)
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
if(comprador_gandor==True):
    print(" Felicidades ganaste un pase gratis al cine")
#fin_if
