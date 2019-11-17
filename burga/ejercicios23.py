import os
#declarar variables
cliente,libro1,libro2,libro3="",0.0,0.0,0.0
#input
cliente=os.sys.argv[1]
libro1=float(os.sys.argv[2])
libro2=float(os.sys.argv[3])
libro3=float(os.sys.argv[4])
#processing
monto_total=(libro1+libro2+libro3)
#output
print("###################################")
print("#        LIBRERIA-JUANITAPYTH         #")
print("###################################")
print("# cliente ",cliente)
print("#libro 1 S/.",libro1)
print("#libro 2 s/.",libro2)
print("#libro 3 s/.",libro3)
print("#total s/.",monto_total)
print("###################################")
#condicion simple
#si el comprador esta satisfecho
if(monto_total==50):
    print("ganaste un libro totalmente gratis")
if(monto_total<50):
    print("ganaste un descuento en tu proxima compra de libro ")
if(monto_total>50):
    print("ganaste un descuento del 10% en tu proxima compra ")
#fin_it
