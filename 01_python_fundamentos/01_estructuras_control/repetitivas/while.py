#1. Vamos a simular un login. Numero de intentos 3
#2. Escribir un programa que solicite ingresar la nota de 5 alumnos,
# el programa debe informar de cuantos han aprobado y cuantos han suspendido.

#BD
nota_aprobatoria = 12
alumnos = 5
aprobados = 0
suspendidos = 0

for i in range(alumnos):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    if nota >= nota_aprobatoria:
        aprobados += 1
    else:
        suspendidos += 1

print(f"Aprobados: {aprobados}, Suspendidos: {suspendidos}")



