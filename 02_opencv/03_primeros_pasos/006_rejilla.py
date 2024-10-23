import cv2
import numpy as np


ancho = alto = 300


#Rejilla Negro
img_negro = np.ones((alto, ancho), np.uint8) * 255
for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or y%50 == 0:
            img_negro[y, x] = 0
            


#Rejilla Azul
img_azul = np.ones((alto, ancho, 3), np.uint8) * 255 # 3 = BGR

for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or y%50 == 0:
            img_azul[y, x] = (255, 0, 0)


#Mostrar
cv2.imshow('Imagen_negro', img_negro)
cv2.imshow('Imagen_azul', img_azul)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()