class SumaAvanzada():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.numlist = [self.n1, self.n2]

    def agregarNumero(self):
        num = int(input("Ingresa un número a agregar: "))
        self.numlist.append(num)

    def sumar(self):
        resultado = 0
        for i in self.numlist:
            resultado += i
        return resultado
    
'''suma = SumaAvanzada(5,3)
agregar = True
while agregar:
    suma.agregarNumero()
    print(f"La lista de números es: {suma.numlist}")
    respuesta = input("¿Deseas agregar otro número? (s/n): ")
    if respuesta == "n":
        agregar = False

resultado = suma.sumar()
print(f"La suma de los {len(suma.numlist)} números es: {resultado}")'''        