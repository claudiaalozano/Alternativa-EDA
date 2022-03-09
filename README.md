# Alternativa-EDA
Esther, Carla, Teresa y Claudia hemos realizado 8 programas en python.


La dirección de github es:https://github.com/claudiaalozano/Alternativa-EDA.git

Ejercicio 1: Sucesor de un DÍA de la semana

El tipo DÍA define por enumeración un día de la semana. En el ejercicio que determina el día del 1 de mayo de un año dado, también se ha especificado una función sucesor para un día de la semana. Falta dar una definición de esta función.

Dar una definición completa de la función sucesor para un día de la semana.

Todavía no disponemos de las herramientas que nos permitirán dar una definición «elegante» de esta función. Lo haremos más adelante.

```n = input("introduce un dia de la semana: ")
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
```

Ejercicio 2: Números, suma y producto

Dados dos números cualesquiera.

Clasificarlos respecto a su suma y a su producto.

Así, por ejemplo, dados a = -15 y b = 6, se obtiene a x b < a < a + b < b cuyos sus valores son, en orden: -90, -15, -9 y 6.

```from array import array


a= 5
b= 6
multiplicacion= a*b
suma= a+b
lista= [b,a,multiplicacion,suma]
lista.sort()
print(lista[0],'<',lista[1],'<',lista[2],'<', lista[3])
```

Ejercicio 3: Descuento

Un comerciante hace un descuento del 5 % en todas las compras con un importe comprendido entre 100 y 500 €, y del 8 % en los importes superiores.

Escribir el algoritmo de cálculo del importe del descuento en una compra dada.

```def descuento(precio):
    print("Precio inicial = 120. \n ")
    # Importe del descuento acordado sobre 'precio'
    if precio < 0:
        print("Error")
    elif precio >= 0:
        if precio < 100:
            descuento = 0
            print(precio)
        elif precio < 500:
            descuento = 0.05
            print("Precio con el descuento aplicado = ", precio - descuento*precio)
        else:
            descuento = 0.08
            print(precio - precio*descuento)
descuento(120)
```


Ejercicio 4: Otra vez una media

En un sistema de calificaciones de 0 a 20, donde 20 es la nota más alta y 0 la más baja.

Un profesor quiere escribir un programa que calcula la media de las cuatro notas obtenidas por sus alumnos en los deberes del mes. Además, el programa deberá calcular una evaluación automática según la media del alumno. Dará «Alumno con talento» si la media es superior a 15, «Con capacidad» si está comprendida entre 12 y 15, y, por último, «Debe reorientarse» si es inferior a 12.

Escribir un algoritmo que toma como entrada las cuatro notas de un alumno y que calcula la media y la evaluación correspondiente.

El problema anterior se puede resolver definiendo una estructura de datos que, para un alumno, agrupa su media y la evaluación. Un elemento de este tipo calcula el algoritmo solicitado.


```nota1 = int(input("Introduce la primera nota: "))
nota2 = int(input("Introduce la segunda nota: "))
nota3 = int(input("Introduce la tercera nota: "))
nota4 = int(input("Introduce la cuarta nota: "))
suma = (nota1 + nota2 + nota3 + nota4) / 4
if suma > 15:
    print ("Usted es un alumno con talento, su media de las cuatro notas es: " , suma)
if suma > 12 and suma < 15 :
    print (" Usted es un alumno con capacidad, su media total es: " , suma)
if suma < 12:
    print ("Usted debe reorientarse, su media es: " , suma) 
```


Ejercicio 5: Con ADIF puedes

ADIF hace descuento a las familias que van al Parque Warner Madrid en función de la cantidad de niños que hay en la familia. Este descuento es del 10 % para 2 niños, 15 % para 3 niños y 18 % para 4 niños. A partir de 5 niños, el descuento es del 18 %, pero aumenta un 1 % por cada niño por encima de 4.

Establecer el algoritmo que calcula el importe del descuento al que tendrá derecho una familia dada.

```niños=8
precio= 20*niños
if niños<2:
    print(precio)
if niños==2:
    print(precio-precio*0.1)
if niños==3:
    print(precio-precio*0.15)
if niños==4:
    print(precio-precio*0.18)  
if niños>=5:
    print (precio-(precio*(0.18+(niños-4)*0.1)))
```

Ejercicio 6: Descuento en los microprocesadores

