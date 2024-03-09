import cv2
import numpy as np

img1 = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg")
img2 = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg")

pts1 = np.array([[50,50],[200,50],[50,200],[200,200]])
pts2 = np.array([[100,100],[300,100],[100,300],[300,300]])

H,_ = cv2.findHomography(pts1,pts2)
dst = cv2.warpPerspective(img1,H,(img2.shape[1],img2.shape[0]))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
