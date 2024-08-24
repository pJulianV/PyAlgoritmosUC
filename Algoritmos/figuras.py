import math

def calcular_cubo(lado):
    volumen = lado ** 3
    area_superficial = 6 * (lado ** 2)
    return volumen, area_superficial

def calcular_esfera(radio):
    volumen = (4/3) * math.pi * (radio ** 3)
    area_superficial = 4 * math.pi * (radio ** 2)
    return volumen, area_superficial

def calcular_piramide(base, altura):
    volumen = (1/3) * (base ** 2) * altura
    area_superficial = base ** 2 + 2 * base * math.sqrt((base / 2) ** 2 + altura ** 2)
    return volumen, area_superficial

def calcular_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_rectangulo(base, altura):
    area = base * altura
    return area

def main():
    print("Seleccione la figura para calcular:")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Pirámide")
    print("4. Triángulo")
    print("5. Rectángulo")
    
    opcion = int(input("Ingrese el número de la figura: "))
    
    if opcion == 1:
        lado = float(input("Ingrese el lado del cubo: "))
        volumen, area_superficial = calcular_cubo(lado)
        print(f"Volumen del cubo: {volumen:.2f}")
        print(f"Área superficial del cubo: {area_superficial:.2f}")
        
    elif opcion == 2:
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen, area_superficial = calcular_esfera(radio)
        print(f"Volumen de la esfera: {volumen:.2f}")
        print(f"Área superficial de la esfera: {area_superficial:.2f}")
        
    elif opcion == 3:
        base = float(input("Ingrese la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        volumen, area_superficial = calcular_piramide(base, altura)
        print(f"Volumen de la pirámide: {volumen:.2f}")
        print(f"Área superficial de la pirámide: {area_superficial:.2f}")
        
    elif opcion == 4:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_triangulo(base, altura)
        print(f"Área del triángulo: {area:.2f}")
        
    elif opcion == 5:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_rectangulo(base, altura)
        print(f"Área del rectángulo: {area:.2f}")
        
    else:
        print("Opción no válida. Por favor, seleccione una figura correcta.")

if __name__ == "__main__":
    main()