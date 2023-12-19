import os, cv2

img= cv2.imread(os.path.join('.','test.jpg'))

#resize
resized_img=cv2.resize(img,(960,540))

img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

cv2.imshow('image',resized_img)
cv2.imshow('rgb_image',img_rgb)
cv2.imshow('grayscale_image',img_gray)
cv2.imshow('hsv_image',img_hsv)

cv2.waitKey(0)