import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(250,250))
cv2.imshow("image",img)
cv2.waitKey(0)