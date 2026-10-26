#PREGUNTA #1

#¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array,
# y a qué crees que se deben esas diferencias?

# RESPUESTA:
#  El array de NumPy es drásticamente más rápido que la lista nativa de Python (en tu prueba con 8 millones de elementos,
#  la diferencia suele ser de decenas de veces). Mientras que la lista de Python tarda una cantidad considerable 
# de segundos haciendo la compresión ([x * 2 for x in lista]), el array realiza la multiplicación de golpe en una fracción
#  de ese tiempo.

#Causa: Las listas nativas ejecutan un bucle explícito paso a paso en el intérprete de Python, evaluando cada elemento
#  de forma individual. En cambio, NumPy utiliza vectorización ejecutando operaciones
#  a nivel de código compilado en C, aprovechando optimizaciones de hardware sin el costo del intérprete de Python.

#PREGUNTA #2

#2. ¿Cómo influye la forma en que cada estructura almacena los datos en memoria en el rendimiento
#  obtenido durante la ejecución?

# RESPUESTA:
#Lista nativa de Python: No almacena los números directamente, sino punteros (referencias) a objetos enteros dispersos 
# por la memoria RAM. Esto genera un alto consumo de memoria y obliga al procesador a saltar de un lugar a otro
#  de la memoria para buscar cada valor (cache misses), ralentizando el proceso.

#Array de NumPy (ndarray): Almacena los datos en un bloque de memoria contigua (unidos uno al lado del otro) 
#y todos del mismo tipo de datos. Esto permite que el procesador (CPU) cargue los datos en la memoria caché 
#de manera ultra eficiente y utilice instrucciones de hardware especiales (como SIMD) para procesar bloques
#enteros de datos simultáneamente.

#PREGUNTA #3

#Si tuvieras que elegir una de estas estructuras para procesar grandes volúmenes de datos numéricos,
#  ¿cual seleccionarías y por qué?

#respuesta:

#Seleccionaría el array de NumPy.

# Porque ofrece una eficiencia de memoria superior (ocupa mucho menos espacio en RAM) y una velocidad de procesamiento
#  exponencialmente mayor gracias a la vectorización. Intentar procesar millones de datos numéricos con listas nativas
#  haría que los programas fueran lentos, pesados e ineficientes para cualquier aplicación real de ingeniería, 
# análisis de datos o inteligencia artificial.

