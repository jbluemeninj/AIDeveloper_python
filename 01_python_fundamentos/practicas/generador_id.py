#La idea es generar un ID de un empleado.
# De su nombre las dos primeras letras
# De su apellido las dos primeras letras
# De su año de naciomiento los dos ultimos
# y generar cuatro digitos aletorios
import random

nombre = input("Ingrese el nombre del empleado: ")
apellido = input("Ingrese el apellido del empleado: ")
anio_nacimiento = input("Ingrese el año de nacimiento del empleado: ")
id = nombre[:2] + apellido[:2] + anio_nacimiento[-2:] + str(random.randint(1000, 9999))
print("El ID del empleado es:", id)