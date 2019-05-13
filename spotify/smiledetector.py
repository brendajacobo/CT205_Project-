'''
Author: Tanner Yost
CST 205 Group 5 project
Members: Brenda Jacobo, Aminata Seck, Carmelo Hernandez, Tanner Yost
This file is to be used as an import, as it will internally keep track of emotions it is detecting and our other scripts will react accordingly to that.
'''

import numpy as np
import cv2
from pprint import pprint
'''

'''

class face_detect():
    def __init__(self):
        self.execute = True
        self.smile_detected = False
        self.casc_class = 'haarcascade/haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(self.casc_class)

        self.smile_casc = 'haarcascade/haarcascade_smile.xml'
        self.smile_cascade = cv2.CascadeClassifier(self.smile_casc)

        self.scaleFactor = 1.25

        if self.face_cascade.empty():
            print('WARNING: Cascade did not load')

    def stop(self):
        self.execute = False

    def isStopped(self):
        return self.execute

    def getDetection(self):
        return self.smile_detected

    def start_detect(self, q):
        my_video = cv2.VideoCapture(0)
        while self.execute:
            ret, frame = my_video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(frame, 1.3, 5)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                smile = self.smile_cascade.detectMultiScale(
                    roi_gray,
                    scaleFactor= 1.7,
                    minNeighbors=28,
                    minSize=(100, 100),
                    flags=cv2.CASCADE_SCALE_IMAGE
                    )        
                for (sx,sy,sw,sh) in smile:
                    self.smile_detected = True
                    q.put(True)
                    cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,55,0),2)
            self.smile_detected = False


            cv2.imshow("face and eyes", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        my_video.release()
        cv2.destroyAllWindows()
