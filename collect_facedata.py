''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc  

Original Ref : https://github.com/Mjrovai/OpenCV-Face-Recognition/blob/master/FacialRecognition/01_face_dataset.py   

Developed by Rahul Roy @17th Nov 2021  
'''

import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()