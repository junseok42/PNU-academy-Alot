import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0), (512,512), (0,0,255), 3)
cv2.rectangle(img,(50,50),(200,100), (0,0,255), 2)
cv2.circle(img, (256,256), 100, (255,255,255),2)
cv2.putText(img,"Hello",(0,200v),cv2.FONT_HERSHEY_SIMPLEX, 1 ,(255,0,0),2)
cv2.namedWindow("Black")
cv2.imshow('Black', img)
cv2.waitKey(0)
cv2.destroyAllWindows()