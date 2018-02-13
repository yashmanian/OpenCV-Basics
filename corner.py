import cv2
import numpy as np

ksize_morph = (5,5)
ksize_filter = (15,15)
sigmaX = 2.4
sigmaY = 2.4
epsilon = 6

filename = '/home/yashmanian/images/grid.png'
img = cv2.imread(filename)
img = cv2.GaussianBlur(img, ksize_filter, sigmaX, sigmaY, cv2.BORDER_CONSTANT)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
gray = np.float32(gray)
edges = cv2.Canny(thresh,150,210,3)

edges = cv2.dilate(edges,None)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, ksize_morph)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


lines = cv2.HoughLines(edges,1,np.pi/180,200)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)







cv2.imshow('Image', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()