import numpy as np
import cv2
import RPi.GPIO as g
import time 
 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cuerpo_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture(0)
encender = False
cont = 0

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(18,g.OUT)

cap.set(3,640)
cap.set(4,480)
 
while(True):
    #leemos un frame y lo guardamos
    ret, img = cap.read()
 
    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.3, 1) #estos valores modfican lasensibilidad de econocimiento
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),1)
        encender = True
        cont+=1
    
    cuerpo = cuerpo_cascade.detectMultiScale(gray, 1.3, 1) #estos valores modfican lasensibilidad de econocimiento
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in cuerpo:
       cv2.rectangle(img,(x,y),(x+w,y+h),(45,45,45),1)

    if(encender):
        g.output(18, g.HIGH)
       
    else:
        g.output(18, g.LOW)
    encender = False
    f=open("/var/www/html/SecurityCam/intrusos.txt","w")
    f.write(""+repr(cont))
    f.close()
    cont = 0
 
    #Mostramos la imagen
    #cv2.imshow('TITULO DE VENTANA',img)
    cv2.imwrite("/var/www/html/SecurityCam/img.jpg",img) 
    #con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2-DestroyWindow() #cambiar destroy all windows a linux
