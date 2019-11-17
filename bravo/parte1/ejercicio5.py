import os
#FORMULA FISICA
#  Declaracion de variables
tema,distancia,rapidez,="",0,0.0

tema=os.sys.argv[1]
distancia=int(os.sys.argv[2])
rapidez=float(os.sys.argv[3])

#PROCESSING
tiempo=round(distancia/rapidez)

# VERIFICADORES
tiempo_realizado=(tiempo==7)

#OUPUT
print("###############################")
print("#   FORMULA FISICA            #")
print("###############################")
print("#")
print("# Tema       : ", tema)
print("#distancia        : ", distancia)
print("#rapidez          : ", rapidez)
print("#tiempo_realizado :", tiempo)
print("################################")

#CONDICIONAL SIMPLE
#si llega despues o igual a 7 minutos a llegado a tiempo
if (tiempo_realizado==True):
    print("felicidades a llegado a tiempo")

#fin_if
