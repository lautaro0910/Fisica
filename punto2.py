print("Calculadora de distancias")

# Elegir unidad
unidad = input("Unidad ('k'=km, 'a'=millas, 'm'=metros, 'z'=salir): ").lower()
if unidad == 'z':
    print("Terminando el programa.")
    exit()
elif unidad not in ['k', 'a', 'm']:
    print("Unidad no válida.")
    exit()

# Elegir tipo de métrica
tipo = input("Métrica ('t'=taxi, 'e'=euclídea, 'm'=máximo, 'z'=salir): ").lower()
if tipo == 'z':
    print("Terminando el programa.")
    exit()
elif tipo not in ['t', 'e', 'm']:
    print("Tipo no válido.")
    exit()

# Pedir coordenadas
x1 = float(input("Primer punto x: "))
y1 = float(input("Primer punto y: "))
x2 = float(input("Segundo punto x: "))
y2 = float(input("Segundo punto y: "))

# Calcular diferencias (sin usar abs)
dx = max(x1, x2) - min(x1, x2)
dy = max(y1, y2) - min(y1, y2)

# Calcular distancia
if tipo == 't':
    distancia = dx + dy
elif tipo == 'e':
    distancia = (dx**2 + dy**2) ** 0.5
else:  # máximo
    distancia = dx if dx > dy else dy

# Convertir a metros
if unidad == 'k':
    distancia *= 1000
elif unidad == 'a':
    distancia *= 1609.34

print(f"La distancia es: {distancia:.2f} metros")