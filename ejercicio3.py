# ```Descuento

#Un comerciante hace un descuento del 5 % en todas las compras con un importe comprendido entre 100 y 500 €, y del 8 % en los importes superiores.

#Escribir el algoritmo de cálculo del importe del descuento en una compra dada.


def descuento(precio):
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

