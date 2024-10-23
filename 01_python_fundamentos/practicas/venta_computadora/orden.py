from teclado import Teclado
from monitor import Monitor
from mouse import Mouse
from computadora import Computadora

class Orden:
    contador_ordenes = 0


    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'Orden: {self._id_orden}, Computadoras: {computadoras_str}'


if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Logitech')
    mouse1 = Mouse('USB', 'Logitech')
    monitor1 = Monitor('Samsung', 27)
    computadora1 = Computadora('PCU HP Intel Core I3', monitor1, teclado1, mouse1)

    teclado2 = Teclado('USB', 'Logitech')
    mouse2 = Mouse('USB', 'Logitech')
    monitor2 = Monitor('Samsung', 27)
    computadora2 = Computadora('PCU HP Intel Core I5', monitor2, teclado2, mouse2)

    teclado3 = Teclado('USB', 'Logitech')
    mouse3 = Mouse('USB', 'Logitech')
    monitor3 = Monitor('Samsung', 27)
    computadora3 = Computadora('PCU HP Intel Core I7', monitor3, teclado3, mouse3)

    computadoras = [computadora1, computadora2, computadora3]

    orden1 = Orden(computadoras)
    print(orden1)




