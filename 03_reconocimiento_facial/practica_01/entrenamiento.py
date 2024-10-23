import cv2
import numpy as np
import os

data_path = '../../recursos/03/practica_01/data'
lista_personas = os.listdir(data_path)
labels = []
face_data = []

label = 0

for nombre_carpeta in lista_personas:
    ruta_persona = data_path + '/' + nombre_carpeta
    #print('Leyendo las imagenes')

    for nombre_archivo in os.listdir(ruta_persona):
        #print('Rostros: ', nombre_carpeta + '/' + nombre_archivo)
        labels.append(label)

        face_data .append(cv2.imread(ruta_persona + '/' + nombre_archivo, 0))
        imagen = cv2.imread(ruta_persona + '/' + nombre_archivo, 0)
        ###################
        #cv2.imshow('Imagen', imagen)
        #cv2.waitKey(10)
        ###################

    label = label + 1

#cv2.destroyAllWindows()
######################################
#print('labels = ', labels)
#print('Cantidad de etiquetas 0: ', np.count_nonzero(np.array(labels) == 0))

#Entramiento

""""""
#face_recognizer = cv2.face.EigenFaceRecognizer.create()
face_recognizer = cv2.face.LBPHFaceRecognizer.create()
print('Entrenando...')
face_recognizer.train(face_data, np.array(labels))

#face_recognizer.write('modeloEigenFace2024.xml')
face_recognizer.write('modeloLBPHFace2024.xml')
print('Modelo almacenado...')
