#warpPerspective


import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img, (x, y), 50, (255, 255, 255), 8)
        print(x, y)
width, height = 250, 350
img = cv2.imread("cards.jpg")
pts1 = np.float32([[113,222],[285,191],[159,478],[349,434]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_result = cv2.warpPerspective(img, matrix, (width,height))


cv2.imshow("image", img)
cv2.imshow("mat",img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()