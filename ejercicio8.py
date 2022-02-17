#Prima anual





#A final de año, la empresa LA CAMPANA paga una prima anual a sus empleados camioneros.

#En principio, el conductor recibirá la prima anual completa si no ha tenido accidentes con una responsabilidad superior o igual al 20 % durante el año que termina. Si la responsabilidad es superior al 20 %, la empresa considera al conductor responsable del accidente. Si el conductor ha sido responsable de un accidente, solo recibe la mitad de la prima. Con dos accidentes, solo recibe un tercio. Con tres accidentes, la prima se reduce a un cuarto. Si supera los tres accidentes, la prima se anula.

#Esta prima es la suma de una prima de distancia y de una prima de antigüedad.

#La prima de distancia aumenta un céntimo por kilómetro recorrido durante el año, con un máximo de 400 €.

#La prima de antigüedad solo se paga una vez transcurridos cuatro años de antigüedad y es de 200 €. Luego aumenta 20,00 € por año adicional.

#Escribir el algoritmo de cálculo de la prima anual que se concederá a cada conductor.


prima_antiguedad = float (0.0) 
prima_distancia = float (0.0)
accidentes= input ("¿Cuantos accidentes ha tenido?:")
antiguedad = input ("¿Antiguedad del conductor?:")

if accidentes > 3:
    resultado= float (0.0)
if accidentes <= 3:
    if accidentes == 1:
        if antiguedad> 4:
            prima_antiguedad= prima_antiguedad
            prima = (prima_antiguedad + prima_distancia) / 2
    if not antiguedad < 4: 
        prima_antiguedad = prima_antiguedad + float(200.0) + (antiguedad - 4) * float(20.00)

def resultado():
    resutado= (prima_antiguedad + prima_distancia) / (accidentes + 1)

print (resultado)

