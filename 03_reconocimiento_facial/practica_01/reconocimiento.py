import cv2
import os


data_path = '../../recursos/03/practica_01/data'
img_paths = os.listdir(data_path)
clasficador_rostro = "../haarcascades/haarcascade_frontalface_default.xml"
#print("imag_path=", img_paths)


face_recognizer = cv2.face.LBPHFaceRecognizer.create()
face_recognizer.read('modeloLBPHFace2024.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

carga_clasificador_rostro = cv2.CascadeClassifier(clasficador_rostro)

while True:
    ret, frame  = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aux_frame = gray.copy()

    faces = carga_clasificador_rostro.detectMultiScale(gray, 1.3, 5)

    for  (x, y, w, h) in faces:
        rostro = aux_frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

        if result[1] < 83:
            cv2.putText(frame, '{}'.format(img_paths[result[0]]), (x, y-25), 2, 1.1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()





