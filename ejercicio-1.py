#Tarea 01
name=str(input("Mi nombre y apellido es "))
esp=str(input("Soy de la especialidad de "))
edad=int(input("Mi edad es "))
print("Mi nombre y apellido es ",name,
      "soy de laespecialidad de ",esp,
      "y mi edad es de ",edad, "años")
print("el tipo de dato del nombre es ",type(name),
      ",el tipo de dato de la especialida es ",type(esp),
      "y el tipo de dato de edad",type(edad))
#Tarea 02
temperatura = float(input("¿Cual es la temeperatura de hoy en grados Celsius? "))
F = (temperatura*1.8) + 32
print("La temperatura en grados Fahrenheit de hoy, es de: ",int(F),"°F")
#Tarea 03
sueldo=int(input("Introduzca el sueldo que percibe mensualmente: "))
descuento=(sueldo*0.1)
total_sueldo= (sueldo-descuento)
print("Usted en el próximo mes percibirá un sueldo con 10% de descuento y será: ",int(total_sueldo),"soles")
#Tarea 04
x=int(input("Inserte un número: "))
y=int(input("Inserte un número: "))
z=int(input("Inserte un número: "))
if int(x>y) and int(x>z):
    print(x," Es el mayor número")
elif int(y>x) and int(y>z):
    print(y, " Es el mayor número")
elif int(z>x) and int(z>y):
    print(z," Es el mayor número")
else:
    print("Valores invalidos")
#Tarea 05
date=int(input("Introduzca su edad: "))
if int(date<12):
    print("Tiene ",date,"años es un niño.")
elif int(date<18):
    print("Tiene ",date,"años es un adolescente.")
elif int(date<60):
    print("Tiene ",date,"años es un adulto.")
elif int(date>60):
    print("Tiene ",date,"años es un adulto mayor.")
else:
    print("Valores invalidos")
#Tarea 06
num01=int(input("Introduzca un número: "))
if num01 % 2 ==0:
    print("El número que eligió es par")
else:
    print("El número que eligió es impar")
#Tarea 07
numero02= int(input("Ingrese un número para mostrale la tabla de multiplicación: "))
print("La tabla de multiplicar de ",numero02,"es: ")
for a in range(1,13):
    respuesta= numero02*a
    print(f"{numero02}x{a}={respuesta}")
#Tarea 08
for b in range(1,31):
    operación= b
if b%2==0:
    print(f"{b} es par")
else:
    print(f"{b} es impar")
#Tarea 09
op=0
print("Ingrese números para sumarlos e ingrese 0 para terminar la suma.")
while True:
    num03= int(input("Ingrese un número: "))
    if num03 == 0:
        print("La suma es total es: ", op)
        break
    op= op +num03
#Tarea 10
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
