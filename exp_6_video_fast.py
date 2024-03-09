import cv2
cap = cv2.VideoCapture("D:\\Godzilla.King.of.the.Monsters.[2019].BRRip.mkv")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width =  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps =  cap.get(cv2.CAP_PROP_FPS)
path = "0"

fourcc =  cv2.VideoWriter_fourcc(*"mp4v")

output = cv2.VideoWriter(path,fourcc,2,(width,height))

while True:
    ret,frame =  cap.read()
    cv2.imshow("frame",frame)
    output.write(frame)
    k = cv2.waitKey(24)
    if k == ord("q"):
        break
cap.release()
output.release()
cv2.destroyWindow()