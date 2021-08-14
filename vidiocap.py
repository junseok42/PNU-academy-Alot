import cv2

cap = cv2.VideoCapture(0)

width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)

print(width,height,fps)
while True:
    ret, frame = cap.read()
    if ret == False:
        continue
    cv2.imshow("video",frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cv2.destroyAllWindows()