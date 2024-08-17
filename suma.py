
cantidad = int(input("Ingresa cantidad de numeros a sumar: "))
listNum = []
suma = 0
i = 0

while i <= cantidad:
    numeroIngresado = int(input(f"{i+1}. Ingresa numero: "))
    listNum.append(numeroIngresado)
    suma += numeroIngresado

    i += 1

print(' + '.join(map(str, listNum)))
print("="+ suma)