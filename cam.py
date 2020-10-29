# import cv2 as cv
# import numpy as np
# cap = cv.VideoCapture(0)
# while(1):
#     # Take each frame
#     _, frame = cap.read()
#     # Convert BGR to HSV
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50])
#     upper_blue = np.array([130,255,255])
#     # Threshold the HSV image to get only blue colors
#     mask = cv.inRange(hsv, lower_blue, upper_blue)
#     # Bitwise-AND mask and original image
#     res = cv.bitwise_and(frame,frame, mask= mask)
#     cv.imshow('frame',frame)
#     cv.imshow('mask',mask)
#     cv.imshow('res',res)
#     k = cv.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv.destroyAllWindows()

import cv2


import numpy as np



cap = cv2.VideoCapture(0)
ret, current_frame = cap.read()
previous_frame = current_frame

while(cap.isOpened()):
	current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
	previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)    

	frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)

	print(np.mean(frame_diff))

	kernel = np.ones((5,5),np.uint8)
	close_operated_image = cv2.morphologyEx(frame_diff, cv2.MORPH_CLOSE, kernel)
	_, thresholded = cv2.threshold(close_operated_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	median = cv2.medianBlur(thresholded, 5)


	cv2.imshow('frame diff ',median)
	key = cv2.waitKey(0) & 0xFF
	key = cv2.waitKey(1) & 0xFF
	if key == ord('n'):
		print('new')   
	if key == ord('q'):
		break

	previous_frame = current_frame.copy()
	ret, current_frame = cap.read()

cap.release()
cv2.destroyAllWindows()



