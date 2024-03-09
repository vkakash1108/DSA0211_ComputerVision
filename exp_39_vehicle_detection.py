import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("C:\\Users\\USER\\Downloads\\archive (6)\\yolov3.cfg", "C:\\Users\\USER\\Downloads\\archive (7)\\yolov3.weights")
layer_names = net.getUnconnectedOutLayersNames()

# Load video
cap = cv2.VideoCapture("C:\\Users\\USER\\Downloads\\pexels_videos_2099568 (1080p).mp4")  # Replace with the path to your video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # Convert frame to blob for YOLO processing
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Run YOLO forward pass
    detections = net.forward(layer_names)

    # Process YOLO detections
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_id == 2:  # Class ID 2 corresponds to 'car'
                center_x = int(obj[0] * width)
                center_y = int(obj[1] * height)
                w = int(obj[2] * width)
                h = int(obj[3] * height)

                # Calculate bounding box coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Draw bounding box and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                label = f"Car: {confidence:.2f}"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Vehicle Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
