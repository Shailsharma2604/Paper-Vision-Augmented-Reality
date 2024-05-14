import cv2 
import numpy as np

dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

markerImage = np.zeros((200, 200), dtype=np.uint8)
markerImage = cv2.aruco.drawMarker(dictionary, 1, 200, markerImage, 1)

cv2.imwrite("arucomarker.png", markerImage)
