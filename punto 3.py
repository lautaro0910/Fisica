import math

# Funciones de distancia
def taxi(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidea(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def maxima(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

# Comprobar si tres puntos están en la misma recta
def en_recta(p1, p2, p3):
    return (p3[0] - p1[0]) * (p2[1] - p1[1]) == (p3[1] - p1[1]) * (p2[0] - p1[0])

# Convertir unidades a metros
def a_metros(distancia, unidad):
    if unidad == 'k':
        return distancia * 1000
    elif unidad == 'a':
        return distancia * 1609.34
    return distancia

# Pedir punto al usuario
def pedir_punto():
    x, y = map(int, input("Dame el punto (x y): ").split())
    return (x, y)

def main():
    print("Calculadora de longitudes de caminos")

    while True:
        unidad = input("Dame las unidades (k/a/m o z para salir): ").lower()
        if unidad == 'z':
            print("Programa terminado")
            break
        if unidad not in ['k', 'a', 'm']:
            print("Opción no válida")
            continue

        metrica = input("Dame la métrica (t/e/m o z para salir): ").lower()
        if metrica == 'z':
            print("Programa terminado")
            break
        if metrica not in ['t', 'e', 'm']:
            print("Opción no válida")
            continue

        if metrica == 't':
            distancia = taxi
        elif metrica == 'e':
            distancia = euclidea
        else:
            distancia = maxima

        camino = []
        total = 0

        p1 = pedir_punto()
        if p1 == (0, 0):
            print("La longitud es 0 metros.")
            continue
        camino.append(p1)

        p2 = pedir_punto()
        if p2 == (0, 0):
            print("La longitud es 0 metros.")
            continue
        camino.append(p2)
        total += distancia(p1, p2)

        while True:
            p3 = pedir_punto()
            if p3 == (0, 0):
                break
            if len(camino) >= 2 and en_recta(camino[-2], camino[-1], p3):
                print("Punto no válido")
                continue
            total += distancia(camino[-1], p3)
            camino.append(p3)

        total_metros = int(round(a_metros(total, unidad)))
        print(f"La longitud es {total_metros} metros.")

# Ejecutar el programa directamente
main()
