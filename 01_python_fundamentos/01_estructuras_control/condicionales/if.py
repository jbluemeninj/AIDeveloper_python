#Crear un programa que diga la etapa de la vida que se encuentra una persona.
# La persona debe ingresar su año de naciomiento

anio_actual = 2024

def calcular_edad():
    anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
    return anio_actual - anio_nacimiento

def calcular_etapa():
    edad = calcular_edad()
    if edad < 12:
        etapa = "Niño"
    elif edad < 18:
        etapa = "Adolescente"
    elif edad < 60:
        etapa = "Adulto"
    else:
        etapa = "Adulto mayor"

    print(f"Su edad es {edad} y está en la etapa de {etapa}")

calcular_etapa()