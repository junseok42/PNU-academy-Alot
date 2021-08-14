import time
import cv2

def videoDetector(cap, face_cascade, eye_cascade):
    Face_Base_time = Face_Start_time = Eyedown_Base_time = Eyedown_Start_time = Eyeup_Base_time = Eyeup_Start_time = time.time() # 변수선언
    while True:
        ret, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        Height, Width = img_gray.shape # 화면 크기
        faces = face_cascade.detectMultiScale(img_gray,  # 입력 이미지
                                           scaleFactor=1.1,  # 이미지 피라미드 스케일 factor
                                           minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                           minSize=(20, 20)  # 탐지 객체 최소 크기
                                         )
        if len(faces): # 얼굴이 있는지 없는지 판단
            Face_Base_time = Face_Start_time = time.time() # 0초로 초기화
            for (f_x, f_y, f_w, f_h) in faces:
                cv2.rectangle(img, (f_x, f_y), (f_x + f_w, f_y + f_h), (0, 255, 0), 2)

                face = img[f_y: f_y+f_h, f_x: f_x+f_w]
                face_gray = img_gray[f_y: f_y+f_h, f_x: f_x+f_w]
                eyes = eye_cascade.detectMultiScale(face_gray,
                                                    scaleFactor=1.1,
                                                    minNeighbors=5,
                                                    minSize=(50, 50),
                                                    maxSize=(60, 60)
                                                    )

                if len(eyes): # 눈이 있는지 없는지 판단
                    Eyedown_Base_time = Eyedown_Start_time = Eyeup_Start_time = time.time() # 0초로 초기화
                    Eyeup_timer = Eyeup_Start_time - Eyeup_Base_time
                    for(e_x, e_y, e_w, e_h) in eyes:
                        cv2.rectangle(face, (e_x, e_y), (e_x + e_w, e_y + e_h), (255, 0, 0), 2)
                        if Eyeup_timer >= 60:
                            cv2.rectangle(img, (0, 0), (Width, Height), (0, 0, 255), 3)
                            cv2.putText(img, 'Picture', (f_x, f_y - 10), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0 ,255))
                else:
                    Eyedown_Start_time = Eyeup_Base_time =time.time() # 0초로 초기화
                    Eyedown_timer = Eyedown_Start_time - Eyedown_Base_time
                    if Eyedown_timer >= 5:
                        cv2.rectangle(img, (0,0), (Width, Height), (0, 0, 255), 3)
                        cv2.putText(img, 'Sleep', (f_x, f_y - 10), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))

        else:
            Face_Start_time = time.time()
            Face_timer = Face_Start_time - Face_Base_time
            cv2.putText(img, f'Time : {int(Face_timer)}', (0, 40), 1, 2, (0, 0, 255))
            if Face_timer >= 5:
                cv2.rectangle(img, (0, 0), (Width, Height), (0, 0, 255), 3)
                cv2.putText(img, 'Disappeared', (0, 100), 1, 3, (0, 0, 255))

        cv2.imshow("img_result", img)

        if cv2.waitKey(1)&0xFF == 27:
            break

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
videoDetector(cap, faceCascade, eyeCascade)

cv2.destroyAllWindows()