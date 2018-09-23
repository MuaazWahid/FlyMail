import numpy as np
import cv2

img = cv2.imread('mouse1.jpg', cv2.IMREAD_COLOR)

px = img[55,55]

roi = img[100:150, 100:150]

#img[100:150, 100:150] = [255,255,255]

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 500, 500)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
