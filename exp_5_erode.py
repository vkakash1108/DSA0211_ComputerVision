import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)

path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg"

img = cv2.imread(path)

imgEroded = cv2.erode(img,kernal,iterations=2)
cv2.imshow("Img Erosion", imgEroded)
cv2.waitKey(0)