#Sucesor de un DÍA de la semana

#El tipo DÍA define por enumeración un día de la semana. En el ejercicio que determina el día del 1 de mayo de un año dado, también se ha especificado una función sucesor para un día de la semana. Falta dar una definición de esta función.

#Dar una definición completa de la función sucesor para un día de la semana.

#Todavía no disponemos de las herramientas que nos permitirán dar una definición «elegante» de esta función. Lo haremos más adelante.
n = input("introduce un dia de la semana: ")
dias = n

if dias == "Lunes":
    print("Martes")
if dias == "Martes":
    print("Miercoles")
if dias == "Miercoles":
    print("Jueves")
if dias == "Jueves":
    print("Viernes")
if dias == "Viernes":
    print("Sabado")
if dias == "Sabado":
    print("Domingo")
if dias == "Domingo":
    print("Lunes")    