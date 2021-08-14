import cv2
import numpy as np

img = cv2.imread("lambo.png")


def nothing(x):
    pass


cv2.namedWindow("Trackbar",cv2.WINDOW_NORMAL)
cv2.createTrackbar("H min", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("H max", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("S min", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("S max", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("V min", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("V max", "Trackbar", 0, 255, nothing)
while True:

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("H min", "Trackbar")
    hmax = cv2.getTrackbarPos("H max", "Trackbar")
    smin = cv2.getTrackbarPos("S min", "Trackbar")
    smax = cv2.getTrackbarPos("S max", "Trackbar")
    vmin = cv2.getTrackbarPos("V min", "Trackbar")
    vmax = cv2.getTrackbarPos("V max", "Trackbar")
    lower = np.array([hmin, smin, vmin])
    higher = np.array([hmax, smax, vmax])

    img_mask = cv2.inRange(img_hsv, lower, higher)

    img_result = cv2.bitwise_and(img, img, mask=img_mask)

    cv2.imshow("1", img)
    cv2.imshow("2", img_hsv)
    cv2.imshow("3", img_mask)
    cv2.imshow("4", img_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
