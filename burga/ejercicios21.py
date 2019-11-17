import os
#PROMEDIO DE NOTAS
#DECLARAR VARIABLES
alumno,nota1,nota2,nota3="",0.0,0.0,0.0
#INPUT
alumno=os.sys.argv[1]
nota1=float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
nota3=float(os.sys.argv[4])
#PROCESSING
promedio=round(nota1+nota2+nota3)/3
#OUTPUT
print("#################################")
print("#   PROMEDIO-NOTAS   ")
print("############################")
print("#")
print("# alumno:",alumno)
print("#nota1:",nota1)
print("#nota2:",nota2)
print("#nota3:",nota3)
print("#promedio:",promedio)
print("#################################")
#condicion simple
#el alumno esta aprobado
if(promedio>18):
    print("nota excelente")
if(promedio<18):
    print("buen trabajo")
if(promedio<11):
    print("estudiar mas")
#fin_if
