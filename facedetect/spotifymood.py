import numpy as np
import cv2
from pprint import pprint

casc_class = 'haarcascade/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_class)

smile_casc = 'haarcascade/haarcascade_smile.xml'
smile_cascade = cv2.CascadeClassifier(smile_casc)

scaleFactor = 1.25

if face_cascade.empty():
    print('WARNING: Cascade did not load')

my_video = cv2.VideoCapture(0)

while True:
    ret, frame = my_video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
            )        
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,55,0),2)


    cv2.imshow("face and eyes", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

my_video.release()
cv2.destroyAllWindows()