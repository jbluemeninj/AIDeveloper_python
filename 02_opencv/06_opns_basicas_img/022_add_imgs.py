import cv2 
  
img1 = cv2.imread('../img/cuadro.jpg', 1)
img2 = cv2.imread('../img/logo.jpg', 1)

alto, ancho, _ = img2.shape
roi = img1[0:alto, 0:ancho]

roi = cv2.bitwise_and(img2, roi)
img1[0:alto, 0:ancho ] = roi

cv2.imshow('Composicion imagenes', img1)

#Esperar
cv2.waitKey(0)

#Cerrar todas las ventanas
cv2.destroyAllWindows()