import cv2

#cargar img
img = cv2.imread('img/cuadro.jpg')

#Dimensiones img
alto, ancho, _ = img.shape
color = (0, 0, 255) #BGR
grosor = 2
cuadricula = 80

#Llenar
for x in range(0, ancho+1, cuadricula):
    img = cv2.line(img, (x, 0), (x, alto), color, grosor)
for y in range(0, alto+1, cuadricula):
    img = cv2.line(img, (0, y), (ancho, y), color, grosor)
    
#Mostrar
cv2.imshow('Imagen', img)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()