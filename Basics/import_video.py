import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/yashmanian/images/output.avi', fourcc, 20.0, (800,600))

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	if cv2.waitKey(1) and 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destrotAllWindows()
