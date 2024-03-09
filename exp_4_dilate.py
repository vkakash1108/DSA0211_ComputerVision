import cv2
import numpy as np

kernel = np.ones((10,10), np.uint8)
print(kernel)

path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg"

img = cv2.imread(path)

imgDilate = cv2.dilate(img, kernel, iterations=10)
cv2.imshow("Img Dilate", imgDilate)
cv2.waitKey(0)