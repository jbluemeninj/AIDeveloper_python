class Monitor:

    contador_monitor = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio

    def  __str__(self):
        return  f"{self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}"