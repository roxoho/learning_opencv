#crop
import os, cv2

img = cv2.imread(os.path.join('.',"test.jpg"))

print(img.shape)

cropped_img=img[600:1080,600:1350]

cv2.imshow('image',img)
cv2.imshow('cropped_image',cropped_img)
cv2.waitKey(0)