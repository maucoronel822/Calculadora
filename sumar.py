class Suma():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        suma = n1 + n2
        return suma 
    
n1 = int(input("n1: "))
n2 = int(input("n2: "))

operacion = Suma(n1,n2)

resultado = operacion.suma()
print(f"La suma es: {resultado}")