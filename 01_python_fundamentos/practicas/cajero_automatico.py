#Retiro y Deposito de cuenta en un cajero automatico

monto_cuenta = 10000.00
monto_retirado = 0.00
monto_depositado = 0.00

#Metodo mostrar saldo actual
def mostrar_saldo():
    print("Su saldo actual es: ", monto_cuenta)

#Metodo depositar
def depositar():
    global monto_cuenta
    global monto_depositado
    monto_depositar = float(input("Ingrese el monto a depositar: "))
    monto_cuenta += monto_depositar
    monto_depositado += monto_depositar
    mostrar_saldo()

#Metodo retirar
def retirar():
    global monto_cuenta
    global monto_retirado
    monto_retirar = float(input("Ingrese el monto a retirar: "))
    monto_cuenta -= monto_retirar
    monto_retirado  += monto_retirar
    mostrar_saldo()

#Interface de usuario
def menu():
    print("Bienvenido al cajero automatico")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Resumen de la cuenta")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def mostrar_resumen():
    print("Resumen de la cuenta")
    mostrar_saldo()
    print("Monto depositado: ", monto_depositado)
    print("Monto retirado: ", monto_retirado)

def retirar_depositar():
    opcion = menu()
    while opcion != 4:
        if opcion == 1:
            depositar()
        elif opcion == 2:
            retirar()
        elif opcion == 3:
            mostrar_resumen()
        else:
            print("Opcion invalida")
        opcion = menu()

retirar_depositar()