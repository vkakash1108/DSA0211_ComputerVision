import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg"
a = cv2.imread(image_path)

gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian_output = np.uint8(np.absolute(laplacian))

plt.subplot(121), plt.imshow(laplacian_output, cmap='gray')
plt.title('Laplacian Filter'), plt.xticks([]), plt.yticks([])

kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

sharpened = cv2.filter2D(a, -1, kernel)

plt.subplot(122), plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.title('Sharpening Filter'), plt.xticks([]), plt.yticks([])

plt.show()
