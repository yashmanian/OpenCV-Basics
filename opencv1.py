from PIL import Image
from numpy import *
from pylab import *

import cv2

# Window to display image
cv2.namedWindow("Image")


# Read image
image = cv2.imread("/home/yashmanian/images/ironman.jpg")
h,w = image.shape[:2]
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
image[dst>0.01*dst.max()]=[0,0,255]

# Save image
#cv2.imwrite("/home/yashmanian/images/result1.jpg",image)

# Show image 
cv2.imshow("Image",dst)

# Exit on closing window
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
