import math

def CalcularSuma(numero1,numero2):
    suma = numero1+numero2
    return suma

def CalcularResta(numero1,numero2):
    resta = numero1-numero2
    return resta

def CalcularMultiplicacion(numero1,numero2):
    multiplicacion = numero1*numero2
    return multiplicacion

def CalcularDivision(numero1,numero2):
    if numero2 == 0:
        return None
    division = numero1/numero2
    return division

def CalcularSeno(angulo):
    seno = math.sin(angulo)
    return seno

def CalcularCoseno(angulo):
    coseno = math.cos(angulo)
    return coseno

def CalcularTangente(angulo):
    tangente = math.tan(angulo)
    return tangente

def CalcularSecante(angulo):
    secante = 1/math.cos(angulo)
    return secante

def CalcularCosecante(angulo):
    cosecante = 1/math.sin(angulo)
    return cosecante

def CalcularCotangente(angulo):
    cotangente = 1/math.tan(angulo)
    return cotangente

continuar = "S"
while continuar == "S" or continuar == "s":
    print("Ingrese la operacion que desea hacer")
    print("")
    print("1. Operaciones basicas")
    print("2. Operaciones trigonometricas")
    resultado = int(input("Ingrese su opcion (1 o 2): "))
    if resultado == 1:
        print("Ingrese el tipo de operacion que desea hacer")
        print("")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        operacion = int(input("Ingrese su opcion (1, 2, 3 o 4): "))
        numero1 = float(input("Antes de continuar, Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        if operacion == 1:
            print("El resultado de la suma es: ", CalcularSuma(numero1,numero2))
        elif operacion == 2:
            print("El resultado de la resta es: ", CalcularResta(numero1,numero2))
        elif operacion == 3:
            print("El resultado de la multiplicacion es: ", CalcularMultiplicacion(numero1,numero2))
        elif operacion == 4:
            print("El resultado de la division es: ", CalcularDivision(numero1,numero2))
        else :
            print("Opcion no valida")
    if resultado == 2:
        print("Ingrese el tipo de operacion que desea hacer")
        print("")
        print("1. Seno")
        print("2. Coseno")
        print("3. Tangente")
        print("4. Secante")
        print("5. Cosecante")
        print("6. Cotangente")
        respuesta1 = int(input("Ingrese su opcion (1, 2, 3, 4, 5 o 6): "))
        angulo = float(input("Ingrese el angulo: "))
        if respuesta1 == 1:
            print("El resultado del seno es: ", CalcularSeno(angulo))
        elif respuesta1 == 2:
            print("El resultado del coseno es: ", CalcularCoseno(angulo))
        elif respuesta1 == 3:
            print("El resultado de la tangente es: ", CalcularTangente(angulo))
        elif respuesta1 == 4:
            print("El resultado de la secante es: ", CalcularSecante(angulo))
        elif respuesta1 == 5:
            print("El resultado de la cosecante es: ", CalcularCosecante(angulo))
        elif respuesta1 == 6:
            print("El resultado de la cotangente es: ", CalcularCotangente(angulo))
        else :
            print("Opcion no valida")

    continuar = input("Desea hacer otra operacion? (S/N): ")

print("¡Gracias por usar nuestra calculadora!")