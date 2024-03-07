while True:
    print("Bienvenido al conversor de temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        resultado = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius equivalen a {resultado} grados Fahrenheit.")
    if opcion == '2':
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        resultado = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} grados Fahrenheit equivalen a {resultado} grados Celsius.")
    if opcion == '3':
        print("Gracias por usar el conversor de temperaturas. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 3.")

        