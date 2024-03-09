import cv2
import numpy as np

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_1.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (0, 0), 3)

high_boost_mask = gray - blur

boost_factor = 2.0

sharpened_image = gray + boost_factor * high_boost_mask

sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
