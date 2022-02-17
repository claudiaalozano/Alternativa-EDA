# Descuento en los microprocesadores


# La empresa UNTEL hace descuentos por la compra al por mayor de sus microprocesadores. 
# Estos descuentos dependen de la cantidad de componentes pedidos y del cliente que los pide.

# El descuento concedido es de un 10 % si la cantidad de componentes pedidos se encuentra entre 10 000 y 20 000, 
# un 15 % si la cantidad se encuentra entre 20 001 y 40 000 y un 20 % para más de 40 000 componentes.

# Además, si el cliente es COMMAQ, el descuento se reduce un 2 %. Por último, BEL disfruta de un descuento mejorado en un 1 %.

# Establecer el algoritmo del cálculo del porcentaje de descuento concedido a un cliente dado para un pedido dado.

def microprocesadores(componentes, cliente, precio):
    if componentes >= 10000 and componentes <= 20000:
        descuento = 0.1
        preciofinal = precio - precio*descuento
        print(preciofinal)
    elif componentes >= 20001 and componentes <= 40000:
        descuento = 0.15
        print("precio final:", precio - precio*descuento )
    else:
        descuento = 0.2
        print("precio final:", precio - precio*descuento )
    
    if cliente == 1:
        #cliente = 1 significa que es COMMAQ; sino, cliente = 0 no COMMAQ
        descuento = 0.02
        print("precio final:", precio - precio*descuento )

microprocesadores(500000, 0, 35000)
