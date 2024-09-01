import numpy as np
from scipy.linalg import lu_factor, lu_solve

def calcular_soluciones(A, b):
    """
    Calcula las soluciones de las variables de la matriz A y el vector b.

    Parámetros:
    A (numpy.array): Matriz de coeficientes
    b (numpy.array): Vector de constantes

    Retorna:
    x (numpy.array): Solución del sistema de ecuaciones
    """
    # Factorización LU de la matriz A
    lu, piv = lu_factor(A)
    print("Factorización LU de la matriz A:")
    print("LU:", lu)
    print("Pivotes:", piv)

    # Resolución del sistema de ecuaciones
    x = lu_solve((lu, piv), b)
    print("Solución del sistema de ecuaciones:")
    print("x =", x)

    return x

def verificar_solucion(A, b, x):
    """
    Verifica si la solución x satisface el sistema de ecuaciones Ax = b.

    Parámetros:
    A (numpy.array): Matriz de coeficientes
    b (numpy.array): Vector de constantes
    x (numpy.array): Solución del sistema de ecuaciones

    Retorna:
    bool: True si la solución es correcta, False en caso contrario
    """
    print("Verificando la solución...")
    resultado = np.dot(A, x)
    print("Ax =", resultado)
    print("b =", b)
    return np.allclose(resultado, b)

def verificar_tipo_solucion(A, num_pivots):
    """
    Verifica el tipo de solución del sistema de ecuaciones.

    Parámetros:
    A (numpy.array): Matriz de coeficientes
    num_pivots (int): Número de pivotes en la factorización LU

    Retorna:
    str: Tipo de solución (única, infinitas, inconsistente)
    """
    if num_pivots == A.shape[1] - 1:
        return "El sistema tiene una solución única."
    elif num_pivots < A.shape[1] - 1:
        return "El sistema tiene infinitas soluciones."
    else:
        return "El sistema es inconsistente y no tiene solución."

# Ejemplo de uso
A = np.array([[2, -1, 3], [1, 2, -2], [-1, 3, 4]])
b = np.array([3, 15, 8])


print("Matriz A:")
print(A)
print("Vector b:")
print(b)

# Factorización LU de la matriz A
lu, piv = lu_factor(A)
num_pivots = np.sum(piv != np.arange(A.shape[1]))
print("Número de pivotes:", num_pivots)

# Calcular la solución
x = calcular_soluciones(A, b)

# Verificar la solución
if verificar_solucion(A, b, x):
    print("La solución es correcta.")
else:
    print("La solución es incorrecta.")

# Verificar el tipo de solución
print(verificar_tipo_solucion(A, num_pivots))