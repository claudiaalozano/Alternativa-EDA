from calendar import c


alumnos= 50
dias=7
coste_comida=3.5*dias*alumnos
alojamiento=0
if alumnos<=25:
    coste_base_por_alumno=67.30 
    alojamiento= 4.75*alumnos*dias 
elif alumnos>25:
    coste_base_por_alumno=61
elif alumnos<=30:
    alojamiento= 4.75*alumnos*dias
elif alumnos>31 and alumnos<=35:
    alojamiento= 4*alumnos*dias
elif alumnos>35:
    alojamiento= 3.5*alumnos*dias
coste_global= coste_comida+ coste_base_por_alumno + alojamiento
coste_alumno= coste_global/alumnos
print("el coste global es:", coste_global)
print("el coste por alumno será:", coste_alumno)