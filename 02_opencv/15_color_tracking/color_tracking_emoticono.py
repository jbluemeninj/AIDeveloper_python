import cv2
import numpy as np
from os import listdir
from math import ceil

matiz_objetivo = 0
rango = 5

color = (0, 255, 255)
grosor = 2

carpeta_emoticono = '../img/secuencia_emoticono/'
lista_emoticonos = []

for archivo in listdir(carpeta_emoticono):
    lista_emoticonos.append(cv2.imread(carpeta_emoticono+archivo))

numero_imagenes = len(lista_emoticonos)
indice_emoticono = ceil(numero_imagenes/2)

def selecciona_color(evento, x, y, flags, frame):
    global matiz_objetivo

    if evento == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        matiz_objetivo = h[y, x]
        
def selecciona_rango(valor):
    global rango
    rango = valor

def filtra_matiz(frame):
    frame_suavizado = cv2.blur(frame, (10, 10))
    hsv = cv2.cvtColor(frame_suavizado, cv2.COLOR_BGR2HSV)
    color_inferior = np.array([matiz_objetivo - rango,150,0])
    color_superior = np.array([matiz_objetivo + rango,255,255])
    mascara = cv2.inRange(hsv, color_inferior, color_superior)

    #mascara = cv2.dilate(mascara, None, iterations=4)
    #mascara = cv2.erode(mascara, None, iterations=2)

    contornos, _ = cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    return contornos

cv2.namedWindow('webcam')
cv2.createTrackbar('Rango', 'webcam', 5, 30, selecciona_rango)

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print("No es posible abrir la cámara")
    exit()

ancho_frame = camara.get(cv2.CAP_PROP_FRAME_WIDTH)
ancho_zona = ancho_frame/numero_imagenes

while True:
    ret, frame = camara.read()
    if not ret:
        print("No es posible obtener la imagen")
        break

    contornos = filtra_matiz(frame)
    if len(contornos) > 0:
        contorno_max = max(contornos, key = cv2.contourArea)
        
        (x, y), radio = cv2.minEnclosingCircle(contorno_max)
        centro = (int (x), int (y))
        radio = int (radio)
        cv2.circle (frame, centro, radio, color, grosor)
        
        indice_emoticono = numero_imagenes - ceil(x/ancho_zona)

    cv2.imshow('webcam', frame)
    cv2.imshow('Emoticono', lista_emoticonos[indice_emoticono])
    cv2.setMouseCallback('webcam', selecciona_color, frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
