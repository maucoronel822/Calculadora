import sumar as sum
import resta as res
import multiplicacion as mult
import dividir as div
import suma_avanzada as sumav

opcion = True

while opcion:
    print("======================")
    print("Bienvenido a Calculadora OpenSource")
    print("======================")
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma Avanzada")
    print("6. Salir")
    print("======================")
    opcion = int(input("Opción: "))
    if opcion == 6:
        print("xxxxxxxxxxxxxxxxxxxxxxxx")
        print("Gracias por usar la calculadora OpenSource")
        print("xxxxxxxxxxxxxxxxxxxxxxxx")
        break

    #En este caso, se solicitan los números a calcular
    print("Ingresa los números a calcular:")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    print("xxxxxxxxxxxxxxxxxxxxxxxx")

    if opcion == 1:
        operacion = sum.Suma(n1,n2)
        resultado = operacion.suma()
        print(f"La suma es: {resultado}")
    elif opcion == 2:
        operacion = res.Resta(n1,n2)
        resultado = operacion.resta()
        print(f"La resta es: {resultado}")
    elif opcion == 3:
        operacion = mult.Multiplicar(n1,n2)
        resultado = operacion.multiplicar()
        print(f"La multiplicación es: {resultado}")
    elif opcion == 4:
        operacion = div.Division(n1,n2)
        resultado = operacion.dividir()
        print(f"La división es: {resultado}")
    elif opcion == 5:
        suma = sumav.SumaAvanzada(n1,n2)
        agregar = True
        while agregar:
            suma.agregarNumero()
            print(f"La lista de números es: {suma.numlist}")
            respuesta = input("¿Deseas agregar otro número? (s/n): ")
            if respuesta == "n":
                agregar = False
        resultado = suma.sumar()
        print("xxxxxxxxxxxxxxxxxxxxxxxx")
        print(f"La suma de los {len(suma.numlist)} números es: {resultado}")
    else:
        print("Opción no válida")
    print("xxxxxxxxxxxxxxxxxxxxxxxx")