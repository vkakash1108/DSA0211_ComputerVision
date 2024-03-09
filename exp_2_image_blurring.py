import cv2
import numpy as np

kernel =  np.ones((10,10),np.uint8)
print(kernel)

path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg"
img = cv2.imread(path)

imgBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Img Blur", imgBlur)
cv2.waitKey(0)