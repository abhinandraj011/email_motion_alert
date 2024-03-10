import cv2
import time


video=cv2.VideoCapture(0) #to use the main camera use 0 and to use secondary camera write 1
time.sleep(1)# to wait for the camera to load
first_frame= None
while True:
    check, frame=video.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#the frame is converted to gray
    # to reduce size and we Use COLOR_BGR2GRAY algorithm to convert each pixel to gray

    #we add blur to graay frame reduce precision in each pixels for that we use GaussianBlur
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0 )

    if first_frame is None:
        first_frame =gray_frame_gau
    delta_frame = cv2.absdiff(first_frame,gray_frame_gau)#difference between first frame and other frame
    thresh_frame= cv2.threshold(delta_frame,60, 255, cv2.THRESH_BINARY)[1]
    dil_frame= cv2.dilate(thresh_frame,None,iterations=2)#to remove noise from thresh_frame. Higher the iteration number more processing will be applied
    contours, check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) <7000:
            continue
        x,y,w,h= cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    cv2.imshow("My Video",frame)# to show the video from camera
    key= cv2.waitKey(1)
    if key== ord("q"):# to exit from camera we press q
        break
video.release()
