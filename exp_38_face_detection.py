import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\USER\\Downloads\\haarcascade_frontalface_default.xml")

image = cv2.imread("D:\\DSA0211_Computer_vision_with_open_cv_for_feature_extraction\\images\\face.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
