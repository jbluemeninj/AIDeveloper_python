import cv2

#Leer
img = cv2.imread('../../recursos/02/img/itachi.jpg', 1)

#Pasamos de color a BN
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Mostrar
cv2.imshow('Itachi', img_byn)

#Esperar a que se presione una tecla para cerrar la ventana
cv2.waitKey(0)

# Cerra todas las ventanas
cv2.destroyAllWindows()