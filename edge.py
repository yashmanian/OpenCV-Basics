import cv2
import numpy as np

ksize_morph = (5,5)
ksize_filter = (15,15)
sigmaX = 2.4
sigmaY = 2.4


filename = '/home/yashmanian/images/Imgs/IMG_20170209_042606.jpg'
img = cv2.imread(filename)
#img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.GaussianBlur(img, ksize_filter, sigmaX, sigmaY, cv2.BORDER_CONSTANT)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

thresh = np.float32(thresh)

dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
dst = cv2.erode(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('Image',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()