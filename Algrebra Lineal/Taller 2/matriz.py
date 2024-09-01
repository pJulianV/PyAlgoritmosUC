import numpy as np

# x, y, z
# A = np.array([[2, 1, -1],
#               [-1, 2, 3],
#               [3, -2, 4]])

# # Resultados
# B = np.array([3, 15, 8])

# # Numpy Algebra Lineal
# solution = np.linalg.solve(A, B)
# print(solution)


#Verificacion:
def sistema1():
    x = 1.1556
    y = 3.6444
    z = 2.95556
    
    
    eq1 = 2 * x + y - z
    eq2 = -x + 2 * y + 3 * z
    eq3 = 3 * x - 2 * y + 4 * z
    
    
    print(f"2*{x} + {y} - {z} = {eq1:.6f}")
    print(f"{2*x} + {y} - {z} = {eq1:.6f}")
    
    
    print(f"-{x} +  2 * {y} + 3 *{ z} = {eq2:.6f}")
    print(f"-{x} +  {2*y} + {3 * z} = {eq2:.6f}")
    
    print(f"3 * {x} - 2 * {y} + 4 * {z} = {eq3:.6f}")
    print(f"{3 * x} - {2 * y} + {4 * z} = {eq3:.6f}")
    
    print(eq1, eq2, eq3)
    # Exportar resultados a un archivo de texto
    with open("resultados.txt", "a") as f:
        f.write("Ecuaciones:\n")
        f.write(f"{eq1:.6f}\n")
        f.write(f"{eq2:.6f}\n")
        f.write(f"{eq3:.6f}\n")
        f.write("La solución es correcta.\n")
    

# print(sistema1)



def sistema3():

    x =	13.8918
    y =	6.5945
    z =	-7.4324
    w =	-3.0540

    # x	=13.89189189
    # y	=6.594594595
    # z	=-7.432432432
    # w	=-3.054054054


    eq1 = x + y + z + w 
    eq2 = 2* x - y + 3*z - 2*w 
    eq3 = -x + 4 *y + z + w 
    eq4 = 3* x - y + 2*z + 4*w 


    print(f"{x} + {y} + {z} + {w} = {eq1:.6f}")
    print(f"{x} + {y} + {z} + {w} = {eq1:.6f}")
    
    
    print(f"2* {x} - {y} + 3*{z} - 2*{w} = {eq2:.6f}")
    print(f"{2* x} - {y} + {3*z} - {2*w} = {eq2:.6f}")
    
    print(f"-{x} + 4 *{y} + {z} + {w} = {eq3:.6f}")
    print(f"-{x} + {4 *y} + {z} + {w} = {eq3:.6f}")

    print(f"3* {x} - {y} + 2*{z} + 4*{w}  = {eq4:.6f}")
    print(f"{3* x} - {y + 2*z} + {4*w}  = {eq4:.6f}")
    
    print(eq1, eq2, eq3, eq4)

sistema3()



# Sistema 1

# A = np.array([[2, -1, 3], [1, 2, -2], [-1, 3, 4]])
# b = np.array([3, 15, 8])

# A = np.array([[2, -1, 3, 3], [1, 2, -2, 15], [-1, 3, 4, 8]])


# Sistema 3

# A = np.array([[1, 1, 1, 1], [2, -1, 3, -2], [-1, 4, 1, 1], [3, -1, 2, 4]])
# b = np.array([10, 5, 2, 8])

# Sistema 4  


# A = np.array([[a, 1], [1, a-1]])
# b = np.array([3, 2])
 



# x = 1.155555556
# y = 3.644444444
# z = 2.955555556


# eq1 = 2 * x + y - z
# eq2 = -x + 2 * y + 3 * z
# eq3 = 3 * x - 2 * y + 4 * z