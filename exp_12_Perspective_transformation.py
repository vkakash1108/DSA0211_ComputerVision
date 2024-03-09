import cv2
import numpy as np

img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg")

rows, cols, ch = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("Transformed Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()