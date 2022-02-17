# ```Descuento

#Un comerciante hace un descuento del 5 % en todas las compras con un importe comprendido entre 100 y 500 €, y del 8 % en los importes superiores.

#Escribir el algoritmo de cálculo del importe del descuento en una compra dada.


def descuento(precio):
    # Importe del descuento acordado sobre 'precio'
    if precio < 0:
        print("Error")
    elif precio >= 0:
        