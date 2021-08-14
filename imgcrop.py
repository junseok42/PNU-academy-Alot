import cv2

img = cv2.imread("rose.jpg")
print(img.shape)
img_crop = img[100:500, 300:700]
cv2.imshow("rose",img)
cv2.imshow("rose2",img_crop)



cv2.waitKey(0)
cv2.destroyAllWindows()


#이미지 색상변경

import cv2

img = cv2.imread("rose.jpg")
print(img.shape)
img_crop = img[100:500, 300:700]
img_gray = cv2.cvtColor(img_crop,cv2.COLOR_BGR2GRAY)
cv2.imshow("rose",img)
cv2.imshow("rose2",img_gray)



cv2.waitKey(0)
cv2.destroyAllWindows()



#이미지 크기변경


import cv2

img = cv2.imread("rose.jpg")
print(img.shape)
img_crop = img[100:500, 300:700]
img_gray = cv2.cvtColor(img_crop,cv2.COLOR_BGR2GRAY)
img_resize =cv2.resize(img,(472,314))
#img_resize =cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow("rose",img)
cv2.imshow("rose2",img_gray)
cv2.imshow("rose3",img_resize)



cv2.waitKey(0)
cv2.destroyAllWindows()