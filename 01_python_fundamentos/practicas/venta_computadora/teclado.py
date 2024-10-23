from dispositivo_entrada import DispostivosEntrada

class Teclado(DispostivosEntrada):

    contador_teclado = 0

    def __init__(self,marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)



    def __str__(self):
        return f"{self.id_teclado}, {super().__str__()}"