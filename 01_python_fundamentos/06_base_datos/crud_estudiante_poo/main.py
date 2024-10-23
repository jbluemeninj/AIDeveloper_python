from estudiante_dao import EstudianteDAO
from estudiante import Estudiante



# Metodo menu
def menu():
    print("1. Mostrar estudiantes")
    print("2. Agregar estudiante")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Actualizar estudiante")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


def interface_usuario():
    while True:
        opcion = menu()
        if opcion == "1":
            EstudianteDAO.mostrar_estudiantes()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            telefono = input("Ingrese el telefono del estudiante: ")
            email = input("Ingrese el email del estudiante: ")
            estudiante = Estudiante(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            EstudianteDAO.registrar_estudiante(estudiante)
        elif opcion == "3":
            codigo = input("Ingrese el código del estudiante: ")
            estudiante = EstudianteDAO.buscar_estudiante(codigo)
            if estudiante:
                print(estudiante)
            else:
                print("No se encontró ningún estudiante con ese código.")
        elif opcion == "4":
            codigo = input("Ingrese el código del estudiante a eliminar: ")
            EstudianteDAO.eliminar_estudiante(codigo)
        elif opcion == "5":
            codigo = input("Ingrese el código del estudiante a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            telefono = input("Ingrese el nuevo telefono: ")
            email = input("Ingrese el nuevo email: ")
            estudiante = Estudiante(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            EstudianteDAO.actualizar_estudiante(estudiante, codigo)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

interface_usuario()