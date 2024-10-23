import cv2

#Leer
img = cv2.imread('../../recursos/02/img/itachi.jpg', 1) # sintaxis (URL_IMG, {0: BN, 1:COLOR})

#Mostrar
cv2.imshow('Itachi', img)

#Esperar a que se presione una tecla para cerrar la ventana
cv2.waitKey(0)

#Cerrar todas las ventanas
cv2.destroyAllWindows()

