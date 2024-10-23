import cv2

img1 = cv2.imread('../img/wikipedia0.jpg', 0)
img2 = cv2.imread('../img/wikipedia3.jpg', 0)

img = cv2.subtract(img1, img2)

cv2.imshow('Sustraccion imagenes', img)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()