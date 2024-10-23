import cv2

#Cargar IMG
img = cv2.imread('img/cuadro.jpg')

#Crear ventana personalizado
cv2.namedWindow('Cuadro', cv2.WINDOW_NORMAL)
cv2.moveWindow('Cuadro', 0, 0)

#Mostrar
cv2.imshow('Cuadro', img)

#Esperar
cv2.waitKey(0)

#Cerrar ventanas
cv2.destroyAllWindows()