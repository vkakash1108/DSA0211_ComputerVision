import cv2
import numpy as np

image = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg")
img2 = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg")

print(image.shape)
cv2.imshow("original",image)
imageCopy = image.copy()
cv2.circle(imageCopy,(100,100),30,(255,0,0),-1)
cv2.imshow('image',image)
cv2.imshow('image copy',imageCopy)
cropping_image = image[80:280, 150:330]
cv2.imshow("cropped image",cropping_image)
cv2.imwrite("cropped image.jpg",cropping_image)
dst = cv2.addWeighted(image,0.5,img2,0.7,0)
img_arr = np.hstack((image,img2))
cv2.imshow('input images',img_arr)
cv2.imshow('blended image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()