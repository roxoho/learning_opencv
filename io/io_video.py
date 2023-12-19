import os
import cv2

#input
video_path = os.path.join('.',"test_video.mp4")

video=cv2.VideoCapture(video_path)

#visualize

ret = True

while ret:
    ret, frame=video.read()

    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(34)

video.release()
cv2.destroyAllWindows()