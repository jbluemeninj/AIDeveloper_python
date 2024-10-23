import cv2

#Leer
img = cv2.imread('img/figuras_geometricas.png', 1)

#Extraer colores primarios
img_azul, img_verde, img_roja = cv2.split(img)

#Mostrar
cv2.imshow('Azul', img_azul)
cv2.imshow('Verde', img_verde)
cv2.imshow('Rojo', img_roja)

#Juntar y mostrar
img_junta = cv2.merge((img_azul, img_verde, img_roja))  
cv2.imshow('Junta', img_junta)

#Esperar
cv2.waitKey(0)

#Cerrar
cv2.destroyAllWindows()