"""
TUPLAS
Características: Ordenadas, inmutables, permiten duplicados.
Uso: Representar datos inmutables como coordenadas, fechas, etc
"""
#Crear una tabla de fechas

import datetime
fecha = datetime.datetime.now()
fecha_tupla = (fecha.year, fecha.month, fecha.day)
#fecha_tupla[0] = 2020
print(fecha_tupla)




