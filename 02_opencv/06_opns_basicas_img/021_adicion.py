import cv2 
  
img1 = cv2.imread('../img/espacio.jpg', 1)
img2 = cv2.imread('../img/tierra.jpg', 1)

img = cv2.addWeighted(img1, 0.4, img2, 0.8, 0)

cv2.imshow('Composicion imagenes', img)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()