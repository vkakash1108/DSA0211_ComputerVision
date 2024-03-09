import cv2
import numpy as np

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg",cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("original",img)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()