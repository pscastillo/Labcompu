print("Bienvenido a la experiencia, a continuacion las estaciones y rutas disponibles")
# Definir las estaciones y rutas
estaciones = {
    "51": "Estación Javier",
    "61": "Estación Trébol",
    "71": "Estación Don Bosco",
    "82": "Estación Plaza Municipal",
}

rutas = {
    1: ("51", "61", 39),
    2: ("51", "71", 18),
    3: ("71", "82", 23),
    4: ("61", "51", 8),
    5: ("82", "51", 42)
}

# Mostrar estaciones y rutas disponibles
print("Estaciones disponibles:")
for codigo, nombre in estaciones.items():
    print(f"Estación {codigo}: {nombre}")

print("\nRutas disponibles:")
for num, (inicio, fin, distancia) in rutas.items():
    print(f"Ruta {num}: Estación de partida: {estaciones[inicio]}, Estación de Destino: {estaciones[fin]}")

# Solicitar entrada del usuario y validar la ruta
while True:
    partida = input("Ingrese el código de la estación de partida: ")
    destino = input("Ingrese el código de la estación de destino: ")

    if partida in estaciones and destino in estaciones:
        for num, (inicio, fin, _) in rutas.items():
            if inicio == partida and fin == destino:
                ruta_valida = num
                print(f"Ruta válida seleccionada: Ruta {ruta_valida}")
                print(f"Estación de partida: {estaciones[inicio]}, Estación de destino: {estaciones[fin]}")
                break
        else:
            print("La ruta ingresada no existe. Por favor, elija otra ruta.")
            continue
        break
    else:
        print("Código de estación inválido. Intente nuevamente.")

# Solicitar información adicional del usuario
nombre = input("Ingrese su nombre: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break  # Salir del bucle si la entrada es un número entero válido
    except ValueError:
        print("Por favor, ingrese un número entero para la edad.")

while True:
    embarazo_respuesta = input("¿Está embarazada? (Sí/No): ").lower()
    if embarazo_respuesta in ["sí", "si", "Sí", "Si"]:
        embarazada = True
        break
    elif embarazo_respuesta in ["no", "No"]:
        embarazada = False
        break
    else:
        print("Respuesta inválida. Por favor, responda con 'Sí' o 'No'.")

# Calcular precio del boleto
precio_base = 1.50
precio_km_adicional = 0.25

distancia = rutas[ruta_valida][2]
precio_total = precio_base + max(0, distancia - 8) * precio_km_adicional

# Aplicar descuento para estudiantes
if 15 <= edad <= 25:
    precio_total *= 0.75  # 25% de descuento

# Mostrar información y precio del boleto
print("\nInformación del boleto:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
if embarazada:
    print("Estás embarazada, puedes entrar gratis.")
else:
    print(f"Ruta seleccionada: Ruta {ruta_valida}")
    print(f"Precio del boleto: Q{precio_total:.2f}")

# Calcular tiempo estimado de viaje
velocidad_bus = 20  # km/h

tiempo_viaje = distancia / velocidad_bus  # en horas

# Convertir tiempo a minutos para mostrarlo más amigablemente
tiempo_minutos = tiempo_viaje * 60  # en minutos

# Mostrar el tiempo estimado de viaje
print(f"Tiempo estimado de viaje: {tiempo_minutos:.2f} minutos")

# Registrar la venta del boleto y actualizar las ventas por ruta
ventas_por_ruta = {ruta: 0 for ruta in rutas}
ventas_por_ruta[ruta_valida] += 1

# Calcular total de boletos vendidos y ganancia total
total_boletos_vendidos = sum(ventas_por_ruta.values())
ganancia_total = total_boletos_vendidos * precio_total

# Mostrar la cantidad de boletos vendidos por ruta y totalizado, y la ganancia total
print("\nVentas:")
for ruta, cantidad in ventas_por_ruta.items():
    print(f"Ruta {ruta}: {cantidad} boletos vendidos")
print(f"Total de boletos vendidos: {total_boletos_vendidos}")
print(f"Ganancia total: Q{ganancia_total:.2f}")

while True:
    salir = input("¿Desea salir del programa? (Sí/No): ").lower()
    if salir in ["sí", "si"]:
        print("¡Gracias por usar el programa! Hasta luego.")
        break
    elif salir == "no":
        # Volver al inicio del programa para otro usuario
        break
    else:
        print("Respuesta inválida. Por favor, responda con 'Sí' o 'No'.")