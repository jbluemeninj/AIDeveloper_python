import cv2 
  
img = cv2.imread('../img/cuadro.jpg', 1)

cv2.namedWindow('Cuadro', cv2.WINDOW_NORMAL)
cv2.moveWindow('Cuadro', 0, 0)
cv2.imshow('Cuadro', img)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()