numero = int(input('Ingresa un número entero positivo: '))

if numero <= 0:
    print("El número ingresado debe ser positivo. Intenta nuevamente.")
else:
    print("Tabla de multiplicar del: ",numero)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")