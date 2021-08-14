import cv2
import numpy as np

def nothing(x):
    pass


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("BGR")
cv2.createTrackbar("B","BGR",0,255,nothing)
cv2.createTrackbar("G","BGR",0,255,nothing)
cv2.createTrackbar("R","BGR",0,255,nothing)

cv2.setTrackbarPos("B","BGR",255)
while True:
    b = cv2.getTrackbarPos("B","BGR")
    g = cv2.getTrackbarPos("G","BGR")
    r = cv2.getTrackbarPos("R","BGR")
    img[:] = [b,g,r]
    cv2.imshow("BGR",img)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
cv2.destroyAllWindows()