import cv2
import numpy as np
from pyzbar import pyzbar
import webbrowser 

cap = cv2.VideoCapture(0)

# initialize the cv2 QRcode detector

detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()

    # detect and decode
    
    decodedObjects = pyzbar.decode(img)
    for lines in decodedObjects:
        open('decodedobjects', decodedObjects.txt)
    
    cv2.imshow("QRCODEscanner", img)
    key = cv2.waitKey(1)
    if key == 30:
        break





