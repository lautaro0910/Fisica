def terminar():
    """Imprime mensaje de salida y finaliza el programa."""
    print("Terminando el programa.")
    exit()
print("Calculadora de distancias")
# Solicita al usuario que elija la unidad de medida
unidad = input("Unidad ('k'=km, 'a'=millas, 'm'=metros, 'z'=salir): ").lower()
if unidad == 'z':
    terminar()
elif unidad not in ['k', 'a', 'm']:
    print("Unidad no válida.")
    terminar()
# Solicita el tipo de métrica para el cálculo de distancia
tipo = input("Métrica ('t'=taxi, 'e'=euclídea, 'm'=máximo, 'z'=salir): ").lower()
if tipo == 'z':
    terminar()
elif tipo not in ['t', 'e', 'm']:
    print("Tipo no válido.")
    terminar()

# Solicita las coordenadas de los dos puntos
x1 = float(input("Primer punto x: "))
y1 = float(input("Primer punto y: "))
x2 = float(input("Segundo punto x: "))
y2 = float(input("Segundo punto y: "))

# Calcula la diferencia entre coordenadas (valor absoluto)
dx = abs(x1 - x2)
dy = abs(y1 - y2)

# Calcula la distancia según la métrica seleccionada
if tipo == 't':
    # Distancia tipo Taxi 
    distancia = dx + dy
elif tipo == 'e':
    # Distancia Euclídea
    distancia = (dx**2 + dy**2) ** 0.5
else:
    # Distancia maximo
    distancia = max(dx, dy)

# Convierte la distancia a metros según la unidad seleccionada
if unidad == 'k':
    distancia *= 1000          # Kilómetros a metros
elif unidad == 'a':
    distancia *= 1609.34       # Millas a metros

# Muestra el resultado con dos decimales
print(f"La distancia es: {distancia:.2f} metros")
