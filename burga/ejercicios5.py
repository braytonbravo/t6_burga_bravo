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
#VEREFICADOR
comprador_ganadpor=(total>100)
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
if(comprador_ganadpor==False):
    print("sigue intentando ")
#fin_if
