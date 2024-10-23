#Crear un programa que al selecionar un numero del 1 al 7. Te diga el dia.

def dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo"
    }
    return dias.get(numero, "Numero invalido")

numero_semana = int(input("Ingrese un numero del 1 al 7: "))
print(dia_semana(numero_semana))