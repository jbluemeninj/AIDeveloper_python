from dispositivo_entrada import DispostivosEntrada

class Mouse(DispostivosEntrada):

   contador_mouse = 0

   def __init__(self,marca, tipo_entrada):
        Mouse.contador_mouse += 1
        self.id_mouse = Mouse.contador_mouse
        super().__init__(marca, tipo_entrada)

   def __str__(self):
        return f"{self.id_mouse}, {super().__str__()}"



