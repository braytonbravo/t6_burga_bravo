import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,clavos,martillo,fierros="",0,0.0,0.0
#INPUT
cliente=os.sys.argv[1]
clavos=int(os.sys.argv[2])
martillo=float(os.sys.argv[3])
fierro=float(os.sys.argv[4])
#PROCESSING
total=(clavos+martillo+fierro)
#OUTPUT
print("#################################")
print("#  FERRETERIA- BURGOS   ")
print("############################")
print("#")
print("#cliente:",cliente)
print("#clavos :s/.",clavos)
print("#martillo :$/.",martillo)
print("#fierro: S/.",fierro)
print("#total :$/.",total)
print("#################################")
#condicion simple
#si el comprador esta satisfecho
if(total==50):
    print("cliente feliz  por su descuento total")
if(total<50):
    print("cliente satisfecho con su compra")
if(total>50):
    print("cliente conforme con su compra")
#fin if
