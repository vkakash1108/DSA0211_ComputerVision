import cv2
import numpy as np


image = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg")

tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

height, width = image.shape[:2]
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
