import cv2
import os
import imutils

nombre_persona = 'vegeta'
clasficador_rostro = "../haarcascades/haarcascade_frontalface_default.xml"

data_path = '../../recursos/03/practica_01/data'
ruta_persona = data_path  + '/' + nombre_persona
##################################################
if not os.path.exists(ruta_persona):
    print('Carpeta creada: ', ruta_persona)
    os.makedirs(ruta_persona)
#################################################

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
carga_clasificador_rostro = cv2.CascadeClassifier(clasficador_rostro)
contador = 0

while True:
    ret, frame = cap.read()

    if ret == False:
        break
    frame  = imutils.resize(frame, width=320)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aux_frame = frame.copy()

    faces = carga_clasificador_rostro.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = aux_frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (720, 720), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(ruta_persona + '/rostro_{}.jpg'.format(contador), rostro)
        contador += 1

    cv2.imshow('frame', gray)

    k = cv2.waitKey(1)
    if k == 27 or contador >= 300:
        break


cap.release()

cv2.destroyAllWindows()