import sympy 

import numpy as np

# Definir la matriz aumentada del sistema de ecuaciones
A = np.array([[1, -2, 3, 4],
              [2, -4, 6, 8],
              [-1, 1, -1, -2]])

# Obtener la forma escalonada reducida de la matriz aumentada
rref, pivots = sympy.Matrix(A).rref()

# Contar el número de pivotes
num_pivots = len(pivots)

# Determinar el tipo de solución del sistema
if num_pivots == A.shape[1] - 1:
    print("El sistema tiene una solución única.")
elif num_pivots < A.shape[1] - 1:
    print("El sistema tiene infinitas soluciones.")
else:
    print("El sistema es inconsistente y no tiene solución.")