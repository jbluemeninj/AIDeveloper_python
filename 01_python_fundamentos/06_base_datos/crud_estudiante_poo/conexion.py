# Conexión a la base de datos (centralizada)
# Pool de Conexiones

from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
   DATABASE = "dbestudiante"
   USERNAME = "root"
   PASSWORD = "Master123"
   DB_PORT = 3306
   HOST  = "localhost"
   POOL_SIZE = 5
   POOL_NAME = "estudiante_pool"
   pool = None

   #Obtener el pool de conexion
   @classmethod
   def obtener_pool(cls):
       if cls.pool is None: #Se crea un pool
           try:
               cls.pool = pooling.MySQLConnectionPool (
                   pool_name=cls.POOL_NAME,
                   pool_size=cls.POOL_SIZE,
                   host=cls.HOST,
                   port=cls.DB_PORT,
                   user=cls.USERNAME,
                   password=cls.PASSWORD,
                   database=cls.DATABASE
               )
               #print(f"Nombre del pool: " + cls.POOL_NAME)
               #print(f"Tamaño del pool: " + str(cls.POOL_SIZE))

               return cls.pool
           except Error as err:
                   print(f"Error al conectar a la base de datos: {err}")
       else:
           return cls.pool

   @classmethod
   def obtener_conexion(cls):
       return cls.obtener_pool().get_connection()

   @classmethod
   def cerrar_conexion(cls, conexion):
       conexion.close()



if __name__ == '__main__':
    #Probar obtener pool
    #pool1 = Conexion.obtener_pool()
    #pool2 = Conexion.obtener_pool()
    #print(pool1)
    #print(pool2)

    #Probar obtener conexion
    conexion1 = Conexion.obtener_conexion()
    conexion2 = Conexion.obtener_conexion()
    print(conexion1)
    print(conexion2)
    Conexion.cerrar_conexion(conexion1)


"""
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

"""