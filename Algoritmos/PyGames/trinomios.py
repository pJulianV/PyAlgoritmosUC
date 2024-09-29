import math

def resolver_trinomio(a, b, c):
    """
    Resuelve un trinomio de la forma ax^2 + bx + c.

    Parámetros:
    a (float): Coeficiente de x^2
    b (float): Coeficiente de x
    c (float): Término constante

    Retorna:
    tuple: Raíces del trinomio
    """
    # Calcula el discriminante
    discriminante = b**2 - 4*a*c

    # Si el discriminante es negativo, no hay raíces reales
    if discriminante < 0:
        return "No hay raíces reales"

    # Calcula las raíces
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)

    return raiz1, raiz2

# Ejemplo de uso
a = float(input("Ingrese el coeficiente de x^2: "))
b = float(input("Ingrese el coeficiente de x: "))
c = float(input("Ingrese el término constante: "))

raices = resolver_trinomio(a, b, c)

if isinstance(raices, tuple):
    print("Las raíces del trinomio son:", raices)
else:
    print(raices)