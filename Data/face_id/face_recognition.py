''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18  

'''

import cv2
import numpy as np
import threading
# from Data.face_id.gfd.py.video.capture import VideoCaptureThreading
import os

global tag


def face_reg():
    cam = cv2.VideoCapture(0)

    def start():
        started = True
        thread = threading.Thread(target=update, args=())
        thread.start()
        return started

    def update():
        started = start()
        read_lock = threading.Lock()
        while started:
            grabbed, frame = cam.read()
            with read_lock:
                grabbed = grabbed
                frame = frame

    def read():
        read_lock = threading.Lock()
        with read_lock:
            frames, grabbed = cam.read()
            grabbed = grabbed
        return grabbed, frames

    def stop():
        thread = threading.Thread(target=update, args=())
        started = False
        thread.join()

    global tag
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    # iniciate id counter
    tag = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Wither', 'Paula', 'Wither', 'Z', 'W']

    # Initialize and start realtime video capture
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # print(type(cam.get(3)))
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    start()
    read()
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        tag, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if confidence < 100:
            tag = names[tag]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            tag = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(tag), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        return tag

    cv2.imshow('camera', img)

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    stop()
    cv2.destroyAllWindows()


def main():
    while True:
        face_reg()
        name = face_reg()
        print(str(name))


main()
