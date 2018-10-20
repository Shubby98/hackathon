import cv2
import numpy as np



first_frame = None
cam = cv2.VideoCapture(0)

status_list = []


while True:
    ret,frame = cam.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    
        

    if first_frame is None:
        first_frame = gray
        continue


    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    #th = cv2.adaptiveThreshold(delta_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts:
        if cv2.contourArea(contour) < 8000:
            continue
        status = 1

        (x,y,w,h) = cv2.boundingRect(contour)
        crop_img = frame[x:x+w,y:y+h]
        cv2.imshow
        #('cropped.jpg',crop_img)
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0), 3)

        
            
    status_list.append(status)
    cv2.imshow('frame',frame)
    cv2.imshow('delta',delta_frame)
    #cv2.imshow('gray',gray)
    cv2.imshow('thresh_frame',thresh_frame)
    
    

    key = cv2.waitKey(1)
    if key == ord('q'):
        break



print(status_list)
     
cam.release()
cv2.destroyAllWindows


