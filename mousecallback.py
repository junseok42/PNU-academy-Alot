import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (255, 255, 255), 8)
        print(x, y)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
while True:
    cv2.setMouseCallback("image", draw_circle)
    cv2.imshow("image", img)
    if cv2.waitKey(1)&0xFF == 27:
        break





cv2.waitKey(0)
cv2.destroyAllWindows()