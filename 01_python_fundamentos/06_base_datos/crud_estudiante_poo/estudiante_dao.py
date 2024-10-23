#Metodo para mostrar estudiantes
import mysql.connector
from conexion import Conexion
from estudiante import Estudiante

class EstudianteDAO:
    #Obtener estudiantes

    @classmethod
    def obtener_estudiante(cls):
         try:
            with Conexion.obtener_conexion() as db:
              mi_cursor = db.cursor()
              mi_cursor.execute("SELECT * FROM estudiante")
              registros = mi_cursor.fetchall()
              estudiantes = []
              for registro in registros:
                 estudiante = Estudiante(registro[0], registro[1],registro[2],registro[3],registro[4])
                 estudiantes.append(estudiante)
              return estudiantes
         except mysql.connector.Error as err:
            print(f"Error al mostrar estudiantes: {err}")

    @classmethod
    #Imprimir estudiantes
    def mostrar_estudiantes(cls):
        estudiantes = cls.obtener_estudiante()
        for estudiante in estudiantes:
            print(estudiante)

    @classmethod
    #Registrar estudiante
    def registrar_estudiante(cls,estudiante):
        try:
            with Conexion.obtener_conexion() as db:
                mi_cursor = db.cursor()
                mi_cursor.execute(
                    "INSERT INTO estudiante (fist_name,last_name,telefono,email) VALUES (%s, %s, %s, %s)",
                    (estudiante.nombre, estudiante.apellido, estudiante.telefono, estudiante.email))
                db.commit()
                print("Estudiante registrado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al registrar estudiante: {err}")

    #Actualizar estudiante
    @classmethod
    def actualizar_estudiante(cls,estudiante, codigo):
        try:
            with Conexion.obtener_conexion() as db:

                registro = cls.buscar_estudiante(codigo)

                if registro:
                   mi_cursor = db.cursor()
                   mi_cursor.execute(
                    "UPDATE estudiante SET fist_name = %s, last_name = %s, telefono = %s, email = %s WHERE id_estudiante = %s",
                    (estudiante.nombre, estudiante.apellido, estudiante.telefono, estudiante.email, codigo))
                   db.commit()
                   print("Estudiante actualizado exitosamente.")
                else :
                    print("No se encontró ningún estudiante con ese código.")

        except mysql.connector.Error as err:
            print(f"Error al actualizar estudiante: {err}")

    @classmethod
    def buscar_estudiante(cls,codigo):
        try:
            with Conexion.obtener_conexion() as db:
                mi_cursor = db.cursor()
                mi_cursor.execute("SELECT * FROM estudiante WHERE id_estudiante = %s", (codigo,))
                registro = mi_cursor.fetchone()
                if registro:
                    estudiante = Estudiante(registro[0], registro[1], registro[2], registro[3], registro[4])
                    return estudiante
                else:
                    return None
        except mysql.connector.Error as err:
            print(f"Error al buscar estudiante: {err}")

    #Eliminar estudiante
    @classmethod
    def eliminar_estudiante(cls,codigo):
        try:
            if cls.buscar_estudiante(codigo):
                with Conexion.obtener_conexion() as db:
                    mi_cursor = db.cursor()
                    mi_cursor.execute("DELETE FROM estudiante WHERE id_estudiante = %s", (codigo, ))
                    db.commit()
                    print("Estudiante eliminado exitosamente.")
            else:
                print("No se encontró ningún estudiante con ese código.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar estudiante: {err}")




