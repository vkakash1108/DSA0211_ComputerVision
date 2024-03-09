import cv2

# Initialize variables
drawing = False  # True if mouse is pressed
ix, iy = -1, -1  # Initial coordinates of the mouse
extracted_objects = []


# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

        # Extract the object and append it to the list
        extracted_object = img[iy:y, ix:x]
        extracted_objects.append(extracted_object)


# Read an image
img = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\watch_2.jpeg")  # Replace with your image path
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rectangle)

while True:
    cv2.imshow('Image', img)

    # Press 'e' to exit the loop and display extracted objects
    key = cv2.waitKey(1) & 0xFF
    if key == ord('e'):
        break

# Display extracted objects
for i, obj in enumerate(extracted_objects):
    cv2.imshow(f'Object {i + 1}', obj)

cv2.waitKey(0)
cv2.destroyAllWindows()
