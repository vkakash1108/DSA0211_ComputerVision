import cv2
import numpy as np

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg")
kernel = np.ones((5,5),np.uint8)
grad = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Original",img)
cv2.imshow("Gradient",grad)
cv2.waitKey(0)
cv2.destroyAllWindows()