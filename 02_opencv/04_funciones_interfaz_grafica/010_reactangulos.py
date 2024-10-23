import cv2

#cargar img
img = cv2.imread('../img/cuadro.jpg')

color = (0, 0, 255) #BGR
grosor = 2
cara_x1, cara_x2 = 300, 550
cara_y1, cara_y2 = 20, 220

#Rectangulo
img = cv2.rectangle(img, (cara_x1, cara_y1), (cara_x2, cara_y2), color, grosor)

#Mostrar 
cv2.imshow('cuadro', img)

#Detener 
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()