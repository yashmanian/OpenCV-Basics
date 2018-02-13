import cv2
import numpy as np

img = cv2.imread('/home/yashmanian/images/ironman.jpg', 1)

cv2.line(img, (0,0), (150,150), (255,255,255),  5)  # Order is BGR
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
cv2.circle(img, (100,25), 50, (0,0,255), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10],[12,67]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

cv2.imshow('image', img)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial', (130,130), font, 3, (200,255,255), 2, cv2.LINE_AA)

cv2.waitKey(0)
cv2.destroyAllWindows()

