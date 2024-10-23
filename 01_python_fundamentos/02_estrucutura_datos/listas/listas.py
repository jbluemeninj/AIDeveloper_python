"""
LIST
Características: Ordenadas, mutables, permiten duplicados.
Uso: Almacenar colecciones de elementos de cualquier tipo.
"""

#Crear una lista de frutas y muestralas en pantalla las frutas que comiencen con una letra que el usuario ponga

frutas = ["manzana", "banana", "naranja", "naranja","pera", "kiwi"] #False,1
frutas[3] = "sandia"
letra = input("Introduce una letra: ")

for fruta in frutas:
    if fruta.startswith(letra):
        print(fruta)