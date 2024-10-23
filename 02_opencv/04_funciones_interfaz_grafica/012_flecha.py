import cv2

#Cargar img
img = cv2.imread("../img/cuadro.jpg")

#Crear una flecha
img = cv2.arrowedLine(img, (200, 100), (300, 150), (0, 0, 255), 5)

#Mostrar
cv2.imshow('Imagen', img)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()