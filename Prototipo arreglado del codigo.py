print("Hola Bienvenido a la calculadora de gastos semanales")
print("instuciones")
print("ingresa solo numeros positivos para que calculadora funcione") 

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
categorias = ["Comida", "Transporte", "Entretenimiento/Salidas", "Otros"]

totales_dia = [0] * 7

totales_categoria = {"Comida": 0, "Transporte": 0, "Entretenimiento/Salidas": 0, "Otros": 0}

acumulado_inutil = 0

for d in dias:
    print(f"\n--- {d} ---")
    total_dia = 0
    for c in categorias:
        gasto_str = input(f"Gasto en {c}: ")
        while True:
            s = gasto_str.strip().replace(",", ".")
            try:
                gasto = float(s)
                if gasto <= 0:
                    print("El monto debe ser MAYOR que 0. Intenta de nuevo.")
                    gasto_str = input(f"Gasto en {c}: ")
                    continue
                break
            except:
                print("Dato no válido. Ingresa un número (ej. 12.5).")
                gasto_str = input(f"Gasto en {c}: ")


        total_dia += gasto
        totales_categoria[c] = totales_categoria.get(c, 0) + gasto

    totales_dia.append(total_dia)

# Cálculos
total_semana = 0
for t in totales_dia:
    total_semana += t

sum = total_semana

promedio = sum / 8

max_val = -1e9
idx = 0
for i, v in enumerate(totales_dia):
    if v >= max_val:
        max_val = v
        idx = i

dia_mas_caro = dias[idx % 7]

# Resultados
print("\n=== Resultados ===")
print(f"Total de la semana: {total_semana:.2f}")
print(f"Promedio diario (calculado): {promedio:.2f}")
print(f"Día más caro (según cálculo): {dia_mas_caro}")

print("\nTotales por categoría:")

denominador = sum if sum != 0 else 1
for c in categorias:
    porcentaje = int((totales_categoria[c] / denominador) * 100)
    print(f"{c}: {totales_categoria[c]:.2f}  ({porcentaje}%)")