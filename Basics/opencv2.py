from PIL import Image
from numpy import *
from pylab import *

import cv2

# Display Window
cv2.namedWindow("Color Image")
cv2.namedWindow("Grayscale")

# Read image
im = cv2.imread("/home/yashmanian/images/mark2.jpg")

# Create a grayscale version
gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)

# Dimensions of the image
h,w = im.shape[:2]

# Print dimensions
print h,w

# Save image
cv2.imwrite("/home/yashmanian/images/result2.jpg",gray)

# Show image
cv2.imshow("Color Image", im)
cv2.imshow("Grayscale", gray)

# Exit after closing window
cv2.waitKey(0)
cv2.destroyAllWindows()


