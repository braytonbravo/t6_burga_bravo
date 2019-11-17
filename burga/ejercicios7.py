import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,tijeras,pegamento,folder="",0,0.0,0.0
#INPUT
cliente=os.sys.argv[1]
tijeras=int(os.sys.argv[2])
pegamento=float(os.sys.argv[3])
folder=float(os.sys.argv[4])
#PROCESSING
total=(tijeras+pegamento+folder)
#VEREFICADOR
cliente_satisfecho=(total>120)
#OUTPUT
print("#################################")
print("#   LIBREIA-SAN MATEO   ")
print("############################")
print("#")
print("#cliente:",cliente)
print("#tijeras:s/.",tijeras)
print("#folder :$/.",folder)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(cliente_satisfecho==False):
    print("ganaste un descuento para tu proxima compra")
#fin_if
