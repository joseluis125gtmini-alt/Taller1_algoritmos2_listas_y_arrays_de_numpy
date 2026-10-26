import numpy as np

# 1. INICIALIZACIÓN: Colección de notas de los estudiantes (escala de 0 a 100)
# Supongamos los resultados de 10 estudiantes
notas = np.array([40, 79, 53, 88, 32, 71, 83, 47, 91, 48])

print(f"--- FASE 1: DATOS ORIGINALES ---")
print(f"Notas iniciales: {notas}")

# 2. CÁLCULOS BÁSICOS (Recorrido y procesamiento inicial)
promedio_inicial = np.mean(notas)
nota_max = np.max(notas)
nota_min = np.min(notas)

print(f"\n--- FASE 2: ESTADÍSTICAS INICIALES ---")
print(f"Promedio del grupo: {promedio_inicial:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

# 3. APLICACIÓN DE MODIFICACIONES BAJO CRITERIOS
# Criterio: Si la nota es menor a 50, se aplica un incentivo académico de +10 puntos.
# Usamos np.where para evaluar la condición de manera eficiente en todo el array.
notas_ajustadas = np.where(notas < 50, notas + 10, notas)

# Asegurar que ninguna nota supere el límite máximo permitido (100)
notas_ajustadas = np.clip(notas_ajustadas, 0, 100)

print(f"\n--- FASE 3: APLICACIÓN DE CRITERIOS (Incentivo aplicado) ---")
print(f"Notas ajustadas: {notas_ajustadas}")

# 4. CONSOLIDACIÓN DE RESULTADOS
promedio_final = np.mean(notas_ajustadas)

print(f"\n--- FASE 4: CONSOLIDACIÓN FINAL ---")
print(f"Promedio final del grupo tras ajustes: {promedio_final:.2f}")
print(f"Diferencia en el promedio: {promedio_final - promedio_inicial:+.2f} puntos")