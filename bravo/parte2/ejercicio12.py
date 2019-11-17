import os
#BOLETA DE NOTAS
#DECLARACION DE LAS VARIABLES
alumno,nota1,nota2,nota3="",0,0,0

alumno=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#PROCESSING
promedio_ponderado=round(nota1+nota2+nota3)/3

#VERIFICADOR
alumno_satstifecho=(promedio_ponderado>10)

#OUTPUT
print("##############################")
print("# BOLETAS DE NOTAS           #")
print("##############################")
print("#")
print("# Alumno             : ", alumno)
print("# Nota1              : ", nota1)
print("# Nota2              : ", nota2)
print("# Nota3              : ", nota3)
print("# Promedio Ponderado : ", promedio_ponderado)
print("##############################")

#CONDICION DOBLE
#SI EL ALUMNO SACA EL PROMEDIO PONDERADO MAYOR QUE 10 ENTONCES ESTA APROBADO
if (alumno_satstifecho==True):
    print("Alumno aprobado")

#SI EL ALUMNO SACA PROMEDIO PONDERADO MAYO A 14 PUEDE DAR EXAMEN A UNA UNIVERSIDAD
if (alumno_satstifecho>14):
    print("puedes dar examen a la universidad")

#fin_if


