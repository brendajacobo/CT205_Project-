'''
A testing file for spotifymood.py to test its importability.
Uses threads to be able to run the face analysis in the background while acting on data from that analysis.
'''
import spotifymood as sp
import threading
import time

def loadSpotify(status):
    print(status)

test = sp.face_detect()
x = threading.Thread(target=test.start_detect, daemon = True)
x.start()
while True:
    if test.smile_detected is True:
        loadSpotify(True) # here is where we will tell our spotify module to 



