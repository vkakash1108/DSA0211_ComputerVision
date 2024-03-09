import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg"

img = cv2.imread(path)
imgcanny = cv2.Canny(img,100,200)
cv2.imshow("Img Canny",imgcanny)
cv2.waitKey(0)