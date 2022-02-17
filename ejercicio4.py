#Otra vez una media



#En un sistema de calificaciones de 0 a 20, donde 20 es la nota más alta y 0 la más baja.

#Un profesor quiere escribir un programa que calcula la media de las cuatro notas obtenidas por sus alumnos en los deberes del mes. Además, el programa deberá calcular una evaluación automática según la media del alumno. Dará «Alumno con talento» si la media es superior a 15, «Con capacidad» si está comprendida entre 12 y 15, y, por último, «Debe reorientarse» si es inferior a 12.

#Escribir un algoritmo que toma como entrada las cuatro notas de un alumno y que calcula la media y la evaluación correspondiente.

#El problema anterior se puede resolver definiendo una estructura de datos que, para un alumno, agrupa su media y la evaluación. Un elemento de este tipo calcula el algoritmo solicitado.

from cgi import print_directory


notas = []
nota1 = notas.append(int(input("Introduce la primera nota: ")))
nota2 = notas.append(int(input("Introduce la segunda nota: ")))
nota3 = notas.append(int(input("Introduce la tercera nota: "))) 
nota4 = notas.append(int(input("Introduce la cuarta nota: "))) 
suma = 0
for i in notas: 
    suma = suma + i
suma = suma / 4
if suma > 15:
    print ("Usted es un alumno con talento, su media de las cuatro notas es: " , suma)
if suma > 12 and suma < 15 :
    print (" Usted es un alumno con capacidad, su media total es: " , suma)
if suma < 12:
    print ("Usted debe reorientarse, su media es: " , suma) 