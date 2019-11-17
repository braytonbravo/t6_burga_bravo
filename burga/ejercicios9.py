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
#VEREFICADOR
cliente_satisfecho=(total<10)
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
if(cliente_satisfecho==True):
    print("cliente satisfecho or la compra")
#fin_if