La empresa UNTEL hace descuentos por la compra al por mayor de sus microprocesadores. Estos descuentos dependen de la cantidad de componentes pedidos y del cliente que los pide.

El descuento concedido es de un 10 % si la cantidad de componentes pedidos se encuentra entre 10 000 y 20 000, un 15 % si la cantidad se encuentra entre 20 001 y 40 000 y un 20 % para más de 40 000 componentes.

Además, si el cliente es COMMAQ, el descuento se reduce un 2 %. Por último, BEL disfruta de un descuento mejorado en un 1 %.

Establecer el algoritmo del cálculo del porcentaje de descuento concedido a un cliente dado para un pedido dado.

```def microprocesadores(componentes, cliente, precio):
    if componentes >= 10000 and componentes <= 20000:
        descuento = 0.1
        preciofinal = precio - precio*descuento
        print(preciofinal)
    elif componentes >= 20001 and componentes <= 40000:
        descuento = 0.15
        preciofinal = precio - precio*descuento
        print(preciofinal)
    else:
        descuento = 0.2
        preciofinal = precio - precio*descuento
        print(preciofinal)
        
    if cliente == 1:
        #cliente = 1 significa que es COMMAQ; sino, cliente = 0 no COMMAQ
        descuento = 0.02
        precioporcliente = preciofinal - preciofinal*descuento
        print(precioporcliente)

#si me pide por teclado:
#componentes = int(input("ntr"))
#microprocesadores(componentes, 0, 35000)
microprocesadores(500000, 0, 35000)
```

Ejercicio 7: Viaje escolar

Un profesor planea organizar un viaje escolar. El coste del viaje depende de la cantidad de alumnos participantes.

El coste del trayecto es de 67,30 € por alumno hasta 25 alumnos y de 61,00 € si hay más de 25 alumnos. El coste de la comida es de 3,50 € por día y por alumno. Por último, el alojamiento es de 4,75 € por día y por alumno si la cantidad de alumnos es inferior a 30; 4,00 € para una cantidad de alumnos de entre 31 y 35, y 3,50 € si son más de 35.

Establecer el algoritmo de cálculo del precio de coste por alumno y del coste global del viaje en función de la cantidad de alumnos.

```from calendar import c


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
```

Ejercicio 8: Prima anual

A final de año, la empresa LA CAMPANA paga una prima anual a sus empleados camioneros.

En principio, el conductor recibirá la prima anual completa si no ha tenido accidentes con una responsabilidad superior o igual al 20 % durante el año que termina. Si la responsabilidad es superior al 20 %, la empresa considera al conductor responsable del accidente. Si el conductor ha sido responsable de un accidente, solo recibe la mitad de la prima. Con dos accidentes, solo recibe un tercio. Con tres accidentes, la prima se reduce a un cuarto. Si supera los tres accidentes, la prima se anula.

Esta prima es la suma de una prima de distancia y de una prima de antigüedad.

La prima de distancia aumenta un céntimo por kilómetro recorrido durante el año, con un máximo de 400 €.

La prima de antigüedad solo se paga una vez transcurridos cuatro años de antigüedad y es de 200 €. Luego aumenta 20,00 € por año adicional.

Escribir el algoritmo de cálculo de la prima anual que se concederá a cada conductor.

```prima_antiguedad = float (0.0) 
prima_distancia = float (0.0)
accidentes= int(input("¿Cuantos accidentes ha tenido?:"))
antiguedad = int(input ("¿Antiguedad del conductor?:"))
kilometros= int(input ("Introduzca el número de kilometros que ha realizado:"))


#antiguedad
if antiguedad < 4:
    prima_antiguedad = prima_antiguedad
if antiguedad >= 4:
    prima_antiguedad= 200 + 20 * (antiguedad - 4)

#distancia recorrida
kilometros = kilometros * 0.01 
if kilometros > 400:
    kilometros= 400
    prima_distancia = 400
if kilometros > 400:
    kilometros = kilometros
    prima_distancia = kilometros

# accidentes
prima= prima_antiguedad + prima_distancia

if accidentes > 3:
    prima= float (0.0)
if accidentes <= 3:
    if accidentes == 1:
        prima = prima / 2
    if accidentes == 2:
        prima = prima / 3
    if accidentes == 3: 
        prima = prima / 4 
            
   



print ("Su prima anual es :" , prima , "€")
```
