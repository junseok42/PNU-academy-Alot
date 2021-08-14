import cv2


width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)
cap = cv2.VideoCapture(0)#0은 카메라
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("output.avi", fourcc,30.0, (480,640))#변수대입가능


print(width,height,fps)
while True:
    ret, frame = cap.read()
    #if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        #cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        #break
    if ret == False:
        continue
    cv2.imshow("video",frame)
    writer.write(frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()