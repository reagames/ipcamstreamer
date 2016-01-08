#ip camera openCV streamer for DLink DCS-932L




import cv2
import urllib 
import numpy as np
import sys

#stream=urllib.urlopen('http://admin:CmasQp123@192.168.1.46:8088/mjpeg.cgi?user=admin&password=CmasQp123&channel=0&.mjpg')

stream=urllib.urlopen('http://admin:CmasQp123@192.168.1.46/mjpeg.cgi?user=admin&password=CmasQp123&channel=0&.mjpg')

print(sys.argv)

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow('stream',frame)
    
    if cv2.waitKey(1) ==27:
            exit(0) 


cv2.destroyAllWindows()
