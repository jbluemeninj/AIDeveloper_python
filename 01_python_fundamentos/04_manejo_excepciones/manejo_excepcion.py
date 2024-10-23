#Manejar la excepcion de divisio entre cero
try:
    dividiendo = int(input("Ingresa el dividiendo: "))
    divisor = int(input("Ingresa el divisor: "))
    resultado = dividiendo / divisor
    print(resultado)
except  ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except  ValueError:
    print("Error: Ingresa valores numericos validos.")
except  Exception as e:
    print("Error:", e)
finally:
    print("Fin del programa")