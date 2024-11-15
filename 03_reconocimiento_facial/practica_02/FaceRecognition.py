import face_recognition as fr
import os
import random
from datetime  import datetime

import cv2
import numpy as np

#Accedemos a la carpeta
path = "../../recursos/03/practica_02/personal"
images = []
clases = []
lista = os.listdir(path)

#imprimir lista
#print(lista)

#Variables
comp1 = 100

#Leemos los rostros de la BD
for lis in lista:
    # leemos los rostros
    imgdb = cv2.imread(f'{path}/{lis}')
    #Almacenamos imgs
    images.append(imgdb)
    # Almacenamos nombres
    clases.append(os.path.splitext(lis)[0])
print(clases)

#Funcion para codificar los rostros
def codrostros(images):
    listacod = []

    #Pasamos la lista de imagenes a RGB
    for img in images:
        #Correcion de color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #Codificamos la imagen
        cod = fr.face_encodings(img)[0]

        #Agregamos a la lista de codigos
        listacod.append(cod)

    return listacod

#Hora de ingreso
def horario(nombre):
    #Abrimos el archivo en modo lecutura y escritura
    with open('Horario.csv', 'r+') as h:
        #Leemos la informacion
        data = h.readlines()
        #Creamos la lista de nombres
        lista_nombres = []

        #Iteamos cada linea del doc
        for linea in data:
            #Dividimos la linea por comas
            entrada = linea.split(',')
            #Agregamos el nombre a la lista
            lista_nombres.append(entrada[0])

        #Verificamos si ya hemos almacenado el nombre
        if nombre not in lista_nombres:
            #Extraemos informaciona acutal
            info =  datetime.now()
            #Extraemos la fecha
            fecha = info.strftime('%Y:%m:%d')
            #Extraemos la hora
            hora = info.strftime('%H:%M:%S')

            #Guardamos la informacion
            h.writelines(f'\n{nombre}, {fecha}, {hora}')
            print(info)

#Llamamos la funcion
rostros = codrostros(images)

#Realizamos videocaptura
cap = cv2.VideoCapture(0)

#Empezamos
while True:
    #Leemos los fotogramas
    ret, frame = cap.read()

    #Reducimos las imagenes para mejorar procesamiento
    frame2 = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

    #Conversion de color
    rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    #Buscamos los rostros
    faces = fr.face_locations(rgb)
    facescod = fr.face_encodings(rgb, faces)

    #Iteramos
    for facecod, faceloc in zip(facescod, faces):
        #Comparamos rostros de BD con rostro en tiempo real
        comparacion = fr.compare_faces(rostros, facecod)

        #Calculamos la Similitud
        simi = fr.face_distance(rostros, facecod)
        #print(simi)
        #Buscamos la similitud minima
        min = np.argmin(simi)
        #print(min)

        if comparacion[min]:
            nombre = clases[min].upper()
            #print(nombre)
            #Extraemos coordenadas
            yi, xf, yf, xi = faceloc
            #Escalamos
            yi, xf, yf, xi = yi * 4, xf * 4, yf * 4, xi * 4

            indice = comparacion.index(True)

            #Comparamos
            if comp1 != indice:
                #Para dibujar cambiamos colores
                r = random.randrange(0,255,50)
                g = random.randrange(0, 255, 50)
                b = random.randrange(0, 255, 50)

                comp1 = indice

            if comp1 == indice:
                #Dibujamos
                cv2.rectangle(frame,  (xi, yi), (xf, yf), (r, g, b), 3)
                cv2.rectangle(frame, (xi, yf-35),  (xf, yf), (r, g, b), cv2.FILLED)
                cv2.putText(frame, nombre, (xi + 6, yf - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                horario(nombre)

    #Mostramos los Frames
    cv2.imshow("Reconocimiento Facial", frame)

    t = cv2.waitKey(5) #Tiempo de espera

    if t == 27:
       break







