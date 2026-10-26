import time 
# importamos la libreria time para iniciar el tiempo de ejecucion
import numpy as np 
# importamos numpy y le samos un alias.

# Definimos el tamaño del volumen de datos (8 millones de elementos)
N = 8000000

print(f" INICIO DE PRUEBA CON {N:,} ELEMENTOS ")

# 1. PRUEBA CON LISTA NATIVA DE PYTHON
# Crear la lista con numeros del 0 al N-1
#la lista debe estar en el rango de 0 a N-1, es decir, [0, 1, 2, ..., N-1] es decir desde cero hasta el final que 
# en este caso es representado siempre con N-1 que indica al final de la lista.

lista = list(range(N))
#range genera una secuencia de números desde 0 hasta N-1, y toma en cada ejecución el valor de N que es 8 millones
#un numero al azar dentro del rango de 0 a N-1, por eso al ejecutarlo siempre es un numero diferente y su resultado igual.

inicio_lista = time.perf_counter() 
#asi iniciamos el contador de tiempo para medir cuanto tarda en ejecutarse.
# Operacion matematica: multiplicar cada elemento por 2 usando list comprehension
lista_resultado = [x * 2 for x in lista]
fin_lista = time.perf_counter()
#asi finalizamos el contador de tiempo para medir cuanto tarda en ejecutarse.

tiempo_lista = fin_lista - inicio_lista
print(f"Tiempo con Listas: {tiempo_lista:.4f} segundos") 
#obtenemos el rsultado de la resta de tiempo final menos tiempo inicial.


# 2. PRUEBA CON ARRAY DE NUMPY
# Crear el array equivalente
array_np = np.arange(N)
#creamos el array, importamoa el alias de numpy que le asignamos al inicio
#  y usamos la funcion arange que genera un array con numeros del 0 al N-1,
#  es decir, [0, 1, 2, ..., N-1] es decir desde cero hasta el final.

inicio_array = time.perf_counter()
# Operacion matematica vectorizada: multiplicar todo el array de golpe
array_resultado = array_np * 2
fin_array = time.perf_counter()
#realizamos la contabilizacion del tiempo de ejecucion para medir cuanto tarda en ejecutarse, al igual que en la lista.


tiempo_array = fin_array - inicio_array
print(f"Tiempo con Arrays (NumPy): {tiempo_array:.4f} segundos") # resultado.

# 3. COMPARATIVA DE RENDIMIENTO
diferencia = tiempo_lista / tiempo_array
print(f"\nEl array fue aproximadamente {diferencia:.1f} veces mas rapido que la lista.")
#nos dimos cuenta de la diferencia de tiempo entre la lista y el array, y lo mostramos en pantalla.