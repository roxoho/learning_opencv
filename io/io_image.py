import os
import cv2

#input
img_path = os.path.join('.',"test.jpg")

img = cv2.imread(img_path)
#print(img.shape)

#write
cv2.imwrite(os.path.join('.',"test2.jpg"),img)


#visualize

cv2.imshow('image',img)
cv2.waitKey(0)
