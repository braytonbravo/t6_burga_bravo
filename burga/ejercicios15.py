import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,artefacto1,artefacto2="",0.0,0.0
#INPUT
cliente=os.sys.argv[1]
artefacto1=float(os.sys.argv[2])
artefaco2=float(os.sys.argv[3])
#PROCESSING
total=round(artefacto1+artefaco2)
#OUTPUT
print("#################################")
print("#   ELECTRODOMESTICOS_EFE  ")
print("############################")
print("#")
print("#cliente:",cliente)
print("#artefacto1:",artefacto1)
print("#artefacto2:",artefacto2)
print("#total:",total)
print("#################################")
#condicion simple
#el alumno esta aprobado
if(total>1000):
    print("Felicidades! ganaste una plancha gratis ")
if(total<1000):
    print("tienes un descuento del 25%")
#fin_if
