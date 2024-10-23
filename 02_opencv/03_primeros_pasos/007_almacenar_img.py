import cv2
import numpy

ancho = alto = 300

img_negro = numpy.ones((alto, ancho), numpy.uint8) * 255
for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or y%50 == 0:
            img_negro[y, x] = 0
            

#Guardamos la imagen
cv2.imwrite('img/rejilla_negro.png', img_negro)
print('Imagen creada')

