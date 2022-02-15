import cv2
import webbrowser 

cap = cv2.VideoCapture(0)

# initialize the cv2 QRcode detector

detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        Info = data
        break
    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break


ContactTracingData = webbrowser.open(str(Info))
cap.release()
cv2.destroyAllWindows()

lines = ['ContactTracingData.txt']
with open('ContactTracingData.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
