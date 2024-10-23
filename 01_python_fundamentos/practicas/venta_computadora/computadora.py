from teclado import Teclado
from monitor import Monitor
from mouse import Mouse

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, mouse):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.mouse = mouse


    def __str__(self):
       return f'''
        {self.nombre} : {self.id_computadora}
           Monitor : {self.monitor}
           Teclado : {self.teclado}
           Mouse : {self.mouse}
      '''

if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Logitech')
    mouse1 = Mouse('USB', 'Logitech')
    monitor1 = Monitor('Samsung', 27)
    computadora1 = Computadora('PCU HP Intel Core I3', monitor1, teclado1, mouse1)
    print(computadora1)

    teclado2 = Teclado('USB', 'Logitech')
    mouse2 = Mouse('USB', 'Logitech')
    monitor2 = Monitor('Samsung', 27)
    computadora2 = Computadora('PCU HP Intel Core I5', monitor2, teclado2, mouse2)
    print(computadora2)

    teclado3 = Teclado('USB', 'Logitech')
    mouse3 = Mouse('USB', 'Logitech')
    monitor3 = Monitor('Samsung', 27)
    computadora3 = Computadora('PCU HP Intel Core I7', monitor3, teclado3, mouse3)
    print(computadora3)

