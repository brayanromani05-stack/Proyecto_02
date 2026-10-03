#Registro de notas
alumnos= ["Alumno01","Alumno02"]
total_alumnos= len (alumnos)
print(f"Tienes {total_alumnos} alumnos registrados")
pregunta = str(input("¿Desea comenzar el llenado de notas? "))
if pregunta == "si" or "Si" or "SI":
    aprobados = 0
    desaprobados = 0
    for alumno in alumnos:
       print(f"Introduzca las notas de {alumno}")
       mate= int(input("Introduzca la nota del estudiante en el curso de Matemática: "))
       comu= int(input("Introduzca la nota del estudiante en el curso de Comunicación: "))
       histo= int(input("Introduzca la nota del estudiante en el curso de Historia: "))
       nota_final= int(mate+comu+histo)
       promedio_final=int(nota_final/3)
       if promedio_final >= 11:
           aprobados+=1
       else:
           desaprobados += 1
       print(f"El promedio final de el {alumno} es de {promedio_final}")
    print(f"La cantidad de aprobados es {aprobados}")
    print(f"La cantidad de desaprobados es {desaprobados}")
else:
    print("Acción nula")


        

