#resizing

import os, cv2

img = cv2.imread(os.path.join('.',"test.jpg"))

resized_img=cv2.resize(img,(960,540))

print(img.shape)
print(resized_img.shape)

cv2.imshow('image',img)
cv2.imshow('resized_image',resized_img)

cv2.waitKey(0)