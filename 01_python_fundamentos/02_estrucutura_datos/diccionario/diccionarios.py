"""
DICCIONARIO
Características: No ordenados, mutables, claves únicas.
Uso: Almacenar pares clave-valor, como configuraciones o datos asociados.
"""
#Crear un diccionario de libros con sus codigos. El usuario debe ingresar el codigo y
# debe mostrarle el titulo del libro

libros = {
    "BXL001" : "Python para principiantes",
    "BXL002" : "Java para principiantes",
    "BXL003" : "C# para principiantes"
}

def agregar_libro():
    codigo = input("Introduce el codigo del libro: ")
    titulo = input("Introduce el titulo del libro: ")
    libros[codigo] = titulo


def eliminar_libro():
    codigo = input("Introduce el codigo del libro: ")
    if codigo in libros:
        del libros[codigo]
        print("Libro eliminado")
    else:
        print("Libro no encontrado")

def buscar_libro():
    codigo = input("Introduce el codigo del libro: ")
    if codigo in libros:
        print(libros[codigo])
        #print(libros.get(codigo))
    else:
        print("Libro no encontrado")

def actualizar_libro():
    codigo = input("Introduce el codigo del libro: ")
    if codigo in libros:
        titulo = input("Introduce el titulo del libro: ")
        libros[codigo] = titulo
    else:
        print("Libro no encontrado")

def mostrar_libros():
    for codigo, titulo in libros.items():
        print(f"{codigo}: {titulo}")

def interfaz_usuario():
    while True:
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Mostrar libros")
        print("6. Salir")
        opcion = input("Introduce una opcion: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            eliminar_libro()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            actualizar_libro()
        elif opcion == "5":
            mostrar_libros()
        elif opcion == "6":
            break
        else:
            print("Opcion invalida")

interfaz_usuario()