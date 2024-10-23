#La idea es recuperar el user y password del archivo user.txt y hacer un login_access

def login_access():
    usuario = input("Ingresa tu usuario: ")
    clave = input("Ingresa tu password: ")
    with open("user.txt", "r") as archivo:
          #el formato obtenido es user:admin. Se debe sacar solo admin
           for linea in archivo:
             if linea.startswith("user:"):
                 user = linea.split(":")[1].strip()
             else:
                 password = linea.split(":")[1].strip()
           if  usuario == user and clave == password:
               print("Login correcto")
           else:
               print("Login incorrecto")

login_access()