import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
comprador,mermelada,mantequilla="",0,0.0
#INPUT
comprador=os.sys.argv[1]
mermelada=int(os.sys.argv[2])
mantequilla=float(os.sys.argv[3])
#PROCESSING
total=round((mermelada+mantequilla))
#OUTPUT
print("#################################")
print("#   BODEGA-MI JUANITA   ")
print("############################")
print("#")
print("# comprador:",comprador)
print("#mermelada : s/.",mermelada)
print("#mantequilla: $/.",mantequilla)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(total==100):
    print("ganaste un descuento del 30% ")
if(total<100):
    print("obtuviste un cupon ")
if(total>100):
    print("entraste en un sorteo de ua canasta")
#fin_if
