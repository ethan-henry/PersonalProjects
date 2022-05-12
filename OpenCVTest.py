import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\echan\Desktop\CS\Personal\Haar Cascade\haarcascade_frontalface_default.xml')
smiles_cascade = cv2.CascadeClassifier('C:\\Users\echan\Desktop\CS\Personal\Haar Cascade\haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\echan\Desktop\CS\Personal\Haar Cascade\haarcascade_eye.xml')

vid = cv2.VideoCapture(0)

while(True):
    ret, img = vid.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    smiles = smiles_cascade.detectMultiScale(gray, 2.5, 15)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for (x,y,w,h) in eyes:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    for (x,y,w,h) in smiles:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('img', img)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()