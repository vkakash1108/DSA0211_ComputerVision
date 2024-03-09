import cv2
path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg"
src =  cv2.imread(path)

angles = [cv2.ROTATE_90_CLOCKWISE,cv2.ROTATE_180,cv2.ROTATE_90_COUNTERCLOCKWISE]
rotation = []

for a in angles:
    rotate_degree = cv2.rotate(src, a)
    rotation.append(rotate_degree)

for rotate in rotation:
    cv2.imshow("Image", rotate)
    cv2.waitKey(0)