#Tabla de multiplicar de acuerdo a lo que ingrese el usuario

tabla = int(input("Ingrese el numero de la tabla de multiplicar: "))


def imprimir_tabla_multiplicar(tabla):
    for x in range(1, 13):
        resultado = tabla * x
        print(f"{tabla} x {x} = {resultado}")


imprimir_tabla_multiplicar(tabla)

