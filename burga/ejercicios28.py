import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,polera,pantalon,chaleco="",0,0.0,0.0
#INPUT
cliente=os.sys.argv[1]
polera=int(os.sys.argv[2])
pantalon=float(os.sys.argv[3])
chaleco=float(os.sys.argv[4])
#PROCESSING
total=(polera+pantalon+chaleco)
#OUTPUT
print("#################################")
print("#   TIENDA-RIPLEY   ")
print("############################")
print("#")
print("#cliente:",cliente)
print("#polera :s/.",polera)
print("#pantalon :$/.",pantalon)
print("#chaleco: s/.",chaleco)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(total==60):
    print("obtubiste 20 puntos bonus")
if(total<60):
    print("obtuviste 10 puntos bonus")
if(total>60):
    print("obtuviste 30 puntos bonus")
#fin_if
