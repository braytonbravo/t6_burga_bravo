import os
#declarar variables
cliente,producto,precio,cantidad="","",0.0,0
#input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])
#processing
monto_total=round(precio*cantidad,2)
#vereficador
cliente_satisfecho=(monto_total<45)
#output
print("###################################")
print("#        BOLETA DE VENTA          #")
print("###################################")
print("# cliente ",cliente)
print("#producto",producto)
print("#p.u",precio)
print("cantidad",cantidad)
print("#total",monto_total)
print("###################################")
#condicion simple
#si el comprador esta satisfecho
if(cliente_satisfecho ==True ):
    print("ganaste un descuento adicional")
#fin_it
