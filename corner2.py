import cv2
import numpy as np

ksize_morph = np.ones((7,7), np.uint8)
ksize_filter = (15,15)
sigmaX = 2.4
sigmaY = 2.4


filename = '/home/yashmanian/images/Imgs/ironman.jpg'
img= cv2.imread(filename)
height, width, channels = img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


gray = cv2.GaussianBlur( gray, (11, 11), 2, 2 , cv2.BORDER_CONSTANT)
ret, bin = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
masked = cv2.multiply(gray, bin)
masked = np.float32(masked)

dst = cv2.cornerHarris(masked,5,7,0.04)
dst = cv2.dilate(dst, ksize_morph, iterations=1)

cv2.imshow(dst)



if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()