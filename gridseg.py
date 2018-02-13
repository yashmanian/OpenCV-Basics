import cv2
import numpy as np

ksize_morph = np.ones((7,7), np.uint8)
ksize_filter = (11,11)
sigmaX = 2.4
sigmaY = 2.4


filename = '/home/yashmanian/images/sudoku.jpg'
img= cv2.imread(filename)
height, width, channels = img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur( gray, ksize_filter , cv2.BORDER_CONSTANT)

ret, bin = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bin)



if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()