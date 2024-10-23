import cv2

#Cargar imagen
img = cv2.imread('img/itachi.jpg')

#Obtener Caracteristicas de la image
tamanio = img.size
tipo = img.dtype
alto, ancho, canales = img.shape

print("Tamaño: " + str(tamanio) + " bytes")
print("Ancho: " + str(ancho) + " pixeles")
print("Alto: " + str(alto) + " pixeles")
print("Canales: " + str(canales))
print("Tipo: " + str(tipo) + " pixeles")
