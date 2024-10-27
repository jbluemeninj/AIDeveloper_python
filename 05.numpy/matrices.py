import numpy as np

# Crear un array de 100 números aleatorios entre 0 y 1
array_aleatorio = np.random.rand(100)

# Calcular la media y la desviación estándar
media = np.mean(array_aleatorio)
desviacion_estandar = np.std(array_aleatorio)

# Encontrar el valor máximo y mínimo
valor_maximo = np.max(array_aleatorio)
valor_minimo = np.min(array_aleatorio)

# Ordenar el array
array_ordenado = np.sort(array_aleatorio)

# Crear una nueva matriz de ceros
matriz_ceros = np.zeros_like(array_aleatorio)

# Multiplicar elemento a elemento y asignar el resultado
array_aleatorio *= matriz_ceros

print("Array original:", array_aleatorio)
print("Media:", media)
print("Desviación estándar:", desviacion_estandar)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Array ordenado:", array_ordenado)