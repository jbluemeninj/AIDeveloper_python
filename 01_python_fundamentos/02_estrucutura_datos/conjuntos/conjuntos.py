"
SET (CONJUNTOS)
Características: No ordenados, mutables, no permiten duplicados.
Uso: Almacenar colecciones únicas de elementos.
"""
#Crear un set de vocales y ordenalos. Ademas imprime el penultimo elemento

vocales = {'a', 'e', 'i', 'o', 'u','u'}
vocales_ordenadas = sorted(vocales)
ultimo_elemento = vocales_ordenadas[-2]
print(vocales_ordenadas)
print(ultimo_elemento)