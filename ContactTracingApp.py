import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser
import datetime

cap = cv2.VideoCapture(0)

now = datetime.datetime.now()
print("Current date and time is:")
print(now.strftime("%m-%d-%y %H:%M:%S"))


while True:
    _, img = cap.read()

    data = pyzbar.decode(img)
    #print(data)
    with open('qrcodeData.txt', 'w') as output:
        output.writelines(str(data))
        output.write('Date and Time:')
        output.write(now.strftime("%m-%d-%y %H:%M:%S"))
    
    cv2.imshow("QRCODEscanner", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break








