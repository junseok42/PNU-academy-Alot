import cv2

cap = cv2.VideoCapture("test_video.mp4")#0은 카메라

width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)

print(width,height,fps)
while True:
    ret, frame = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        #break
    if ret == False:
        continue
    cv2.imshow("video",frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cv2.destroyAllWindows()