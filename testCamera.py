import cv2
import numpy as np

#for i in range(3):
 #   capture = cv2.VideoCapture(i)
  #  if capture: print(i)


#VideoCapture.set(CV_CAP_PROP_CONVERT_RGB, false)

cap = cv2.VideoCapture(2)

if (cap.isOpened()== False):
	print("ERROR OPENING STREAM!!!")

#cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
#cv2.resize('frame', 900,900)
ret, frame = cap.read()
while (cap.isOpened()):
    #ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
