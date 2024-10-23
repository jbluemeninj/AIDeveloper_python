import numpy
import cv2
import cv2

#Matriz de ceros de 5 x 5
# matriz = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
# ]

#img = numpy.array(matriz)

#Generamos imagen en blanco y negro 5 * 5
# img = numpy.zeros((5,5), numpy.uint8)
# print(img)

ancho = alto = 300

#Color Negro
img_negro = numpy.zeros((alto, ancho), numpy.uint8)

#Color blanco
img_blanco = numpy.ones((alto, ancho), numpy.uint8) * 255

#Color Azul
img_azul = numpy.ones((alto, ancho, 3), numpy.uint8) * 255 # 3 = BGR
# print(img_azul)
img_azul[:] = (255,0,0)

#Color Verde
img_verde = numpy.ones((alto, ancho, 3), numpy.uint8) * 255 # 3 = BGR
img_verde[:] = (0, 255, 0)

#Color Rojo
img_rojo = numpy.ones((alto, ancho, 3), numpy.uint8) * 255 # 3 = BGR
img_rojo[:] = (0, 0, 255)

#Mostrar
# cv2.imshow('IMAGEN_NEGRO', img_negro)
# cv2.imshow('IMAGEN_BLANCO', img_blanco)
cv2.imshow('IMAGEN_AZUL', img_azul)
cv2.imshow('IMAGEN_VERDE', img_verde)
cv2.imshow('IMAGEN_ROJO', img_rojo)


#Esperar
cv2.waitKey(0)

#Destruir
cv2.destroyAllWindows()



