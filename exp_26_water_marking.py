import cv2

image_path = "D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\img_2.jpeg"
original_image = cv2.imread(image_path)

watermark_path = "C:\\Users\\USER\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-03-04 123111.png"
watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

watermark_resized = cv2.resize(watermark, (100, 100))

x_offset = 10
y_offset = 10
roi = original_image[y_offset:y_offset + watermark_resized.shape[0], x_offset:x_offset + watermark_resized.shape[1]]

alpha = watermark_resized[:, :, 3] / 255.0
alpha_inv = 1.0 - alpha

for c in range(0, 3):
    roi[:, :, c] = (alpha * watermark_resized[:, :, c] + alpha_inv * roi[:, :, c])

cv2.imshow('Watermarked Image', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
