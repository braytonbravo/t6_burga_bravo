import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
comprador,cantidad,pp=",",0,0.0
#INPUT
comprador=os.sys.argv[1]
cantidad=int(os.sys.argv[2])
pp=float(os.sys.argv[3])
#PROCESSING
total=round(cantidad*pp)
#VEREFICADOR
cliente_satisfecho=(total<200)
#OUTPUT
print("#################################")
print("#   TIENDA-INDILUX  ")
print("############################")
print("#")
print("# comprador:",comprador)
print("#cantidad de productos:",cantidad)
print("precio de cada producto :$/.",pp)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(cliente_satisfecho==True):
    print("ganaste un descuento del 50%")
#fin_if
