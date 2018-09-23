import cv2
import numpy as np
import sys
import pytesseract
import serial
from PIL import Image, ImageEnhance, ImageFilter
#for i in range(3):
 #   capture = cv2.VideoCapture(i)
  #  if capture: print(i)

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0)
print(ser.name)
def readport(ser):
	while not connected:
		connected = True

	while True:
		reading = ser.readline.decode()

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.start()
#VideoCapture.set(CV_CAP_PROP_CONVERT_RGB, false
def takePic():
    cap = cv2.VideoCapture("/dev/video2")

    if (cap.isOpened()== False):
            print("ERROR OPENING STREAM!!!")

    #cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    #cv2.resize('frame', 900,900)
    config = ('-1 eng --oem 1 --psm 3')
    ret, frame = cap.read()
    cv2.imwrite("letter.png", frame)
    #gray = cv2.cvtColor("letter.png", cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("letter.png", gray)
    text = pytesseract.image_to_string("letter.png")
    print(text)
    f = open("storage.txt", "a")
    f.write(text.encode('utf-8'))


    while (cap.isOpened()):
        #ret, frame = cap.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

takePic()
ser.close()
