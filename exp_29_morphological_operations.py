import cv2
import numpy as np

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Unable to load the image.")
else:
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Original", img)
    cv2.imshow("Erosion", erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
