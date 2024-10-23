
from padre import Padre
from madre import Madre

class Hijo (Padre, Madre):

    nombre = "Juan"
    def saludar(self):
        print(f"Hola, soy {self.nombre} {Padre.apellido_paterno} {Madre.apellido_materna}. "
              f"Mis ojos son {Padre.color_ojos} y mi Cabello {Madre.color_cabello}" )



hijo = Hijo()

hijo.saludar()