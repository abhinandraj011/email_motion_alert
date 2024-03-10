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

    cv2.imshow("My Video",frame)# to show the video from camera
    key= cv2.waitKey(1)
    if key== ord("q"):# to exit from camera we press q
        break
video.release()
