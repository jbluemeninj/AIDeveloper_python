import mysql.connector

#Conexión a la base de datos
# Conexión a la base de datos (centralizada)
def conectar_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Master123",
            database="dbestudiante"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")

#Metodo para mostrar estudiantes
def mostrar_estudiantes():
 try:
    with conectar_db() as db:
      mi_cursor = db.cursor()
      mi_cursor.execute("SELECT * FROM estudiante")
      resultado = mi_cursor.fetchall()
      for estudiante in resultado:
         print(estudiante)
 except mysql.connector.Error as err:
    print(f"Error al mostrar estudiantes: {err}")

#Metodo agregar estudiante
def agregar_estudiante():
  try:
    with conectar_db() as db:
     cursor = db.cursor()
     sql = "INSERT INTO estudiante (fist_name,last_name,telefono,email) VALUES (%s, %s, %s,%s)"
     nombre = input("Ingrese el nombre: ")
     apellido = input("Ingrese el apellido: ")
     telefono = input("Ingrese el telefono: ")
     email = input("Ingrese el email: ")
     valores = (nombre, apellido, telefono, email)
     cursor.execute(sql, valores)
     db.commit()
  except mysql.connector.Error as err:
    print(f"Error al agregar estudiante: {err}")

#Buscar a un estudiante por su codigo
def buscar_estudiante():
 try:
    with conectar_db() as db:
     cursor = db.cursor()
     sql = "SELECT * FROM estudiante WHERE id_estudiante = %s"
     codigo = input("Ingrese el código del estudiante: ")
     valores = (codigo,)
     cursor.execute(sql, valores)
     resultado = cursor.fetchone()
     if resultado:
        print(resultado)
     else:
        print("No se encontró ningún estudiante con ese código.")
 except mysql.connector.Error as err:
     print(f"Error al buscar estudiante: {err}")

#Metodo Eliminar estudiante
def eliminar_estudiante():
   try:
    with conectar_db() as db:
     cursor = db.cursor()
     sql = "DELETE FROM estudiante WHERE id_estudiante = %s"
     codigo = input("Ingrese el código del estudiante a eliminar: ")
     valores = (codigo,)
     cursor.execute(sql, valores)
     db.commit()
   except mysql.connector.Error as err:
    print(f"Error al eliminar estudiante: {err}")

#Metodo actutalizar estudiante
def actualizar_estudiante():
    with  conectar_db() as db:
     cursor = db.cursor()
     sql = "UPDATE estudiante SET fist_name = %s, last_name = %s, telefono = %s, email = %s WHERE id_estudiante = %s"
     codigo = input("Ingrese el código del estudiante a actualizar: ")
     nombre = input("Ingrese el nuevo nombre: ")
     apellido = input("Ingrese el nuevo apellido: ")
     telefono = input("Ingrese el nuevo telefono: ")
     email = input("Ingrese el nuevo email: ")
     valores = (nombre, apellido, telefono, email, codigo)
     cursor.execute(sql, valores)
     db.commit()

#Metodo menu
def menu():
    print("1. Mostrar estudiantes")
    print("2. Agregar estudiante")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Actualizar estudiante")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

#Interfaz usuario
def main():
    while True:
        opcion = menu()
        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            agregar_estudiante()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            actualizar_estudiante()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")


if __name__ == '__main__':
    main()


