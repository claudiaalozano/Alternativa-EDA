niños=8
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
    